from pyrogram import Client, filters
from bot import COMMAND
from bot.handlers import leech_handler

@Client.on_message(filters.private & ~filters.regex(r'^/'))
async def func(client : Client, message : Message):
    message.text = "/" + COMMAND.LEECH + " " + message.text
    return await leech_handler.func(client, message)
