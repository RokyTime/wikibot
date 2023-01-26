from aiogram.dispatcher import Dispatcher
from aiogram import Bot

import config


bot = Bot(config.TOKEN)
dp = Dispatcher(bot)