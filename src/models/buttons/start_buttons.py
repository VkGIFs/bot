from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, LoginUrl

from core.auth_url import build_auth_url
from core.constants.buttons import LOGIN_BUTTON_TEXT


def create_start_buttons_markup(telegram_id: int) -> InlineKeyboardMarkup:
    """Create inline keyboard markup for start buttons"""

    url = build_auth_url(telegram_id=telegram_id)
    login_button = InlineKeyboardButton(text=LOGIN_BUTTON_TEXT, url=url)
    return InlineKeyboardMarkup(inline_keyboard=[[login_button]])
