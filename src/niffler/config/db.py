from pprint import pprint

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from niffler.config import settings
from niffler.models import MongoCoin


async def connect_db() -> None:
    try:
        client: AsyncIOMotorClient = AsyncIOMotorClient(
            settings.mongo.url,
        )
        db = client.get_database(settings.mongo.name)
        await init_beanie(
            database=db,
            document_models=[MongoCoin],
        )

    except Exception as e:
        pprint(f"MongoDB connection failed: {e}")
        raise
