from pprint import pprint

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from niffler.config import settings
from niffler.models import CryptoToken


async def connect_db() -> None:
    try:
        print(settings.mongo)
        client: AsyncIOMotorClient = AsyncIOMotorClient(
            settings.mongo.url,
        )
        db = client.get_database(settings.mongo.name)
        await init_beanie(
            database=db,
            document_models=[CryptoToken],
        )

    except Exception as e:
        pprint(f"MongoDB connection failed: {e}")
        raise
