import asyncio

from pyrogram.enums import UserStatus

from PyroUbot import *

__MODULE__ = "ɪɴᴠɪᴛᴇ"
__HELP__ = """
<blockquote>Bantuan Untuk Invite

perintah : <code>{0}invite</code> [username]
    mengundang anggota ke group</blockquote>
"""


@PY.UBOT("invite")
@PY.TOP_CMD
@PY.GROUP
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ktrng = await EMO.BL_KETERANGAN(client)
    mg = await message.reply(f"{prs}menambahkan pengguna!")
    if len(message.command) < 2:
        return await mg.delete()
    user_s_to_add = message.text.split(" ", 1)[1]
    if not user_s_to_add:
        await mg.edit(
            f"{ktrng}beri saya pengguna untuk ditambahkan!\nperiksa menu bantuan untuk info lebih lanjut!"
        )
        return
    user_list = user_s_to_add.split(" ")
    try:
        await client.add_chat_members(message.chat.id, user_list, forward_limit=100)
    except Exception as e:
        return await mg.edit(f"{e}")
    await mg.edit(f"{brhsl}berhasil ditambahkan {len(user_list)} ke grup ini")







