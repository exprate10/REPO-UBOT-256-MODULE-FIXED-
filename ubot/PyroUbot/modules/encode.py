import os
import subprocess
from pyrogram import Client, filters
from PyroUbot import PY
import shutil
from pyrogram.types import Message

__MODULE__ = "ᴇɴᴄʀʏᴘᴛ ʜᴀʀᴅ"
__HELP__ = """
<blockquote><b>Bantuan Untuk Encrypt JS</b>

Perintah:
<code>{0}enc</code> → Balas file .js untuk dienkripsi.

Sumber: Menggunakan UglifyJS untuk enkripsi JavaScript.</blockquote></b>
"""

if not shutil.which("uglifyjs"):
    raise Exception("⚠️ UglifyJS belum terinstal. Install dengan `npm install -g uglify-js`")

@PY.UBOT("enc")
@PY.TOP_CMD
async def encrypt_js(client: Client, message: Message):
    if not message.reply_to_message or not message.reply_to_message.document:
        return await message.reply("😠 Silakan balas file .js untuk dienkripsi.")

    file_info = message.reply_to_message.document
    file_name = file_info.file_name

    if not file_name.endswith('.js'):
        return await message.reply("❌ File harus berekstensi .js!")

    msg = await message.reply("⚡ Mengunduh file...")
    file_path = await client.download_media(message.reply_to_message.document)

    await msg.edit("⚡ Memproses encrypt hard code...")

    encrypted_file_path = f"./encrypted_{file_name}"

    try:
        subprocess.run(["uglifyjs", file_path, "-o", encrypted_file_path, "-c", "-m"], check=True)

        await message.reply_document(
            encrypted_file_path,
            caption="✅ **File berhasil dienkripsi!**\n🔒 @kingprem_bot"
        )

    except subprocess.CalledProcessError:
        await msg.edit("❌ Gagal mengenkripsi file!")

    os.remove(file_path)
    os.remove(encrypted_file_path)
