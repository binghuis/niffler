import os
from functools import lru_cache

from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings

load_dotenv()


@lru_cache
def get_settings():
    return Settings()


class XAIConfig(BaseModel):
    api_key: str
    base_url: str


class Settings(BaseSettings):
    tg_bot_token: str = os.getenv("TELEGRAM_BOT_TOKEN", "")
    xai: XAIConfig = XAIConfig(
        api_key=os.getenv("XAI_API_KEY", ""),
        base_url=os.getenv("XAI_BASE_URL") or "https://api.x.ai/v1",
    )
