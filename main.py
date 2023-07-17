from aiogram import Dispatcher, executor, Bot
from  aiogram.types import Message
bot = Bot('6035367479:AAHFneZGRy0jg3Zhug_ekGxO2svxeo5ccFE')
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: Message):
    await  message.answer(f'xush kelbsz {message}')

executor.start_polling(dp, skip_updates=True)
