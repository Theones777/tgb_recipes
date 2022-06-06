from aiogram import Bot, Dispatcher, executor, types
import os

bot_token = os.getenv("BOT_TOKEN")
bot = Bot(token=bot_token)
dp = Dispatcher(bot)

first_ingrid = ''
second_ingrid = ''


@dp.message_handler(content_types=['text'])
async def start(message):
    if message.text == '/start':
        await message.answer("Введи первый ингридиент")
        message.register_next_step_handler(message, get_first_ingrid)  # следующий шаг – функция get_name
    else:
        await message.answer('Привет!\nЯ выдаю рецепты по двум ингридиентам!\n'
                                                   'Напиши /start')


async def get_first_ingrid(message):
    global first_ingrid
    first_ingrid = message.text
    await message.answer('Введи sec ингридиент')
    message.register_next_step_handler(message, get_second_ingrid)


async def get_second_ingrid(message):
    global second_ingrid
    second_ingrid = message.text
    await message.answer('Catch')


if __name__ == '__main__':
    executor.start_polling(dp)
