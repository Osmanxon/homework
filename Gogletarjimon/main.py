
import logging
from googletrans import Translator

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6718466276:AAGVS4K_Bdgx0st8RFSD9kF8ULe15s3T9vE'
logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
translator=Translator()

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    await message.reply("Salom!\nBu bot siz kiritkan matnni rus tiliga tarjima qilib beradi!\nKerakli matnni kiriting.!")



@dp.message_handler()
async def gte_data(message: types.Message):
    translation=translator.translate(message.text,dest="ru")
    trans_text=translation.text
    await message.reply(trans_text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
