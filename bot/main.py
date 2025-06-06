from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.utils import executor
import os

API_TOKEN = os.getenv("7816012207:AAH5W5anKmcxXgZHCJJ2JDWsWN7rcosN3Ik")  # توکن رباتتو باید تو متغیر محیطی تنظیم کنی

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("سلام! ربات آماده است و به /start پاسخ میده.")

if __name__ == "__main__":
    executor.start_polling(dp)
