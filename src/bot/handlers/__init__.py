from bot.handlers.start import start_router
from src.bot.handlers.echo import echo_router


list_of_routers = [start_router]

__all__ = ["list_of_routers"]
