from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
import buttons
import re
from aiogram.types import ReplyKeyboardRemove


class FSM_reg(StatesGroup):
    id_product = State()
    size = State()
    quantity = State()
    phone = State()


async def fsm_start(message: types.Message):
    await message.answer(text='Привет! \n'
                              'Укажите артикул товара который вас интересует:\n\n'
                              '!Для того чтобы воспользоваться командами, '
                              'нажмите на "Отмена"!', reply_markup=buttons.cancel)
    await FSM_reg.id_product.set()


async def load_id_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id_product'] = message.text

    await FSM_reg.next()
    await message.answer(text='Укажите размер товара:')


async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

    await FSM_reg.next()
    await message.answer(text='Укажите количество товара:')


async def load_quantity(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['quantity'] = message.text

        await FSM_reg.next()
        await message.answer(text='Укажите ваш номер телефона:')


async def load_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text


    kb = types.ReplyKeyboardRemove()

    await message.answer_photo(photo=data['photo'],
                               caption=f"Артикул товара - {data['fullname']}\n"
                                       f"Размер товара - {data['age']}\n"
                                       f"Количество тоавара - {data['email']}\n"
                                       f"Номер тел - {data['phone']}\n"
                               )
    await message.answer(text='Ваш заказ принят!',reply_markup=kb)
    await state.finish()


async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer(text='Отменено!')


def zakazy_fsm(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, Text(equals='Отмена',
                                                 ignore_case=True),
                                state="*")

    dp.register_message_handler(fsm_start, commands=['registration'])
    dp.register_message_handler(load_id_product(), state=FSM_reg.id_product)
    dp.register_message_handler(load_size, state=FSM_reg.size)
    dp.register_message_handler(load_quantity(), state=FSM_reg.quantity)
    dp.register_message_handler(load_phone, state=FSM_reg.phone)
