from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart,CommandHelp
from aiogram.dispatcher import filters

from aiogram.utils.markdown import hbold, hcode, hitalic, hunderline, hlink, hstrikethrough
from loader import dp

# html formatlash
@dp.message_handler(commands='info_html')
async def bot_help(message: types.Message):
    text=f"Assalomu alaykum {message.from_user.full_name}!\n"
    text += "Bu <b> qalin </b> shirft\n"
    text += "Bu <i> qalin </i> shirft\n"
    text += "Bu <u> qalin </u> shirft\n"
    text += "Bu <s> qalin </s> shirft\n"
    text += "Bu <a href='https://kun.uz'> Kun uz sahifasi </a>"
    text += "Bu kod: <code> print('Salom') </code>"d

    await message.answer(text)

# markdown formatlash
@dp.message_handler(commands="info_markdown")
async def get_mark(message: types.Message):
    text += f"Assalomu alaykum {message.from_user.full_name}\!\n"
    text += f"Bu *Qalin shirft markdown usulida*"
    text += f"~to'liq~"
    text += f"[Kun uz sahifasi](https://kun.uz)"

    await message.answer(text,parse_mode=types.ParseMode.MARKDOWN_V2)

# aiogram funksiya yordamida farmatlash
@dp.message_handler(commands="info_aiogram")
async def get_aio(message: types.Message):
    text = f"Assalomu alaykum {message.from_user.full_name}!\n"
    text += "Bu " + hbold('qalin \n')
    text += "Bu " + hitalic('qalin \n')
    text += "Bu " + hunderline('qalin \n')
    text += "Bu " + hstrikethrough('qalin \n')
    text += "Bu " + hcode('@dp.message_hundler(commands="info_aiogram")\n')
    await message.answer(text)

@dp.message_handler(content_types='contact',is_sender_contact=True)
@dp.message_handler(filters.IsSenderContact,content_types='contact')
async def reply_contact(msg: types.Message):
    await msg.answer('Raqamingiz qabul qilindi')

@dp.message_handler(is_forwarded=True)
async def reply_forward(msg: types.Message):
    await msg.answer('Men uzatilgan habarlarga javob bermayman')












