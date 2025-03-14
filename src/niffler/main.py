# from telegram.ext import CommandHandler
# from niffler.bot import Bot
# from niffler.handlers import start
# bot = Bot()
# bot.add_handler(CommandHandler("start", start.handler))
# bot.run_polling()

from contextlib import asynccontextmanager

from fastapi import FastAPI

from niffler.config.db import connect_db
from niffler.routers import crypto_token


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("连接数据库")
    await connect_db()
    print("数据库连接成功")
    yield
    print("关闭数据库连接")


app = FastAPI(lifespan=lifespan)

app.include_router(crypto_token.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
