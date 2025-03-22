from settings import get_settings


def build_auth_url(telegram_id: int):
    settings = get_settings()
    url = settings.API_URL + f"/auth/{telegram_id}"
    return url
