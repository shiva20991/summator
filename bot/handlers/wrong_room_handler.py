from pyrogram import Client
from bot import LOCAL, CONFIG

async def func(client : Client, message):
    if message.chat.type == "private":
        try:
            await message.delete()
        except:
            pass
