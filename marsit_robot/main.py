import logging

from aiogram import Bot, Dispatcher, executor, types
from buttons import *

API_TOKEN = ''

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'pomosh'])
async def send_welcome(message: types.Message):
    await message.reply("Добро пожаловать в Mars IT! Пожалуйста, выберите вариант",reply_markup=glavniy_keyboard)


@dp.callback_query_handler(text="Я Родитель")
async def echo(call: types.CallbackQuery):
    await call.message.answer("Ассаляму алейкум уважаемый родитель!", reply_markup=ota_ona_keyboard)

@dp.callback_query_handler(text="Я Студент")
async def echo(call: types.CallbackQuery):
    await call.message.answer("Ассаляму алейкум уважаемый студент!", reply_markup=uchenik_keyboard)

@dp.callback_query_handler(text="Я Гость")  
async def echo(call: types.CallbackQuery):
    await call.message.answer("Ассаляму алейкум уважаемый гость!")


@dp.callback_query_handler(text="MARS mini")  
async def echo(call: types.CallbackQuery):
    await call.message.answer_photo("https://t.me/giwoek/24", caption=" MARS mini\nPrice: 20", reply_markup=space_shop_keyboard)

@dp.callback_query_handler(text="MARS Sticker")  
async def echo(call: types.CallbackQuery):
    await call.message.answer_photo("https://t.me/giwoek/25", caption=" MARS Sticker\nPrice: 70", reply_markup=space_shop_keyboard)


@dp.callback_query_handler(text="Usb fleshka")  
async def echo(call: types.CallbackQuery):
    await call.message.answer_photo("https://t.me/giwoek/19", caption=" Usb fleshka\nPrice: 150", reply_markup=space_shop_keyboard)

@dp.callback_query_handler(text="MARS chocolate")  
async def echo(call: types.CallbackQuery):
    await call.message.answer_photo("https://t.me/giwoek/22", caption=" MARS chocolate\nPrice: 50", reply_markup=space_shop_keyboard)

@dp.callback_query_handler(text="Mouse")  
async def echo(call: types.CallbackQuery):
    await call.message.answer_photo("https://t.me/giwoek/21", caption=" Mouse\nPrice: 250", reply_markup=space_shop_keyboard)

@dp.callback_query_handler(text="Strobar")  
async def echo(call: types.CallbackQuery):
    await call.message.answer_photo("https://t.me/giwoek/23", caption=" Strobar\nPrice: 30", reply_markup=space_shop_keyboard)

@dp.callback_query_handler(text="Имя")  
async def echo(call: types.CallbackQuery):
    await call.message.answer("Имя: Muhammadbilol", reply_markup=mars_keyboard)

@dp.callback_query_handler(text="Фамилия")  
async def echo(call: types.CallbackQuery):
    await call.message.answer("Фамилия: Bahtiyorov", reply_markup=mars_keyboard)

@dp.callback_query_handler(text="Язык")  
async def echo(call: types.CallbackQuery):
    await call.message.answer("Язык: ru", reply_markup=mars_keyboard)

@dp.callback_query_handler(text="Телефон")  
async def echo(call: types.CallbackQuery):
    await call.message.answer("Телефон: 974077909", reply_markup=mars_keyboard)

@dp.callback_query_handler(text="Город")  
async def echo(call: types.CallbackQuery):
    await call.message.answer("Город: Toshkent", reply_markup=mars_keyboard)


@dp.callback_query_handler(text="Работы учеников")  
async def echo(call: types.CallbackQuery):
    await call.message.answer_video("https://t.me/giwoek/28?single")
    await call.message.answer_video("https://t.me/giwoek/29")
    await call.message.answer_video("https://t.me/giwoek/30")
    await call.message.answer("Работы учеников", reply_markup=shkola_keyboard)


@dp.callback_query_handler(text="Преподователи")  
async def echo(call: types.CallbackQuery):
    await call.message.answer_video("https://t.me/giwoek/32?single")
    await call.message.answer_video("https://t.me/giwoek/33")
    await call.message.answer_video("https://t.me/giwoek/34")
    await call.message.answer("Преподователи", reply_markup=shkola_keyboard)

# @dp.callback_query_handler(text="14-16 лет")  
# async def echo(call: types.CallbackQuery):
#     await call.message.answer("Выберите", reply_markup=otziv_keyboard)







@dp.message_handler(text="🧑‍🎓Профиль")
async def echo(message: types.Message):
    await message.answer("""
    Имя: Muhammadbilol
    Фамилия: Bahtiyorov
    Телефон: 974077909
    Город: Toshkent
    Учебный центр: YUNUSABAD""", reply_markup=mars_keyboard)

@dp.message_handler(text="🪙Мои монеты")
async def echo(message: types.Message):
    await message.reply("Мои марс монеты: 12", reply_markup=uchenik_keyboard)

@dp.message_handler(text="💥Space shop")
async def echo(message: types.Message):
    await message.reply("Выберите приз", reply_markup=space_shop_keyboard)

@dp.message_handler(text="✍️Оставить отзыв")
async def echo(message: types.Message):
    await message.answer_photo("https://t.me/giwoek/27")
    await message.reply("Напишите свой отзыв")

@dp.message_handler(text="🏫О школе")
async def echo(message: types.Message):
    await message.reply("Выберите кнопку", reply_markup=shkola_keyboard)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
