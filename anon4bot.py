from aiogram import executor
from misc import dp
import handlers
from aiogram.types import InlineQuery, \
    InputTextMessageContent, InlineQueryResultArticle

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
