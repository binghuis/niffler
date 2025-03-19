from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from niffler.config import settings
from niffler.models import MongoCoin


class DBManager:
    def __init__(self) -> None:
        self.client: AsyncIOMotorClient = AsyncIOMotorClient(
            settings.mongo.url,
        )
        self.db = self.client.get_database(settings.mongo.name)

    async def connect(self):
        await init_beanie(
            database=self.db,
            document_models=[MongoCoin],
        )

    async def close(self):
        self.client.close()
