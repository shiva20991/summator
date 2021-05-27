from pyrogram import Client
from bot import LOCAL, CONFIG
from pyrogram.types import Message 

async def func(client : Client, message):
    if message.chat.type == "private":
        try:
            await message.delete()
        except:
            pass
