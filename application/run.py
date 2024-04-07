import asyncio
import logging
from aiogram import Bot, Dispatcher, types

from application.keyboards.keyboards import inline_kb2
from application.token import token

logging.basicConfig(level=logging.INFO)

bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler()
async def welcome(message: types.Message):
    await bot.send_photo(message.from_user.id,
                         photo=open('static/hello.png', 'rb'),
                         caption=f'Привет!🖖 Я бот-Артём!'
                                 f'Давай я тебе помогу. Но сначала мне нужно понять что бы ты хотела.'
                                 f'Выбери, пожалуйста, один из вариантов внизу😉', reply_markup=inline_kb2)


async def main():
    await dp.start_polling()


if __name__ == "__main__":
    asyncio.run(main())
