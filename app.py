import logging

from aiogram import executor

from loader import dp
import middlewares, filters, handlers
from utils.db_api import db_gino
from utils.db_api.db_gino import db
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Уведомляет про запуск
    print("Подключаем БД")
    await db_gino.on_startup(dp)
    print("Готово")

    print("Чистим базу")
    await db.gino.drop_all()

    print("Готово")

    print("Создаем таблицы")
    await db.gino.create_all()

    print("Готово")
    await on_startup_notify(dp)
    await set_default_commands(dp)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)