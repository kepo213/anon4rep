import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import json


API_TOKEN = "5317907528:AAF-S4YcbUNo_XcX6caSDI6GiXnsQcKCY3c"


bot = Bot(token=API_TOKEN)

logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
