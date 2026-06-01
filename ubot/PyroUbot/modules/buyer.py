import asyncio
from PyroUbot import *

__MODULE__ = "ᴛʜᴀɴᴋs"

__HELP__ = """
<blockquote><b>✨ ANIMASI TERIMA KASIH BUYER</b>

<code>{0}thanks
<code>{0}tq</code>
<code>{0}nx</code>
➥ Reply ke user ATAU sertakan user_id / username
➥ Bot akan menampilkan animasi ucapan terima kasih</blockquote>
"""

@PY.UBOT("thanks")
async def thanks_buyer(client, message):
    msg = await message.reply("✨")

    frames = [
        "✨",
        "✨ T",
        "✨ Te",
        "✨ Ter",
        "✨ Teri",
        "✨ Terim",
        "✨ Terima",
        "✨ Terima k",
        "✨ Terima ka",
        "✨ Terima kas",
        "✨ Terima kasi",
        "✨ Terima kasih",
        "✨ Terima kasih 🙏",
        "✨ Terima kasih 🙏\n💖",
        "✨ Terima kasih 🙏\n💖 Sudah membeli UBot",
        "✨ Terima kasih 🙏\n💖 Sudah membeli UBot kami",
        "✨ Terima kasih 🙏\n💖 Sudah membeli UBot kami",
        "✨ Terima kasih 🙏\n💖 Sudah membeli UBot kami",
        "✨ Terima kasih 🙏\n💖 Semoga bermanfaat",
        "✨ Terima kasih 🙏\n💖 Semoga bermanfaat\n🚀 Selamat menggunakan!"
    ]

    last = None
    for text in frames:
        if text != last:
            try:
                await msg.edit(text)
            except Exception:
                pass
            last = text
        await asyncio.sleep(0.5)
        
@PY.UBOT("tq")
async def thanks_buyer(client, message):
    msg = await message.reply("✨")

    frames = [
        "✨",
        "✨ T",
        "✨ Te",
        "✨ Ter",
        "✨ Teri",
        "✨ Terim",
        "✨ Terima",
        "✨ Terima k",
        "✨ Terima ka",
        "✨ Terima kas",
        "✨ Terima kasi",
        "✨ Terima kasih",
        "✨ Terima kasih 🙏",
        "✨ Terima kasih 🙏\n💖",
        "✨ Terima kasih 🙏\n💖 Sudah berbelanja",
        "✨ Terima kasih 🙏\n💖 Sudah berbelanja di kami",
        "✨ Terima kasih 🙏\n💖 Sudah berbelanja di kami",
        "✨ Terima kasih 🙏\n💖 Sudah berbelanja di kami",
        "✨ Terima kasih 🙏\n💖 Semoga bermanfaat",
        "✨ Terima kasih 🙏\n💖 Semoga bermanfaat\n🚀 Selamat menggunakan!"
    ]

    last = None
    for text in frames:
        if text != last:
            try:
                await msg.edit(text)
            except Exception:
                pass
            last = text
        await asyncio.sleep(0.5)
        
@PY.UBOT("nx")
async def thanks_buyer(client, message):
    msg = await message.reply("✨")

    frames = [
        "✨",
        "✨ R",
        "✨ Ra",
        "✨ Ran",
        "✨ Ranz",
        "✨ Ranz O",
        "✨ Ranz Of",
        "✨ Ranz Off",
        "✨ Ranz Offc",
        "✨ Ranz Offc U",
        "✨ Ranz Offc Ub",
        "✨ Ranz Offc Ubo",
        "✨ Ranz Offc Ubot",
        "✨ Ranz Offc Ubot 🔫",
        "✨ Ranz Offc Ubot 🔫\nKita tampil bentar",
        "✨ Ranz Offc Ubot 🔫\nKita tampil bentar",
        "✨ Ranz Offc Ubot 🔫\nKita tampil bentar",
        "✨ Ranz Offc Ubot 🔫\nKita tampil bentar",
        "✨ Ranz Offc Ubot 🙏\n💖 Izin bang",
        "✨ Ranz Offc Ubot 🙏\n💖 Izin bang\n🚀 Izin tampil dikit 🙏"
    ]

    last = None
    for text in frames:
        if text != last:
            try:
                await msg.edit(text)
            except Exception:
                pass
            last = text
        await asyncio.sleep(0.5)