from contextlib import asynccontextmanager

from fastapi import FastAPI
from telegram.ext import CommandHandler

from niffler.config.db import DBManager
from niffler.config.scheduler import SchedulerManager
from niffler.handlers import start
from niffler.routers import coin
from niffler.tasks.dexscreener_hunter import DexscreenerHunter
from niffler.tasks.telegram_bot import TelegramBot

app = FastAPI()

db = DBManager()
scheduler = SchedulerManager()

tg_bot = TelegramBot()


@asynccontextmanager
async def lifespan(app: FastAPI):
    tg_bot.add_handler(CommandHandler("start", start.handler))
    tg_bot.run_polling()
    await db.connect()
    scheduler.add_task(DexscreenerHunter())
    await scheduler.start()
    yield
    await scheduler.shutdown()
    await db.close()


app = FastAPI(lifespan=lifespan)

app.include_router(coin.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
