import asyncio
from typing import List

import httpx

from niffler.config import settings
from niffler.schemas.coin import LatestCoinResponse, PairDataResponse


async def fetch_latest_coins() -> List[LatestCoinResponse]:
    async with httpx.AsyncClient() as client:
        res = await client.get(settings.dexscreener.api_latest)
        coins = res.json()
        return coins


async def fetch_coin_pair_data(
    chainId: str, tokenAddress: str
) -> List[PairDataResponse]:
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
            coin_detail = await fetch_coin_pair_data(
                coin["chainId"], coin["tokenAddress"]
            )
            print(coin_detail)

    asyncio.run(main())
