# from telegram.ext import CommandHandler
# from niffler.bot import Bot
# from niffler.handlers import start
# bot = Bot()
# bot.add_handler(CommandHandler("start", start.handler))
# bot.run_polling()
from contextlib import asynccontextmanager

from fastapi import FastAPI

from niffler.config.db import connect_db
from niffler.routers import coin

app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_db()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(coin.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
