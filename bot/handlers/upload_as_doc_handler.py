from pyrogram import Client, filters
from bot import LOCAL, STATUS, COMMAND
from pyrogram.types import Message 

@Client.on_message(filters.command(COMMAND.UPLOAD_AS_DOC))
async def func(client : Client):
    STATUS.UPLOAD_AS_DOC = not STATUS.UPLOAD_AS_DOC
    await message.reply_text(LOCAL.UPLOAD_AS_DOC.format(status=STATUS.UPLOAD_AS_DOC))
