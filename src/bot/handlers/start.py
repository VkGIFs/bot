from typing import Any

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from core.constants.descriptions import GREETING_MESSAGE
from models.buttons.start_buttons import create_start_buttons_markup

start_router = Router(name="start")


@start_router.message(CommandStart())
async def start_handler(message: Message) -> Any:
    """Echo message handlers"""

    first_time = True  # todo

    if first_time:
        await message.answer(GREETING_MESSAGE, reply_markup=create_start_buttons_markup(message.from_user.id))
