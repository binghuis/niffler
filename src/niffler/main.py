# from telegram.ext import CommandHandler
# from niffler.bot import Bot
# from niffler.handlers import start
# bot = Bot()
# bot.add_handler(CommandHandler("start", start.handler))
# bot.run_polling()
import uuid
from contextlib import asynccontextmanager
from datetime import datetime

from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from fastapi import FastAPI
from pymongo import MongoClient

from niffler.config import settings
from niffler.config.db import connect_db
from niffler.routers import coin

app = FastAPI()


scheduler = AsyncIOScheduler(
    jobstores={
        "default": MongoDBJobStore(
            database=settings.mongo.name,
            collection="jobs",
            client=MongoClient(settings.mongo.url),
        )
    },
    timezone="Asia/Shanghai",
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_db()
    scheduler.add_job(
        my_task,
        IntervalTrigger(seconds=1),
        id=uuid.uuid4().hex,
        replace_existing=True,
    )
    scheduler.start()
    yield
    if scheduler.running:
        scheduler.shutdown(wait=False)


app = FastAPI(lifespan=lifespan)

app.include_router(coin.router)


async def my_task():
    print(f"任务执行时间：{datetime.now()}")


@app.get("/")
def read_root():
    return {"Hello": "World"}
