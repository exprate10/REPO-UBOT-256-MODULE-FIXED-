from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from PyroUbot import OWNER_ID, bot, ubot, get_expired_date
from PyroUbot.config import OWNER_USERNAME, MAIN_CHANNEL, NOTIFY_CHANNEL, ROLE_PRICES


def _rupiah(nilai):
    try:
        return "Rp " + f"{int(nilai):,}".replace(",", ".")
    except (TypeError, ValueError):
        return str(nilai)


ROLE_LABEL = {"member": "ᴍᴇᴍʙᴇʀ", "seles": "sᴇʟᴇs", "admin": "ᴀᴅᴍɪɴ"}
ROLE_AKSES = {
    "member": "ᴀᴋsᴇs ᴘʀᴇᴍɪᴜᴍ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ",
    "seles": "ᴀᴋsᴇs ᴘʀᴇᴍɪᴜᴍ + ᴀᴋsᴇs sᴇʟʟᴇʀ",
    "admin": "ᴀᴋsᴇs ᴘʀᴇᴍɪᴜᴍ + sᴇʟʟᴇʀ + ᴀᴅᴍɪɴ ᴘᴇɴᴜʜ",
}


class MSG:
    def EXP_MSG_UBOT(X):
        return f"""
<blockquote><b>❏ ᴘᴇᴍʙᴇʀɪᴛᴀʜᴜᴀɴ</b>
<b>├ ᴀᴋᴜɴ:</b> <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a>
<b>├ ɪᴅ:</b> <code>{X.me.id}</code>
<b>╰ ᴍᴀsᴀ ᴀᴋᴛɪꜰ ᴛᴇʟᴀʜ ʜᴀʙɪs</b></blockquote>
"""

    def START(message):
        return f"""
<blockquote><b>👋🏻 ʜᴀʟᴏ <a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a>!</b>

<b>📚 @{bot.me.username} ᴀᴅᴀʟᴀʜ ʙᴏᴛ ʏᴀɴɢ ᴅᴀᴘᴀᴛ ᴍᴇᴍʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ ᴅᴇɴɢᴀɴ ᴍᴜᴅᴀʜ.</b>

<b>🚀 ʙᴏᴛ ɪɴɪ ᴅɪᴋᴇᴍʙᴀɴɢᴋᴀɴ ᴏʟᴇʜ <a href=tg://openmessage?user_id={OWNER_ID}>@{OWNER_USERNAME}</a>. ᴊɪᴋᴀ ᴀᴅᴀ ᴋᴇɴᴅᴀʟᴀ, ᴅᴍ ᴏᴡɴᴇʀ ʙᴏᴛ ᴅɪ ᴀᴛᴀs.</b>

<b>📝 ᴄᴀʀᴀ sᴇᴡᴀ ᴜsᴇʀʙᴏᴛ:</b>
<b>1. ᴛᴇᴋᴀɴ ᴛᴏᴍʙᴏʟ ʙᴇʟɪ ᴀᴋsᴇs / ᴜsᴇʀʙᴏᴛ ᴅɪ ʙᴀᴡᴀʜ.</b>
<b>2. ᴘɪʟɪʜ ʀᴏʟᴇ ᴀᴋsᴇs ʏᴀɴɢ ɪɴɢɪɴ ᴀɴᴅᴀ ʙᴇʟɪ.</b>
<b>3. ᴛᴇɴᴛᴜᴋᴀɴ ᴅᴜʀᴀsɪ (1 ʙᴜʟᴀɴ ᴀᴛᴀᴜ ᴘᴇʀᴍᴀɴᴇɴ).</b>
<b>4. sᴄᴀɴ ǫʀɪs ʏᴀɴɢ ᴍᴜɴᴄᴜʟ ᴅᴀɴ sᴇʟᴇsᴀɪᴋᴀɴ ᴘᴇᴍʙᴀʏᴀʀᴀɴ.</b>
<b>5. ᴀᴋsᴇs ᴀᴋᴀɴ ᴀᴋᴛɪꜰ ᴏᴛᴏᴍᴀᴛɪs sᴇᴛᴇʟᴀʜ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴛᴇʀᴅᴇᴛᴇᴋsɪ.</b>
<b>6. ᴋʟɪᴋ ʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ ᴅᴀɴ ɪᴋᴜᴛɪ ɪɴsᴛʀᴜᴋsɪɴʏᴀ.</b></blockquote>
"""

    def PILIH_ROLE(message):
        member_b = _rupiah(ROLE_PRICES["member"]["1"])
        member_p = _rupiah(ROLE_PRICES["member"]["0"])
        seles_b = _rupiah(ROLE_PRICES["seles"]["1"])
        seles_p = _rupiah(ROLE_PRICES["seles"]["0"])
        admin_b = _rupiah(ROLE_PRICES["admin"]["1"])
        admin_p = _rupiah(ROLE_PRICES["admin"]["0"])
        return f"""
<blockquote><b>🛒 ᴘɪʟɪʜ ʀᴏʟᴇ ᴀᴋsᴇs</b>

<b>👤 ᴍᴇᴍʙᴇʀ</b>
<b>├ ᴀᴋsᴇs ᴘʀᴇᴍɪᴜᴍ</b>
<b>├ 1 ʙᴜʟᴀɴ: {member_b}</b>
<b>╰ ᴘᴇʀᴍᴀɴᴇɴ: {member_p}</b>

<b>💼 sᴇʟᴇs</b>
<b>├ ᴘʀᴇᴍɪᴜᴍ + sᴇʟʟᴇʀ</b>
<b>├ 1 ʙᴜʟᴀɴ: {seles_b}</b>
<b>╰ ᴘᴇʀᴍᴀɴᴇɴ: {seles_p}</b>

<b>🛡 ᴀᴅᴍɪɴ</b>
<b>├ ᴘʀᴇᴍɪᴜᴍ + sᴇʟʟᴇʀ + ᴀᴅᴍɪɴ</b>
<b>├ 1 ʙᴜʟᴀɴ: {admin_b}</b>
<b>╰ ᴘᴇʀᴍᴀɴᴇɴ: {admin_p}</b>

<b>👇 sɪʟᴀʜᴋᴀɴ ᴘɪʟɪʜ ʀᴏʟᴇ ᴅɪ ʙᴀᴡᴀʜ ɪɴɪ.</b></blockquote>
"""

    def DURASI(role):
        nama = ROLE_LABEL.get(role, role.upper())
        akses = ROLE_AKSES.get(role, "")
        harga_b = _rupiah(ROLE_PRICES.get(role, {}).get("1", 0))
        harga_p = _rupiah(ROLE_PRICES.get(role, {}).get("0", 0))
        return f"""
<blockquote><b>⏳ ᴘɪʟɪʜ ᴅᴜʀᴀsɪ — ʀᴏʟᴇ {nama}</b>

<b>🎁 {akses}</b>

<b>🗓 1 ʙᴜʟᴀɴ: {harga_b}</b>
<b>♾ ᴘᴇʀᴍᴀɴᴇɴ: {harga_p}</b>

<b>👇 ᴘɪʟɪʜ ᴅᴜʀᴀsɪ ᴘᴇɴʏᴇᴡᴀᴀɴ ᴀɴᴅᴀ.</b></blockquote>
"""

    def QRIS(role, durasi, amount, order_id):
        nama = ROLE_LABEL.get(role, role.upper())
        teks_durasi = "1 ʙᴜʟᴀɴ" if durasi == "1" else "ᴘᴇʀᴍᴀɴᴇɴ"
        return f"""
<blockquote><b>💳 sɪʟᴀʜᴋᴀɴ sᴄᴀɴ ǫʀɪs ᴅɪ ᴀᴛᴀs</b>

<b>🏷 ʀᴏʟᴇ: {nama}</b>
<b>⏳ ᴅᴜʀᴀsɪ: {teks_durasi}</b>
<b>💰 ᴛᴏᴛᴀʟ: {_rupiah(amount)}</b>
<b>🧾 ᴏʀᴅᴇʀ ɪᴅ: <code>{order_id}</code></b>

<b>📲 ǫʀɪs ᴍᴇɴᴅᴜᴋᴜɴɢ sᴇᴍᴜᴀ ᴇ-ᴡᴀʟʟᴇᴛ & ᴍᴏʙɪʟᴇ ʙᴀɴᴋɪɴɢ.</b>
<b>✅ ᴀᴋsᴇs ᴀᴋᴀɴ ᴀᴋᴛɪꜰ ᴏᴛᴏᴍᴀᴛɪs sᴇᴛᴇʟᴀʜ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴍᴀsᴜᴋ.</b>
<b>🔄 ᴀɴᴅᴀ ᴊᴜɢᴀ ʙɪsᴀ ᴛᴇᴋᴀɴ ᴄᴇᴋ sᴛᴀᴛᴜs ᴅɪ ʙᴀᴡᴀʜ.</b></blockquote>
"""

    def SUCCESS_ROLE(role, durasi):
        nama = ROLE_LABEL.get(role, role.upper())
        teks_durasi = "1 ʙᴜʟᴀɴ" if durasi == "1" else "ᴘᴇʀᴍᴀɴᴇɴ"
        return f"""
<blockquote><b>✅ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ʙᴇʀʜᴀsɪʟ</b>

<b>🏷 ʀᴏʟᴇ: {nama}</b>
<b>⏳ ᴅᴜʀᴀsɪ: {teks_durasi}</b>

<b>🎉 ᴀᴋsᴇs ᴀɴᴅᴀ ᴛᴇʟᴀʜ ᴅɪᴀᴋᴛɪꜰᴋᴀɴ ᴏᴛᴏᴍᴀᴛɪs.</b>
<b>🤖 sɪʟᴀʜᴋᴀɴ ᴛᴇᴋᴀɴ ᴛᴏᴍʙᴏʟ ᴅɪ ʙᴀᴡᴀʜ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ.</b></blockquote>
"""

    def NOTIFY_ORDER(user, role, durasi, amount, waktu):
        nama = ROLE_LABEL.get(role, role.upper())
        teks_durasi = "1 ʙᴜʟᴀɴ" if durasi == "1" else "ᴘᴇʀᴍᴀɴᴇɴ"
        full_name = f"{user.first_name} {user.last_name or ''}".strip()
        return f"""
<blockquote><b>🔔 ᴏʀᴅᴇʀ ʀᴏʟᴇ ᴜʙᴏᴛ sᴜᴋsᴇs</b>

<b>👤 ʙᴜʏᴇʀ: <a href=tg://user?id={user.id}>{full_name}</a></b>
<b>🆔 ɪᴅ: <code>{user.id}</code></b>
<b>🏷 ʀᴏʟᴇ: {nama}</b>
<b>⏳ ᴅᴜʀᴀsɪ: {teks_durasi}</b>
<b>💰 ɴᴏᴍɪɴᴀʟ: {_rupiah(amount)}</b>
<b>🕒 ᴡᴀᴋᴛᴜ: {waktu} ᴡɪʙ</b></blockquote>

<blockquote><b>📢 @{NOTIFY_CHANNEL}</b></blockquote>
"""

    def NOTIFY_UBOT(account, waktu):
        full_name = f"{account.first_name} {account.last_name or ''}".strip()
        return f"""
<blockquote><b>🤖 ᴜsᴇʀʙᴏᴛ ʙᴀʀᴜ ᴅɪᴀᴋᴛɪꜰᴋᴀɴ</b>

<b>👤 ᴀᴋᴜɴ: <a href=tg://user?id={account.id}>{full_name}</a></b>
<b>🆔 ɪᴅ: <code>{account.id}</code></b>
<b>🕒 ᴡᴀᴋᴛᴜ: {waktu} ᴡɪʙ</b></blockquote>

<blockquote><b>📢 @{NOTIFY_CHANNEL}</b></blockquote>
"""

    def TEXT_PAYMENT(harga, total, bulan):
        return f"""
<blockquote><b>💬 sɪʟᴀʜᴋᴀɴ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ</b>

<b>🎟️ ʜᴀʀɢᴀ ᴘᴇʀʙᴜʟᴀɴ: {harga}.000</b>

<b>💳 ᴍᴇᴛᴏᴅᴇ ᴘᴇᴍʙᴀʏᴀʀᴀɴ:</b>
<b>├ ǫʀɪs ᴀʟʟ ᴘᴀʏᴍᴇɴᴛ</b>
<b>🔖 ᴛᴏᴛᴀʟ ʜᴀʀɢᴀ: ʀᴘ {total}.000</b>
<b>🗓️ ᴛᴏᴛᴀʟ ʙᴜʟᴀɴ: {bulan}</b>

<b>👤 ᴏᴡɴᴇʀ ʙᴏᴛ: <a href=tg://openmessage?user_id={OWNER_ID}>@{OWNER_USERNAME}</a></b>

<b>🛍 ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ ᴋᴏɴꜰɪʀᴍᴀsɪ ᴜɴᴛᴜᴋ ᴍᴇʟᴀɴᴊᴜᴛᴋᴀɴ ᴘᴇᴍʙᴀʏᴀʀᴀɴ.</b></blockquote>
"""

    async def UBOT(count):
        return f"""
<blockquote><b>╭〢 ᴜʙᴏᴛ ʀᴀɴᴢ ᴏꜰꜰᴄ ᴘʀᴇᴍɪᴜᴍ</b> <code>{int(count) + 1}/{len(ubot._ubot)}</code>
<b>├〢 ᴀᴄᴄᴏᴜɴᴛ:</b> <a href=tg://user?id={ubot._ubot[int(count)].me.id}>{ubot._ubot[int(count)].me.first_name} {ubot._ubot[int(count)].me.last_name or ''}</a>
<b>╰〢 ᴜsᴇʀ ɪᴅ:</b> <code>{ubot._ubot[int(count)].me.id}</code></blockquote>
"""

    def DEAK(X):
        return f"""
<blockquote><b>🗑 ᴀᴋᴜɴ ᴅɪɴᴏɴᴀᴋᴛɪꜰᴋᴀɴ</b>
<b>├ ᴀᴋᴜɴ:</b> <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a>
<b>╰ ɪᴅ:</b> <code>{X.me.id}</code></blockquote>
"""

    def POLICY():
        return f"""
<blockquote><b>📌 ᴋᴇᴛᴇɴᴛᴜᴀɴ ʟᴀʏᴀɴᴀɴ</b>

<b>🔒 ᴀᴋsᴇs ᴜsᴇʀʙᴏᴛ ʙᴇʀsɪꜰᴀᴛ ᴘʀɪʙᴀᴅɪ ᴅᴀɴ ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴅɪᴋᴇᴍʙᴀʟɪᴋᴀɴ sᴇᴛᴇʟᴀʜ ᴘᴇᴍʙᴀʏᴀʀᴀɴ.</b>
<b>📢 ᴄʜᴀɴɴᴇʟ ʀᴇsᴍɪ: @{MAIN_CHANNEL}</b>
<b>☎️ ᴊɪᴋᴀ ᴀᴅᴀ ᴋᴇɴᴅᴀʟᴀ, ʜᴜʙᴜɴɢɪ <a href=tg://openmessage?user_id={OWNER_ID}>@{OWNER_USERNAME}</a></b>

<b>👇 ᴛᴇᴋᴀɴ ʟᴀɴᴊᴜᴛᴋᴀɴ ᴜɴᴛᴜᴋ ᴍᴇᴍɪʟɪʜ ʀᴏʟᴇ.</b></blockquote>
"""
