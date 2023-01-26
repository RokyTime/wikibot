from create_bot import dp, bot
import os, hashlib

from aiogram import types
from aiogram.dispatcher import Dispatcher


async def inline_handler(query : types.InlineQuery):
    text = query.query or 'echo'
    link = 'https://ru.wikipedia.org/wiki/'+text
    result_id: str = hashlib.md5(text.encode()).hexdigest()

    articles = [types.InlineQueryResultArticle(
        id=result_id,
        title='Статья из википедии:',
        url=link,
        input_message_content=types.InputTextMessageContent(message_text=link)
    )]
    
    await query.answer(articles, cache_time=1, is_personal=True)




def register_handlers_user(dp : Dispatcher):
    dp.register_inline_handler(inline_handler)
    