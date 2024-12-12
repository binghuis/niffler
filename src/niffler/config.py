import os
from functools import lru_cache

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    tg_bot_token: str = os.getenv("TELEGRAM_BOT_TOKEN", "")


@lru_cache
def get_settings():
    return Settings()
