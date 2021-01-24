from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from mortgage import Mortgage
from loader import dp
from states.form import Form
import logging

morty = Mortgage()

@dp.message_handler(Command("calculate"))
async def enter_form(message: types.Message):

    await message.answer("Введите стоимость объекта \n")
    await Form.Q1.set()


@dp.message_handler(state=Form.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(oject_cost=answer)
    await message.answer("Ввведите первоначальный взнос в %\n")
    await Form.next()

@dp.message_handler(state=Form.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(first_part=answer)
    await message.answer("Ввведите процентную ставку в %. Например: 9.5\n")
    await Form.next()

@dp.message_handler(state=Form.Q3)
async def answer_q3(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(interest_rate=answer)
    await message.answer("Ввведите количество лет ипотеки \n")
    await Form.next()

#
@dp.message_handler(state=Form.Q4)
async def answer_q4(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(mortgage_years = answer)

    data = await state.get_data()
    answer1 = data.get("oject_cost")
    answer2 = data.get("first_part")
    answer3 = data.get("interest_rate")
    answer4 = data.get("mortgage_years")

    answers = [answer1, answer2, answer4]
    if answer3:
        answer3 = answer3.replace(',', '.')

    if all([a.isdigit() for a in answers]):
        try:
            morty.home_value = int(answer1)
            morty.down_payment_percent = float(answer2) / 100
            morty.mortgage_rate = float(answer3) / 100
            morty.years = int(answer4)
            morty.run()

            await message.answer(f'Первоначальный платеж: {int(morty.down_payment)}')
            await message.answer(f'Сумма кредита: {int(morty.mortgage_loan)}')
            await message.answer(f'Процентная ставка по кредиту : {morty.mortgage_rate * 100}%')
            await message.answer(f'Количетство лет кредита: {morty.years}')
            await message.answer(f'Количетсво платежей: {morty.mortgage_payment_periods}')
            await message.answer(f"Ежемесячный платеж по кредиту: {round(morty.periodic_mortgage_payment, 2)}")
            await message.answer(f"Первый платеж (проценты): {round(morty.initial_interest_payment, 2)}")
            await message.answer(f"Первый платеж (основной долг): {round(morty.initial_principal_payment, 2)}")

            await state.reset_state()
        except ValueError as e:
            logging.info(e)
            await message.answer(f'А теперь давай попробуем ввести цифры')
            await state.reset_state()
    else:
        await message.answer(f'А теперь давай попробуем ввести цифры')
        await state.reset_state()