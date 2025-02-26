import asyncio
from pprint import pprint
from typing import List, TypedDict

import httpx

from niffler.api import get_apis

apis = get_apis()


class Link(TypedDict):
    label: str
    url: str
    type: str


class Coin(TypedDict):
    url: str
    chainId: str
    tokenAddress: str
    icon: str
    header: str
    openGraph: str
    description: str
    links: List[Link]
    totalAmount: int
    amount: int


async def fetch_latest_coins() -> List[Coin]:
    async with httpx.AsyncClient() as client:
        res = await client.get(apis.latest_coin_from_dexscreener)
        coins = res.json()
        return coins


async def fetch_coin_detail(chainId: str, tokenAddress: str):
    async with httpx.AsyncClient() as client:
        res = await client.get(
            f"{apis.coin_detail_from_dexscreener}/{chainId}/{tokenAddress}"
        )
        coin_detail = res.json()
        return coin_detail


async def main():
    coins = await fetch_latest_coins()
    for coin in coins:
        coin_detail = await fetch_coin_detail(coin["chainId"], coin["tokenAddress"])
        pprint(coin_detail)


if __name__ == "__main__":
    asyncio.run(main())
