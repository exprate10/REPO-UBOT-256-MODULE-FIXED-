import requests
import os
from PyroUbot import *
from pyrogram.types import Message

__MODULE__ = "ʀᴇᴍɪɴɪ"
__HELP__ = """
<blockquote><b>ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʜᴅ</b></blockquote>

<blockquote><b>ᴘᴇʀɪɴᴛᴀʜ : <code>{0}ʀᴇᴍɪɴɪ</code> ᴀᴛᴀᴜ <code>{0}ʜᴅ</code>
    ᴜɴᴛᴜᴋ ᴍᴇɴᴊᴇʀɴɪʜᴋᴀɴ ɢᴀᴍʙᴀʀ (ғᴜʟʟ ᴘʀᴇᴍɪᴜᴍ)</b></blockquote>
"""

@PY.UBOT("remini|hd")
@PY.TOP_CMD
async def process_image(client, message):
    if not message.reply_to_message or not message.reply_to_message.photo:
        return await message.reply("<blockquote><b>ʀᴇᴘʟʏ ɢᴀᴍʙᴀʀ ʏᴀɴɢ ᴍᴀᴜ ᴅɪ ʜᴅ ɪɴ ᴋɪɴɢ</b></blockquote>")

    msg = await message.reply("<blockquote><b>sᴇᴅᴀɴɢ ᴅɪᴘʀᴏsᴇs ᴍᴇɴᴊᴀᴅɪ ʜᴅ, ᴍᴏʜᴏɴ ᴛᴜɴɢɢᴜ...</b></blockquote>")

    file_path = None
    try:
        file_path = await message.reply_to_message.download()
        
        api_key = "@31Moire_mor"
        api_url = f"https://api.botcahx.eu.org/api/maker/remini?apikey={api_key}"
        
        with open(file_path, "rb") as img_file:
            files = {"file": img_file}
            response = requests.post(api_url, files=files)

        if response.status_code == 200:
            res_data = response.json()
            
            if res_data.get("status") is True:
                image_hd_url = res_data.get("result")
                
                await client.send_photo(
                    chat_id=message.chat.id,
                    photo=image_hd_url,
                    caption="<blockquote><b>sᴜᴅᴀʜ ᴊᴀᴅɪ ʜᴅ ᴋɪɴɢ, sɪʟᴀʜᴋᴀɴ ᴅɪ ᴄᴇᴋ</b></blockquote>",
                    reply_to_message_id=message.id
                )
                await msg.delete()
            else:
                await msg.edit("<blockquote><b>ɢᴀɢᴀʟ ᴍᴇᴍᴘʀᴏsᴇs ɢᴀᴍʙᴀʀ, ᴍᴜɴɢᴋɪɴ ʟɪᴍɪᴛ ᴀᴘɪ ʜᴀʙɪs</b></blockquote>")
        else:
            await msg.edit(f"<blockquote><b>sᴇʀᴠᴇʀ ᴀᴘɪ ᴇʀᴏʀ: {response.status_code}</b></blockquote>")

    except Exception as e:
        await msg.edit(f"<blockquote><b>ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ ᴋɪɴɢ:</b></blockquote>\n<code>{str(e)}</code>")
    
    finally:
        if file_path and os.path.exists(file_path):
            os.remove(file_path)

