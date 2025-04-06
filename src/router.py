from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from config import bot

user_router = Router()


@user_router.message(CommandStart())
async def f1(message: Message, state: FSMContext):
    await bot.send_message(
        chat_id=message.chat.id,
        text=message.chat.first_name
    )


@user_router.message(F.text == "228")
async def f2(message: Message, state: FSMContext):
    await bot.send_message(
        chat_id=message.chat.id,
        text=f"{message.text} это статья"
    )

@user_router.message()
async def f3(message: Message, state: FSMContext):
    await bot.send_message(
        chat_id=message.chat.id,
        text=message.text
    )
