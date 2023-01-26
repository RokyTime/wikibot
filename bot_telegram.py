from create_bot import dp

from aiogram.utils import executor
from handlers import user


def on_startup(_):
    print('bot online')


user.register_handlers_user(dp)



executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
