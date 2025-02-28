from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from niffler.config import settings


async def init_db() -> None:
    client: AsyncIOMotorClient = AsyncIOMotorClient(settings.mongo.url)
    database = client[settings.mongo.name]
    await init_beanie(
        database=database,
        document_models=[],
    )


if __name__ == "__main__":

    async def main():
        await init_db()
