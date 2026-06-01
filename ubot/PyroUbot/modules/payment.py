import asyncio
from datetime import datetime

from dateutil.relativedelta import relativedelta
from pytz import timezone
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from PyroUbot import *
from PyroUbot.config import (
    ROLE_PRICES,
    NOTIFY_CHANNEL,
    NOTIFY_THUMBNAIL,
    START_PHOTO,
    PAYMENT_TIMEOUT,
    PAYMENT_CHECK_INTERVAL,
    OWNER_USERNAME,
)
from PyroUbot.payment import create_qris, cek_status

WIB = timezone("Asia/Jakarta")

ACTIVE_PAYMENT = {}
PROCESSED_ORDER = set()

ROLE_VARS = {
    "member": ["PREM_USERS"],
    "seles": ["PREM_USERS", "SELER_USERS"],
    "admin": ["PREM_USERS", "SELER_USERS", "ADMIN_USERS"],
}


def hitung_expired(durasi):
    now = datetime.now(WIB)
    if durasi == "0":
        return now + relativedelta(years=100)
    try:
        bulan = int(durasi)
    except (TypeError, ValueError):
        bulan = 1
    if bulan < 1:
        bulan = 1
    return now + relativedelta(months=bulan)


async def aktifkan_role(user_id, role, durasi):
    for vars_name in ROLE_VARS.get(role, ["PREM_USERS"]):
        existing = await get_list_from_vars(bot.me.id, vars_name)
        if user_id not in existing:
            await add_to_vars(bot.me.id, vars_name, user_id)
    await set_expired_date(user_id, hitung_expired(durasi))


async def notif_order_sukses(user, role, durasi, amount):
    waktu = datetime.now(WIB).strftime("%d-%m-%Y %H:%M:%S")
    try:
        await bot.send_photo(
            NOTIFY_CHANNEL,
            photo=NOTIFY_THUMBNAIL,
            caption=MSG.NOTIFY_ORDER(user, role, durasi, amount, waktu),
        )
    except Exception as error:
        print(f"[INFO] - gagal kirim notif order: {error}")


async def selesaikan_pembayaran(user_id, order_id, amount, role, durasi, old_message):
    if order_id in PROCESSED_ORDER:
        return
    PROCESSED_ORDER.add(order_id)
    ACTIVE_PAYMENT.pop(user_id, None)

    await aktifkan_role(user_id, role, durasi)

    try:
        await old_message.delete()
    except Exception:
        pass

    await bot.send_message(
        user_id,
        MSG.SUCCESS_ROLE(role, durasi),
        reply_markup=InlineKeyboardMarkup(BTN.SUCCESS_UBOT()),
    )

    try:
        user = await bot.get_users(user_id)
        await notif_order_sukses(user, role, durasi, amount)
    except Exception as error:
        print(f"[INFO] - notif order: {error}")


async def auto_cek_pembayaran(user_id, order_id, amount, role, durasi, sent_message):
    ACTIVE_PAYMENT[user_id] = order_id
    elapsed = 0
    try:
        while elapsed < PAYMENT_TIMEOUT:
            await asyncio.sleep(PAYMENT_CHECK_INTERVAL)
            elapsed += PAYMENT_CHECK_INTERVAL
            if ACTIVE_PAYMENT.get(user_id) != order_id:
                return
            if order_id in PROCESSED_ORDER:
                return
            if await cek_status(order_id, amount):
                await selesaikan_pembayaran(user_id, order_id, amount, role, durasi, sent_message)
                return
        if ACTIVE_PAYMENT.get(user_id) == order_id and order_id not in PROCESSED_ORDER:
            ACTIVE_PAYMENT.pop(user_id, None)
            try:
                await sent_message.delete()
            except Exception:
                pass
            await bot.send_message(
                user_id,
                "<blockquote><b>⌛ ᴡᴀᴋᴛᴜ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ʜᴀʙɪs.\n\nsɪʟᴀʜᴋᴀɴ ᴜʟᴀɴɢɪ ᴘᴇᴍᴇsᴀɴᴀɴ ᴅᴇɴɢᴀɴ /start</b></blockquote>",
            )
    finally:
        if ACTIVE_PAYMENT.get(user_id) == order_id:
            ACTIVE_PAYMENT.pop(user_id, None)


@PY.CALLBACK("belirole")
async def _(client, callback_query):
    user_id = callback_query.from_user.id
    try:
        await smart_edit(
            callback_query,
            MSG.PILIH_ROLE(callback_query),
            reply_markup=InlineKeyboardMarkup(BTN.ROLE_SELECT(user_id)),
        )
    except Exception as error:
        await callback_query.answer(f"Error: {error}", True)


@PY.CALLBACK("rolepilih")
async def _(client, callback_query):
    data = callback_query.data.split()
    role = data[1]
    user_id = callback_query.from_user.id
    try:
        await smart_edit(
            callback_query,
            MSG.DURASI(role),
            reply_markup=InlineKeyboardMarkup(BTN.ROLE_DURASI(role, user_id)),
        )
    except Exception as error:
        await callback_query.answer(f"Error: {error}", True)


@PY.CALLBACK("roledur")
async def _(client, callback_query):
    data = callback_query.data.split()
    role = data[1]
    durasi = data[2]
    user_id = callback_query.from_user.id

    harga = ROLE_PRICES.get(role, {}).get(durasi)
    if harga is None:
        return await callback_query.answer("Role tidak valid", True)

    await callback_query.answer("Membuat QRIS pembayaran...", False)

    qris = await create_qris(harga)
    if not qris:
        buttons = [
            [InlineKeyboardButton("👤 ʜᴜʙᴜɴɢɪ ᴀᴅᴍɪɴ", url=f"https://t.me/{OWNER_USERNAME}")],
            [InlineKeyboardButton("🔙 ᴋᴇᴍʙᴀʟɪ", callback_data=f"belirole {user_id}")],
        ]
        return await smart_edit(
            callback_query,
            "<blockquote><b>❌ ɢᴀɢᴀʟ ᴍᴇᴍʙᴜᴀᴛ ǫʀɪs ᴏᴛᴏᴍᴀᴛɪs.\n\nsɪʟᴀʜᴋᴀɴ ʜᴜʙᴜɴɢɪ ᴀᴅᴍɪɴ ᴜɴᴛᴜᴋ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴍᴀɴᴜᴀʟ.</b></blockquote>",
            reply_markup=InlineKeyboardMarkup(buttons),
        )

    order_id = qris["order_id"]
    amount = qris["amount"]
    total = qris["total"]

    try:
        await callback_query.message.delete()
    except Exception:
        pass

    sent_message = await bot.send_photo(
        user_id,
        photo=qris["qr_image"],
        caption=MSG.QRIS(role, durasi, total, order_id),
        reply_markup=InlineKeyboardMarkup(
            BTN.QRIS_CHECK(order_id, amount, role, durasi, user_id)
        ),
    )

    asyncio.create_task(
        auto_cek_pembayaran(user_id, order_id, amount, role, durasi, sent_message)
    )


@PY.CALLBACK("cancelqris")
async def _(client, callback_query):
    user_id = callback_query.from_user.id
    ACTIVE_PAYMENT.pop(user_id, None)
    try:
        await callback_query.message.delete()
    except Exception:
        pass
    try:
        await bot.send_photo(
            user_id,
            START_PHOTO,
            caption=MSG.START(callback_query),
            reply_markup=InlineKeyboardMarkup(BTN.START(callback_query)),
        )
    except Exception as error:
        await callback_query.answer(f"Error: {error}", True)


@PY.CALLBACK("rolecek")
async def _(client, callback_query):
    data = callback_query.data.split()
    order_id = data[1]
    amount = int(data[2])
    role = data[3]
    durasi = data[4]
    user_id = callback_query.from_user.id

    if order_id in PROCESSED_ORDER:
        return await callback_query.answer("Pembayaran sudah diproses.", True)

    await callback_query.answer("Mengecek pembayaran...", False)

    if await cek_status(order_id, amount):
        await selesaikan_pembayaran(user_id, order_id, amount, role, durasi, callback_query.message)
    else:
        await callback_query.answer(
            "❌ Pembayaran belum masuk. Selesaikan pembayaran lalu cek lagi.", True
        )


@PY.CALLBACK("^(success|failed|home)")
async def _(client, callback_query):
    query = callback_query.data.split()
    user_target = int(query[1])

    if query[0] == "home":
        ACTIVE_PAYMENT.pop(callback_query.from_user.id, None)
        buttons_home = BTN.START(callback_query)
        return await smart_edit(
            callback_query,
            MSG.START(callback_query),
            reply_markup=InlineKeyboardMarkup(buttons_home),
        )

    get_user = await bot.get_users(user_target)

    if query[0] == "success":
        role = query[2] if len(query) > 2 else "member"
        durasi = query[3] if len(query) > 3 else "1"
        await aktifkan_role(get_user.id, role, durasi)
        await bot.send_message(
            get_user.id,
            MSG.SUCCESS_ROLE(role, durasi),
            reply_markup=InlineKeyboardMarkup(BTN.SUCCESS_UBOT()),
        )
        try:
            await notif_order_sukses(get_user, role, durasi, ROLE_PRICES.get(role, {}).get(durasi, 0))
        except Exception:
            pass
        return await callback_query.edit_message_caption(
            caption=f"<blockquote><b>✅ {get_user.first_name} ʙᴇʀʜᴀsɪʟ ᴅɪᴊᴀᴅɪᴋᴀɴ {role.upper()}</b></blockquote>",
        )

    if query[0] == "failed":
        await bot.send_message(
            get_user.id,
            "<blockquote><b>❌ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴅɪᴛᴏʟᴀᴋ / ʙᴜᴋᴛɪ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ.\n\nsɪʟᴀʜᴋᴀɴ ᴄᴏʙᴀ ʟᴀɢɪ ᴅᴇɴɢᴀɴ ʙᴜᴋᴛɪ ʏᴀɴɢ ʙᴇɴᴀʀ.</b></blockquote>",
        )
        return await callback_query.edit_message_caption(
            caption=f"<blockquote><b>❌ {get_user.first_name} ᴅɪᴛᴏʟᴀᴋ.</b></blockquote>",
        )
