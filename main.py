import asyncio

from aiogram import Bot, Dispatcher

from src.settings import get_settings
from src.utils.routers_bind import setup_all_routers


app_settings = get_settings()


async def main():
    """Like a lifespan function"""

    bot = Bot(token=app_settings.TELEGRAM_API_TOKEN.get_secret_value())

    dp = Dispatcher()
    dp = setup_all_routers(dp)

    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    asyncio.run(main())
