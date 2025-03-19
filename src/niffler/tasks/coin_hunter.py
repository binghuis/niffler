import asyncio
from datetime import datetime

import httpx
from apscheduler.triggers.interval import IntervalTrigger

from niffler.config import settings

from .base import BaseTask


class CoinHunter(BaseTask):
    @property
    def id(self) -> str:
        return "coin_hunter"

    @property
    def trigger(self) -> IntervalTrigger:
        return IntervalTrigger(seconds=1)

    async def run(self) -> None:
        print(f"任务执行时间：{datetime.now()}")


async def fetch_latest_coins():
    async with httpx.AsyncClient() as client:
        res = await client.get(settings.dexscreener.api_latest)
        coins = res.json()
        return coins


async def fetch_coin_detail(chainId: str, tokenAddress: str):
    async with httpx.AsyncClient() as client:
        res = await client.get(
            f"{settings.dexscreener.api_pairs}/{chainId}/{tokenAddress}"
        )
        coin_detail = res.json()
        return coin_detail


if __name__ == "__main__":

    async def main():
        coins = await fetch_latest_coins()
        for coin in coins:
            await fetch_coin_detail(coin["chainId"], coin["tokenAddress"])

    asyncio.run(main())
