import logging

from aiogram import Bot,Dispatcher,executor,types

API_TOKEN='7470980536:AAEuN0LgZoEby3MXb_sivDXuutiIhBqa7v4'

logging.basicConfig(level=logging.INFO)
bot=Bot(token=API_TOKEN)
dp=Dispatcher(bot)
@dp.message_handler(commands=['start','help'])
async def send_welcome(message: types.Message):
    """This handler will be called when user '/start' or '/help' command"""
    await message.reply("Salom\nHi!\nI'm Echobot aiogram.")
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)


