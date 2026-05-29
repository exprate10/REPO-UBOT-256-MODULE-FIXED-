import io
import time
import random
import string

import aiohttp

from PyroUbot.config import PAKASIR_BASE_URL, PAKASIR_PROJECT, PAKASIR_API_KEY


def to_rupiah(angka):
    try:
        nilai = int(angka)
    except (TypeError, ValueError):
        return str(angka)
    return "Rp " + f"{nilai:,}".replace(",", ".")


def generate_order_id():
    acak = "".join(random.choices(string.ascii_uppercase + string.digits, k=8))
    return f"TRX-{int(time.time() * 1000)}-{acak}"


def sanitize_qr_string(teks):
    if not teks or not isinstance(teks, str):
        return None
    idx = teks.find("000201")
    if idx != -1:
        return teks[idx:].strip()
    return teks.strip()


def build_qris_image(qr_string):
    import qrcode

    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=2,
    )
    qr.add_data(qr_string)
    qr.make(fit=True)
    gambar = qr.make_image(fill_color="black", back_color="white")
    buffer = io.BytesIO()
    buffer.name = "qris.png"
    gambar.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer


async def create_qris(harga):
    if not PAKASIR_PROJECT or not PAKASIR_API_KEY:
        return None

    amount = int(harga)
    order_id = generate_order_id()
    payload = {
        "project": PAKASIR_PROJECT,
        "order_id": order_id,
        "amount": amount,
        "api_key": PAKASIR_API_KEY,
    }
    timeout = aiohttp.ClientTimeout(total=20)
    try:
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.post(
                f"{PAKASIR_BASE_URL}/transactioncreate/qris", json=payload
            ) as resp:
                data = await resp.json(content_type=None)
    except Exception:
        return None

    if not data or not isinstance(data, dict):
        return None

    payment = data.get("payment") or data.get("transaction") or data
    candidates = [
        payment.get("qr_string"),
        payment.get("qr"),
        data.get("qr_string"),
        data.get("qr"),
        payment.get("payment_number"),
    ]

    qr_string = None
    for kandidat in candidates:
        emv = sanitize_qr_string(kandidat) if isinstance(kandidat, str) else None
        if emv and emv.startswith("000201"):
            qr_string = emv
            break

    if not qr_string:
        return None

    try:
        qr_image = build_qris_image(qr_string)
    except Exception:
        return None

    return {
        "order_id": payment.get("order_id", order_id),
        "amount": int(payment.get("amount", amount)),
        "total": int(payment.get("total_payment", amount)),
        "qr_string": qr_string,
        "qr_image": qr_image,
        "expired_at": payment.get("expired_at"),
    }


async def cek_status(order_id, amount):
    if not PAKASIR_PROJECT or not PAKASIR_API_KEY:
        return False

    url = (
        f"{PAKASIR_BASE_URL}/transactiondetail"
        f"?project={PAKASIR_PROJECT}&amount={int(amount)}"
        f"&order_id={order_id}&api_key={PAKASIR_API_KEY}"
    )
    timeout = aiohttp.ClientTimeout(total=15)
    try:
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(url) as resp:
                data = await resp.json(content_type=None)
    except Exception:
        return False

    if data and isinstance(data, dict):
        transaksi = data.get("transaction") or {}
        status = (transaksi.get("status") or data.get("status") or "").lower()
        if status in ("completed", "success", "paid", "settled"):
            return True
    return False
