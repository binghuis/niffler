from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from niffler.config import settings
from niffler.models import User


async def connect_db() -> None:
    try:
        client: AsyncIOMotorClient = AsyncIOMotorClient(settings.mongo.url)
        await init_beanie(
            database=client[settings.mongo.name],
            document_models=[User],
        )
    except Exception as e:
        print(f"MongoDB connection failed: {e}")
        raise
