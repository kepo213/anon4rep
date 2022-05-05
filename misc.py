import logging
from aiogram import Bot,TOKEN, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import json

TOKEN = 'BOT TOKEN HERE'

# Initialize bot and dispatcher
bot = Bot(TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot,storage=memory_storage)
logging.basicConfig(level=logging.INFO)
