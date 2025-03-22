from typing import Any

from aiogram import Router
from aiogram.types import Message


echo_router = Router(name="echo")


@echo_router.message()
async def message_handler(message: Message) -> Any:
    """Echo message handlers"""

    await message.answer("Hello from my router!")
