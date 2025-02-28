import os
from functools import lru_cache

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

from niffler.types import (
    DeepSeekConfig,
    DEXScreenerConfig,
    MongoConfig,
    XAIConfig,
    XConfig,
)

load_dotenv()


class Settings(BaseSettings):
    tg_bot_token: str = os.getenv("TELEGRAM_BOT_TOKEN", "")

    xai: XAIConfig = XAIConfig(
        api_key=os.getenv("XAI_API_KEY", ""),
        base_url="https://api.x.ai/v1",
        model="grok-2-latest",
    )

    x: XConfig = XConfig(bearer_token=os.getenv("X_BEARER_TOKEN", ""))

    dexscreener: DEXScreenerConfig = DEXScreenerConfig(
        api_top="https://api.dexscreener.com/token-profiles/top/v1",
        api_latest="https://api.dexscreener.com/token-profiles/latest/v1",
        api_pairs="https://api.dexscreener.com/token-pairs/v1",
    )

    deepseek: DeepSeekConfig = DeepSeekConfig(
        api_key=os.getenv("DEEPSEEK_API_KEY", ""),
        base_url="https://api.deepseek.com",
        model="deepseek-reasoner",
    )

    mongo: MongoConfig = MongoConfig(name="niffler_db", url="mongodb://localhost:27017")


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
