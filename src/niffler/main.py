# from telegram.ext import CommandHandler
# from niffler.bot import Bot
# from niffler.handlers import start
# bot = Bot()
# bot.add_handler(CommandHandler("start", start.handler))
# bot.run_polling()
from contextlib import asynccontextmanager

from fastapi import FastAPI

from niffler.config.db import DBManager
from niffler.config.scheduler import SchedulerManager
from niffler.routers import coin
from niffler.tasks.coin_hunter import CoinHunter

app = FastAPI()

db = DBManager()
scheduler = SchedulerManager()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.connect()
    scheduler.add_task(CoinHunter())
    await scheduler.start()
    yield
    await scheduler.shutdown()
    await db.close()


app = FastAPI(lifespan=lifespan)

app.include_router(coin.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
