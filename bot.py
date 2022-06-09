import asyncio
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os

from common import register_handlers_common
from utils import register_handlers_main


async def main():
    bot_token = os.getenv("BOT_TOKEN")
    bot = Bot(token=bot_token)
    dp = Dispatcher(bot, storage=MemoryStorage())

    register_handlers_common(dp)
    register_handlers_main(dp)

    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())

