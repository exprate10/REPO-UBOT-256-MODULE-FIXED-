import random
import re
import os
import platform
import subprocess
import sys
import traceback
from datetime import datetime
from io import BytesIO, StringIO
from PyroUbot.config import OWNER_ID
import psutil
from PyroUbot import *
from datetime import datetime
from time import time
from pyrogram.types import (
    InlineQueryResultPhoto,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    InlineQueryResultArticle,
    InputTextMessageContent
)
from pyrogram import Client
from pyrogram.raw.functions import Ping

from pyrogram.types import *

from PyroUbot import *

@PY.BOT("joinreseller")
async def _(client, message):
    buttons = BTN.PROMODEK(message)
    sh = await message.reply("""<u><b>🏷 Join Reseller: 15.000 </b></u>
<blockquote><b>⚠️ Rules Reseller!!</b>
<b>  -  Bertanggung Jawab Penuh.</b>
<b>  -  Tidak Melakukan Penipuan/Scam.</b>
<b>  -  Memiliki Bank/E-Wallet Untuk Melakukan Transaksi.</b>
<b>  -  Tidak Membagikan Akses Userbot Secara Gratis</b>

<b>📚 Keuntungan Reseller:</b>
<b>  -  Memliki Basic Dasar Untuk Berjualan.</b>
<b>  -  Membeli Paket Reseller, Anda Memiliki Akses Reseller Selamanya.</b>
<b>  -  Diperbolehkan Untuk Menjual Layanan Userbot Kepada Customer.</b>
<b> - Bebas Add/Crate Userbot Tanpa Ada Batasan.</b>
<b>  -  Tidak Ada Reffund Setelah Melakukan Pembayaran.</b></blockquote>
<b>✨ Jika Anda Sudah Setuju Dan Ingin Menjadi Reseller Silahkan Klik Tombol Di Bawah Ini.</b>""", reply_markup=InlineKeyboardMarkup(buttons))



@PY.UBOT("alive")
@PY.TOP_CMD
async def _(client, message):
    try:
        x = await client.get_inline_bot_results(
            bot.me.username, f"alive {message.id} {client.me.id}"
        )
        await message.reply_inline_bot_result(x.query_id, x.results[0].id, quote=True)
    except Exception as error:
        await message.reply(error)



@PY.INLINE("^alive")
async def _(client, inline_query):

    try:

        psr = await EMO.PASIR(client)

        get_id = inline_query.query.split()

        for my in ubot._ubot:

            if int(get_id[2]) == my.me.id:

                try:
                    peer = my._get_my_peer[my.me.id]
                    users = len(peer["pm"])
                    group = len(peer["gc"])
                except Exception:
                    users = random.randrange(await my.get_dialogs_count())
                    group = random.randrange(await my.get_dialogs_count())


                get_exp = await get_expired_date(my.me.id)

                exp = get_exp.strftime("%d-%m-%Y") if get_exp else "None"


                if my.me.id in await get_list_from_vars(client.me.id, "ULTRA_PREM"):

                    status = "SuperUltra"

                else:

                    status = "Premium"


                button = BTN.ALIVE(get_id)


                start = datetime.now()

                await my.invoke(Ping(ping_id=0))

                ping = (datetime.now() - start).microseconds / 1000


                uptime = await get_time((time() - start_time))


                msg = f"""
<blockquote>{bot.me.mention}
    status: {status} 
       {psr} expired_on: {exp} 
        dc_id: {my.me.dc_id}
        ping_dc: {ping} ms
        peer_users: {users} users
        peer_group: {group} group
        start_uptime: {uptime}</blockquote>
        <blockquote><b>ᴜʙᴏᴛ ʀᴀɴᴢ ᴏꜰꜰᴄ ᴘᴇᴅɪᴀ</b></blockquote>
"""


                await client.answer_inline_query(

                    inline_query.id,

                    cache_time=1,

                    results=[

                        InlineQueryResultArticle(

                            title="💬",

                            reply_markup=
                            InlineKeyboardMarkup(button),

                            input_message_content=
                            InputTextMessageContent(msg),

                        )

                    ],

                )

    except:
        pass



@PY.CALLBACK("alv_cls")
async def _(client, callback_query):

    try:

        get_id = callback_query.data.split()

        if not callback_query.from_user.id == int(get_id[2]):
            return


        unPacked = unpackInlineMessage(callback_query.inline_message_id)


        for my in ubot._ubot:

            if callback_query.from_user.id == int(my.me.id):

                await my.delete_messages(

                    unPacked.chat_id,

                    [int(get_id[1]), unPacked.message_id]

                )

    except:
        pass




@PY.BOT("anu")
@PY.ADMIN
async def _(client, message):
    buttons = BTN.BOT_HELP(message)
    sh = await message.reply("help menu information", reply_markup=InlineKeyboardMarkup(buttons))
    

@PY.CALLBACK("balik")
async def _(client, callback_query):
    buttons = BTN.BOT_HELP(callback_query)
    sh = await callback_query.message.edit("help menu information", reply_markup=InlineKeyboardMarkup(buttons))



@PY.CALLBACK("reboot")
async def _(client, callback_query):

    user_id = callback_query.from_user.id

    if user_id not in await get_list_from_vars(client.me.id, "ADMIN_USERS"):
        return await callback_query.answer("tombol ini bukan untuk lu", True)

    await callback_query.answer("system berhasil di restart", True)

    subprocess.call(["bash", "start.sh"])



@PY.CALLBACK("update")
async def _(client, callback_query):

    user_id = callback_query.from_user.id

    if not user_id == OWNER_ID:
        return await callback_query.answer("tombol ini bukan untuk lu", True)

    out = subprocess.check_output(["git", "pull"]).decode("UTF-8")

    if "Already up to date." in str(out):
        return await callback_query.answer("ꜱudah terupdate", True)

    else:
        await callback_query.answer("ꜱedang memproꜱeꜱ update.....", True)


    os.execl(

        sys.executable,

        sys.executable,

        "-m",

        "PyroUbot"

    )



@PY.UBOT("help")
async def user_help(client, message):

    if not get_arg(message):

        try:

            x = await client.get_inline_bot_results(bot.me.username, "user_help")

            await message.reply_inline_bot_result(x.query_id, x.results[0].id)

        except Exception as error:

            await message.reply(error)

    else:

        module = (get_arg(message))

        if get_arg(message) in HELP_COMMANDS:

            prefix = await ubot.get_prefix(client.me.id)

            await message.reply(

                HELP_COMMANDS[get_arg(message)].__HELP__.format(

                    next((p) for p in prefix)

                ),

                quote=True,

            )

        else:

            await message.reply(

                f"<b>❌ ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴍᴏᴅᴜʟᴇ ᴅɪ ᴅᴀᴛᴀʙsᴇ<code>{module}</code></b>"

            )



@PY.INLINE("^user_help")
async def user_help_inline(client, inline_query):

    try:

        SH = await ubot.get_prefix(inline_query.from_user.id)

        caption = (
            f"<blockquote><b>"
            f"✣ ᴍᴇɴᴜ ɪɴʟɪɴᴇ "
            f"<a href=tg://user?id={inline_query.from_user.id}>"
            f"{inline_query.from_user.first_name} {inline_query.from_user.last_name or ''}</a>\n"
            f"ᴛᴏᴛᴀʟ ᴍᴏᴅᴜʟᴇs: {len(HELP_COMMANDS)}\n"
            f"ᴘʀᴇꜰɪx: {' '.join(SH)}\n"
            f"ᴍʏ ᴜʙᴏᴛ: <a href=t.me/{bot.me.username}>{bot.me.username}</a>"
            f"</b></blockquote>"
        )


        results = [

            InlineQueryResultPhoto(

                photo_url="https://files.catbox.moe/pgaypk.jpg",

                thumb_url="https://files.catbox.moe/pgaypk.jpg",

                caption=caption,

                reply_markup=InlineKeyboardMarkup(

                    paginate_modules(0, HELP_COMMANDS, "help")

                ),

            )

        ]


        await client.answer_inline_query(

            inline_query.id,

            cache_time=1,

            results=results,

        )

    except:
        pass

@bot.on_callback_query(filters.regex(r"^help_"))
async def help_callback(client, callback_query):
    data = callback_query.data

    def menu_caption():
        return (
            f"<blockquote><b>"
            f"✣ ᴍᴇɴᴜ ɪɴʟɪɴᴇ "
            f"<a href=tg://user?id={callback_query.from_user.id}>"
            f"{callback_query.from_user.first_name} {callback_query.from_user.last_name or ''}</a>\n"
            f"ᴛᴏᴛᴀʟ ᴍᴏᴅᴜʟᴇs: {len(HELP_COMMANDS)}\n"
            f"ᴍʏ ᴜʙᴏᴛ: <a href=t.me/{bot.me.username}>{bot.me.username}</a>"
            f"</b></blockquote>"
        )

    nav = re.match(r"^help_(prev|next)\((\d+)\)$", data)
    if nav:
        page = int(nav.group(2))
        page = page + 1 if nav.group(1) == "next" else page - 1
        try:
            return await callback_query.edit_message_reply_markup(
                reply_markup=InlineKeyboardMarkup(paginate_modules(page, HELP_COMMANDS, "help"))
            )
        except Exception:
            return await callback_query.answer()

    if data == "help_back":
        try:
            return await callback_query.edit_message_caption(
                caption=menu_caption(),
                reply_markup=InlineKeyboardMarkup(paginate_modules(0, HELP_COMMANDS, "help")),
            )
        except Exception:
            return await callback_query.edit_message_reply_markup(
                reply_markup=InlineKeyboardMarkup(paginate_modules(0, HELP_COMMANDS, "help"))
            )

    mod = re.match(r"^help_module\((.+)\)$", data)
    if mod:
        mod_name = mod.group(1)
        if mod_name in HELP_COMMANDS:
            prefix = await ubot.get_prefix(callback_query.from_user.id)
            help_doc = getattr(HELP_COMMANDS[mod_name], "__HELP__", None)
            if not help_doc:
                return await callback_query.answer("❌ ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴅᴇsᴋʀɪᴘsɪ ᴜɴᴛᴜᴋ ᴍᴏᴅᴜʟ ɪɴɪ", True)
            help_text = help_doc.format(next((p) for p in prefix))
            button = [[InlineKeyboardButton("🔙 ᴋᴇᴍʙᴀʟɪ", callback_data="help_back")]]
            return await callback_query.edit_message_caption(
                caption=f"<blockquote><b>{help_text}</b></blockquote>",
                reply_markup=InlineKeyboardMarkup(button),
            )
        return await callback_query.answer("❌ ᴍᴏᴅᴜʟ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ", True)

    return await callback_query.answer()

@PY.CALLBACK("^close_user")
async def close_usernya(client, callback_query):
    try:
        unPacked = unpackInlineMessage(callback_query.inline_message_id)
        for x in ubot._ubot:
            if callback_query.from_user.id == int(x.me.id):
                await x.delete_messages(unPacked.chat_id, unPacked.message_id)
    except:
        pass
        