import os
from urllib.parse import unquote, urlparse
import re
import traceback
import sys
import random
import aiohttp
import requests
import traceback
from lycia import LYCIA
from datetime import datetime
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputTextMessageContent,
    InlineQueryResultArticle,
    InlineQueryResultPhoto,
    CallbackQuery,
    InlineQuery,
    InlineQueryResultAnimation,
)   
from pykeyboard import InlineKeyboard

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            try:
                data = await resp.json()
            except Exception:
                data = await resp.text()
    return data


@LYCIA.on_inline_query()
async def inline_query_handler(client, query):
    string = query.query.lower()

    answers = []
    if string.split()[0] == "lycia":
            if len(string.split()) < 2:
                await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text='Ledy | Chat [text]',
                    switch_pm_parameter='lycia',
                )
                return
            lycia = string.split(None, 1)[1].strip()
            Lycia = await lyciachatbot(answers, lycia)
            await client.answer_inline_query(
                query.id,
                results=Lycia,
                cache_time=2
            )
   

async def lyciachatbot(answers, text):
    URL = f"https://api.affiliateplus.xyz/api/chatbot?message={text}&botname=@Lyciachatbot&ownername=@madepranav"
    result = await fetch(URL)
    buttons = InlineKeyboard(row_width=1)
    buttons.add(InlineKeyboardButton(
        "Lycia",
        switch_inline_query_current_chat="lycia"
    ))
    caption = f"""
**You:** `{text}`
**Ledy:** `{result['message']}`"""
    answers.append(
        InlineQueryResultPhoto(
            photo_url="https://telegra.ph/file/4fd47f6ab742a28b5e57c.jpg",
            caption=caption,
            reply_markup=buttons
        ))
    return answers
