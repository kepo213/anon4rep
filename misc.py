import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import json


memory_storage = MemoryStorage()
bot = Bot(token="5317907528:AAF-S4YcbUNo_XcX6caSDI6GiXnsQcKCY3c", parse_mode='html', disable_web_page_preview=True)
dp = Dispatcher(bot,storage=memory_storage)
logging.basicConfig(level=logging.INFO)
