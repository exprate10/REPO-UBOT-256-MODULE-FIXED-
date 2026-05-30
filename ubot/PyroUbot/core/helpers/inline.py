import re
from pykeyboard import InlineKeyboard
from pyrogram.errors import MessageNotModified
from pyrogram.types import *
from pyromod.helpers import ikb
from pyrogram.types import (InlineKeyboardButton, InlineQueryResultArticle,
                            InputTextMessageContent)

from PyroUbot import *

def detect_url_links(text):
    link_pattern = (
        r"(?:https?://)?(?:www\.)?[a-zA-Z0-9.-]+(?:\.[a-zA-Z]{2,})+(?:[/?]\S+)?"
    )
    link_found = re.findall(link_pattern, text)
    return link_found


def detect_button_and_text(text):
    button_matches = re.findall(r"\| ([^|]+) - ([^|]+) \|", text)
    text_matches = (
        re.search(r"(.*?) \|", text, re.DOTALL).group(1) if "|" in text else text
    )
    return button_matches, text_matches


def create_inline_keyboard(text, user_id=False, is_back=False):
    keyboard = []
    button_matches, text_matches = detect_button_and_text(text)

    prev_button_data = None
    for button_text, button_data in button_matches:
        data = (
            button_data.split("#")[0]
            if detect_url_links(button_data.split("#")[0])
            else f"_gtnote {int(user_id.split('_')[0])}_{user_id.split('_')[1]} {button_data.split('#')[0]}"
        )
        cb_data = data if user_id else button_data.split("#")[0]
        if "#" in button_data:
            if prev_button_data:
                if detect_url_links(cb_data):
                    keyboard[-1].append(InlineKeyboardButton(button_text, url=cb_data))
                else:
                    keyboard[-1].append(
                        InlineKeyboardButton(button_text, callback_data=cb_data)
                    )
            else:
                if detect_url_links(cb_data):
                    button_row = [InlineKeyboardButton(button_text, url=cb_data)]
                else:
                    button_row = [
                        InlineKeyboardButton(button_text, callback_data=cb_data)
                    ]
                keyboard.append(button_row)
        else:
            if button_data.startswith("http"):
                button_row = [InlineKeyboardButton(button_text, url=cb_data)]
            else:
                button_row = [InlineKeyboardButton(button_text, callback_data=cb_data)]
            keyboard.append(button_row)

        prev_button_data = button_data

    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)

    if user_id and is_back:
        markup.inline_keyboard.append(
            [
                InlineKeyboardButton(
                    "ᴋᴇᴍʙᴀʟɪ",
                    f"_gtnote {int(user_id.split('_')[0])}_{user_id.split('_')[1]}",
                )
            ]
        )

    return markup, text_matches


class BTN:
    def ALIVE(get_id):
        button = [
            [
                InlineKeyboardButton(
                    text="ᴛᴜᴛᴜᴘ",
                    callback_data=f"alv_cls {int(get_id[1])} {int(get_id[2])}",
                )
            ],
            [
                InlineKeyboardButton(
                    text="ʜᴇʟᴘ",
                    callback_data="help_back",
                )
            ]
        ]
        return button
        
    def PROMODEK(message):
        button = [
            [InlineKeyboardButton("✅ sᴇᴛᴜᴊᴜ & ʟᴀɴᴊᴜᴛᴋᴀɴ", callback_data="bahan")],
        ]
        return button

    def BOT_HELP(message):
        button = [
            [InlineKeyboardButton("ʀᴇsᴛᴀʀᴛ", callback_data="reboot")],
            [InlineKeyboardButton("sʏsᴛᴇᴍ", callback_data="system")],
            [InlineKeyboardButton("ᴜʙᴏᴛ", callback_data="ubot")],
            [InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ", callback_data="update")],
        ]
        return button

    def START(message):
        user_id = message.from_user.id
        if not user_id == OWNER_ID:
            button = [
                [InlineKeyboardButton("⦪ ʙᴇʟɪ ᴀᴋsᴇs / ᴜsᴇʀʙᴏᴛ ⦫", callback_data="bahan")],
                [InlineKeyboardButton("✭ ᴄʜᴀɴɴᴇʟ ᴛᴇsᴛɪᴍᴏɴɪ ✭", url="https://t.me/AllTestiRanzOffc")],
                [
                    InlineKeyboardButton("⦪ ʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ ⳼", callback_data="buat_ubot"),
                    InlineKeyboardButton("⦪ ʜᴇʟᴘ ᴍᴇɴᴜ ⦫", callback_data="help_back")
                ],
                [InlineKeyboardButton("⦪ sᴜᴘᴘᴏʀᴛ ⦫", callback_data="support")]
            ]
        else:
            button = [
                [InlineKeyboardButton("⦪ ʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ ⦫", callback_data="bahan")],
                [
                    InlineKeyboardButton("⦪ ɢɪᴛᴘᴜʟʟ ⦫", callback_data="cb_gitpull"),
                    InlineKeyboardButton("⦪ ʀᴇsᴛᴀʀᴛ ⦫", callback_data="cb_restart")
                ],
                [
                    InlineKeyboardButton("⦪ ʟɪsᴛ ᴜsᴇʀʙᴏᴛ ⦫", callback_data="cek_ubot")
                ]
            ]
        return button

    def ADD_EXP(user_id):
        buttons = InlineKeyboard(row_width=3)
        keyboard = []
        for X in range(1, 13):
            keyboard.append(
                InlineKeyboardButton(
                    f"{X} ʙᴜʟᴀɴ",
                    callback_data=f"success {user_id} member {X}",
                )
            )
        buttons.add(*keyboard)
        buttons.row(
            InlineKeyboardButton(
                "⦪ ᴅᴀᴘᴀᴛᴋᴀɴ ᴘʀᴏғɪʟ ⦫", callback_data=f"profil {user_id}"
            )
        )
        buttons.row(
            InlineKeyboardButton(
                "⦪ ᴛᴏʟᴀᴋ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ⦫", callback_data=f"failed {user_id}"
            )
        )
        return buttons

    def EXP_UBOT():
        button = [
            [InlineKeyboardButton("⦪ ʙᴇʟɪ ᴜsᴇʀʙᴏᴛ ⦫", callback_data="bahan")],
        ]
        return button

    def UBOT(user_id, count):
        button = [
            [
                InlineKeyboardButton(
                    "⦪ ʜᴀᴘᴜs ᴅᴀʀɪ ᴅᴀᴛᴀʙᴀsᴇ ⦫",
                    callback_data=f"del_ubot {int(user_id)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "⦪ ᴄᴇᴋ ᴍᴀsᴀ ᴀᴋᴛɪғ ⦫",
                    callback_data=f"cek_masa_aktif {int(user_id)}",
                )
            ],
            [
                InlineKeyboardButton("⟢ sᴇʙᴇʟᴜᴍɴʏᴀ", callback_data=f"p_ub {int(count)}"),
                InlineKeyboardButton("sᴇʟᴀɴᴊᴜ𝗧ɴʏᴀ ⟣", callback_data=f"n_ub {int(count)}"),
            ],
        ]
        return button
    
    def DEAK(user_id, count):
        button = [
            [
                InlineKeyboardButton(
                    "⦪ ᴋᴇᴍʙᴀʟɪ ⦫",
                    callback_data=f"p_ub {int(count)}"
                ),
                InlineKeyboardButton(
                    "⦪ sᴇᴛᴜᴊᴜɪ ⦫", callback_data=f"deak_akun {int(count)}",
                ),
            ],
        ]
        return button

    def ROLE_SELECT(user_id):
        button = [
            [InlineKeyboardButton("👤 ᴍᴇᴍʙᴇʀ", callback_data=f"rolepilih member {int(user_id)}")],
            [InlineKeyboardButton("💼 sᴇʟᴇs", callback_data=f"rolepilih seles {int(user_id)}")],
            [InlineKeyboardButton("🛡 ᴀᴅᴍɪɴ", callback_data=f"rolepilih admin {int(user_id)}")],
            [InlineKeyboardButton("🔙 ᴋᴇᴍʙᴀʟɪ", callback_data=f"home {int(user_id)}")],
        ]
        return button

    def ROLE_DURASI(role, user_id):
        button = [
            [InlineKeyboardButton("🗓 1 ʙᴜʟᴀɴ", callback_data=f"roledur {role} 1 {int(user_id)}")],
            [InlineKeyboardButton("♾ ᴘᴇʀᴍᴀɴᴇɴ", callback_data=f"roledur {role} 0 {int(user_id)}")],
            [InlineKeyboardButton("🔙 ᴋᴇᴍʙᴀʟɪ", callback_data=f"belirole {int(user_id)}")],
        ]
        return button

    def QRIS_CHECK(order_id, amount, role, durasi, user_id):
        button = [
            [InlineKeyboardButton("🔄 ᴄᴇᴋ sᴛᴀᴛᴜs ᴘᴇᴍʙᴀʏᴀʀᴀɴ", callback_data=f"rolecek {order_id} {int(amount)} {role} {durasi}")],
            [InlineKeyboardButton("🔙 ʙᴀᴛᴀʟ", callback_data=f"cancelqris {int(user_id)}")],
        ]
        return button

    def SUCCESS_UBOT():
        button = [
            [InlineKeyboardButton("🤖 ʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ", callback_data="buat_ubot")],
        ]
        return button


async def smart_edit(callback_query, text, reply_markup=None, disable_web_page_preview=True):
    pesan = callback_query.message
    is_media = bool(
        getattr(pesan, "photo", None)
        or getattr(pesan, "video", None)
        or getattr(pesan, "document", None)
        or getattr(pesan, "animation", None)
    )
    try:
        if is_media:
            return await pesan.edit_caption(caption=text, reply_markup=reply_markup)
        return await pesan.edit_text(
            text,
            reply_markup=reply_markup,
            disable_web_page_preview=disable_web_page_preview,
        )
    except MessageNotModified:
        return None
    except Exception:
        try:
            await pesan.delete()
        except Exception:
            pass
        return await bot.send_message(
            callback_query.from_user.id,
            text,
            reply_markup=reply_markup,
            disable_web_page_preview=disable_web_page_preview,
        )
        

