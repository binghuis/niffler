import os
from functools import lru_cache

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

from niffler.types import DEXScreenerConfig, XAIConfig, XConfig

load_dotenv()


class Settings(BaseSettings):
    tg_bot_token: str = os.getenv("TELEGRAM_BOT_TOKEN", "")
    xai: XAIConfig = XAIConfig(
        model="grok-2-latest",
        base_url="https://api.x.ai/v1",
        api_key=os.getenv("XAI_API_KEY", ""),
    )
    x: XConfig = XConfig(bearer_token=os.getenv("X_BEARER_TOKEN", ""))
    dexscreener: DEXScreenerConfig = DEXScreenerConfig(
        api_top="https://api.dexscreener.com/token-profiles/top/v1",
        api_latest="https://api.dexscreener.com/token-profiles/latest/v1",
        api_pairs="https://api.dexscreener.com/token-pairs/v1",
    )


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
