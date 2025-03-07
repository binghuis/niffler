# from telegram.ext import CommandHandler
# from niffler.bot import Bot
# from niffler.handlers import start
# bot = Bot()
# bot.add_handler(CommandHandler("start", start.handler))
# bot.run_polling()

from contextlib import asynccontextmanager

from fastapi import FastAPI

from niffler.config.db import connect_db
from niffler.routers import user


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("初始化数据库连接")
    await connect_db()
    yield
    print("关闭数据库连接")


app = FastAPI(lifespan=lifespan)

app.include_router(user.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
