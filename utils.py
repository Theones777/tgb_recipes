from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class ChooseIndrids(StatesGroup):
    get_first_ingrid = State()
    get_second_ingrid = State()


async def start(message):
    await message.answer("Введи первый ингридиент")
    await ChooseIndrids.get_first_ingrid.set()


async def first_chosen(message: types.Message, state: FSMContext):
    await state.update_data(f_ingr=message.text.lower())
    await ChooseIndrids.next()
    await message.answer("Введи второй ингридиент")


async def sec_chosen(message: types.Message, state: FSMContext):
    user_data = await state.get_data()

    await message.answer(f"Ты выбрал {user_data['f_ingr']} и {message.text.lower()}")

    await state.finish()


def register_handlers_main(dp: Dispatcher):
    dp.register_message_handler(start, commands="start", state="*")
    dp.register_message_handler(first_chosen, state=ChooseIndrids.get_first_ingrid)
    dp.register_message_handler(sec_chosen, state=ChooseIndrids.get_second_ingrid)
