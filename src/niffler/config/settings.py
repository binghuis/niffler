from functools import lru_cache
from os import getenv

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

from niffler.typedefs import (
    DeepSeekConfig,
    DEXScreenerConfig,
    GrokConfig,
    KimiConfig,
    MongoConfig,
    XConfig,
)

load_dotenv()


class Settings(BaseSettings):
    tg_bot_token: str = getenv("TELEGRAM_BOT_TOKEN", "")

    grok: GrokConfig = GrokConfig(
        api_key=getenv("GROK_API_KEY", ""),
        base_url="https://api.x.ai/v1",
        model="grok-2-latest",
    )

    kimi: KimiConfig = KimiConfig(
        api_key=getenv("MOONSHOT_API_KEY", ""),
        base_url="https://api.moonshot.cn/v1",
        model="moonshot-v1-8k-vision-preview",
    )

    x: XConfig = XConfig(bearer_token=getenv("X_BEARER_TOKEN", ""))

    dexscreener: DEXScreenerConfig = DEXScreenerConfig(
        api_top="https://api.dexscreener.com/token-profiles/top/v1",
        api_latest="https://api.dexscreener.com/token-profiles/latest/v1",
        api_pairs="https://api.dexscreener.com/token-pairs/v1",
    )

    deepseek: DeepSeekConfig = DeepSeekConfig(
        api_key=getenv("DEEPSEEK_API_KEY", ""),
        base_url="https://api.deepseek.com",
        model="deepseek-reasoner",
    )

    mongo: MongoConfig = MongoConfig(
        admin_name="admin",
        admin_password="123456",
        name="niffler",
        url=f"mongodb://{getenv('MONGO_INITDB_ROOT_USERNAME')}:{getenv('MONGO_INITDB_ROOT_PASSWORD')}@mongo/niffler?authSource=admin&directConnection=true",
    )


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
