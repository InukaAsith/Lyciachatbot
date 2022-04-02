from lycia import LYCIA
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

LYCIA_START = """
Salam, mən Ledy, Ağıllı ChatBotam. Əgər özünüzü tənha hiss edirsinizsə, hər zaman yanıma gəlib mənimlə söhbət edə bilərsiniz!
"""


@LYCIA.on_message(filters.command(["start"], prefixes = "/") & ~filters.edited)
async def info(client, message):
    buttons = [
                [InlineKeyboardButton("Ledy", switch_inline_query_current_chat="lycia "), InlineKeyboardButton("Owner", url = "https://t.me/Tenha055")]
              ]
    await LYCIA.send_message(chat_id = message.chat.id, text = LYCIA_START, reply_markup = InlineKeyboardMarkup(buttons))
