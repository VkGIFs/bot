from aiogram import Dispatcher

from src.bot.handlers import list_of_routers


def setup_all_routers(dp: Dispatcher):
    """Include all routers from app"""

    dp.include_routers(*list_of_routers)
    return dp
