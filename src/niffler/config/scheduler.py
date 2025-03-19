from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pymongo import MongoClient

from niffler.config import settings
from niffler.tasks.base import BaseTask


class SchedulerManager:
    def __init__(self):
        self.scheduler = AsyncIOScheduler(
            jobstores={
                "default": MongoDBJobStore(
                    database=settings.mongo.name,
                    collection="jobs",
                    client=MongoClient(settings.mongo.url),
                )
            },
            timezone=settings.timezone,
        )

    def add_task(self, task: BaseTask) -> bool:
        try:
            self.scheduler.add_job(
                task.run,
                trigger=task.trigger,
                id=task.id,
                replace_existing=True,
            )
            return True
        except Exception:
            return False

    async def start(self) -> None:
        if not self.scheduler.running:
            self.scheduler.start()

    async def shutdown(self, wait: bool = False) -> None:
        if self.scheduler.running:
            self.scheduler.shutdown(wait=wait)
