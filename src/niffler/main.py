import asyncio

import uvicorn
from fastapi import FastAPI

from niffler.bot import Bot
from niffler.config import get_settings
from niffler.handlers import start_handler


async def run_bot():
    bot = Bot()
    bot.add_handler(start_handler.handler)
    bot.run_polling()


async def startup_event():
    asyncio.create_task(run_bot())


app = FastAPI(on_startup=[startup_event])


settings = get_settings()


# @app.get("/")
# async def get_bot_info():
#     url = f"https://api.telegram.org/bot{settings.tg_bot_token}/getMe"

#     async with httpx.AsyncClient() as client:
#         try:
#             response = await client.get(url)
#             response.raise_for_status()
#             return response.json()
#         except httpx.HTTPStatusError as e:
#             raise HTTPException(status_code=e.response.status_code, detail=str(e))
#         except httpx.RequestError as e:
#             raise HTTPException(status_code=500, detail=f"Request failed: {str(e)}")


if __name__ == "__main__":
    uvicorn.run(app)
