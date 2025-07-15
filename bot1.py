import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '7895557739:AAF5CR2fDYTLqCaMFn-8nGs-ZA81E8ZQrmg'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu aleykum botga hush kelibsiz...")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
