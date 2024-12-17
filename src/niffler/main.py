import httpx
from fastapi import FastAPI, HTTPException

from niffler.config import get_settings

app = FastAPI()


@app.get("/")
async def get_bot_info():
    url = f"https://api.telegram.org/bot{get_settings().tg_bot_token}/getMe"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=str(e))
        except httpx.RequestError as e:
            raise HTTPException(status_code=500, detail=f"Request failed: {str(e)}")


if __name__ == "__main__":
    pass
