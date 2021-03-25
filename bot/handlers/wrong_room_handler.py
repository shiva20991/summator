from pyrogram import Client
from bot import LOCAL, CONFIG

async def func(client : Client, message):
    if message.chat.type == "private":
        try:
            await message.delete()
        except:
            pass
    else:
        await message.reply_text(
            LOCAL.WRONG_ROOM.format(
                CHAT_ID = message.from_user.id            
            )
        )
