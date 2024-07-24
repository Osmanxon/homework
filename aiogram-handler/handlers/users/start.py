from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart,CommandHelp

from loader import dp

BLACKLIST=[6491720394]

@dp.message_handler(chat_id=BLACKLIST,text='/start ')
async def bot_start(message: types.Message):
    text=f"Salom,{message.from_user.full_name}! Siz bloklangansiz!"
    await message.answer(text)


@dp.message_handler(CommandStart(deep_link="itpark_echo"))
async def bot_start(message: types.Message):
    args=message.get_args()
    text=f"Salom,{message.from_user.full_name}!"
    text+=f"Sizni {args} tavsiya qildi"
    await message.answer(text)

# @dp.message_handler(CommandHelp())
# async def help(msg: types.Message):
#     text=f"Bu bot Filter uchun yaratilgan"
#     await (msg.answer())