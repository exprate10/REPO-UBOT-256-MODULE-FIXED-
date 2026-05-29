import asyncio
import os
import sys
import signal
import tornado.ioloop
import tornado.platform.asyncio
from pyrogram import Client, filters
from PyroUbot import *

@bot.on_message(filters.command("restart"))
async def restart_bot_utama(client, message):
    pengirim_name = message.from_user.first_name
    pengirim_id = message.from_user.id

    status = await message.reply("<b>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ</b>")
    
    await asyncio.sleep(2)
    
    await status.edit(
        f"<b>ʀᴇsᴛᴀʀᴛ ʙᴇʀʜᴀsɪʟ ᴅɪʟᴀᴋᴜᴋᴀɴ !</b>\n\n"
        f"<b>ɴᴀᴍᴇ:</b> {pengirim_name} | <code>{pengirim_id}</code>"
    )
    
    os.execl(sys.executable, sys.executable, "-m", "PyroUbot")

async def shutdown(signal, loop):
    print(f"Received exit signal {signal.name}...")
    tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]
    [task.cancel() for task in tasks]
    print("Cancelling outstanding tasks")
    await asyncio.gather(*tasks, return_exceptions=True)
    loop.stop()

async def main():
    await bot.start()
    for _ubot in await get_userbots():
        ubot_ = Ubot(**_ubot)
        try:
            await asyncio.wait_for(ubot_.start(), timeout=10)
        except asyncio.TimeoutError:
            await remove_ubot(int(_ubot["name"]))
            print(f"[ɪɴғᴏ]: {int(_ubot['name'])} ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇʀᴇsᴘᴏɴ")
        except Exception:
            await remove_ubot(int(_ubot["name"]))
            print(f"[ɪɴғᴏ]: {int(_ubot['name'])} ʙᴇʀʜᴀsɪʟ ᴅɪ ʜᴀᴘᴜs")
    
    await bash("rm -rf *session*")
    
    await asyncio.gather(loadPlugins(), installPeer(), expiredUserbots())
    
    stop_event = asyncio.Event()
    loop = asyncio.get_running_loop()
    for s in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(
            s, lambda: asyncio.create_task(shutdown(s, loop))
        )

    try:
        await stop_event.wait()
    except asyncio.CancelledError:
        pass
    finally:
        await bot.stop()

if __name__ == "__main__":
    tornado.platform.asyncio.AsyncIOMainLoop().install()
    loop = tornado.ioloop.IOLoop.current().asyncio_loop
    loop.run_until_complete(main())
    