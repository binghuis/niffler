from apscheduler.triggers.interval import IntervalTrigger

from niffler.integrations.coin import fetch_coin_pair_data, fetch_latest_coins
from niffler.models.coin import MongoCoin

from .base import BaseTask


class DexscreenerHunter(BaseTask):
    @property
    def id(self) -> str:
        return "coin_hunter"

    @property
    def trigger(self) -> IntervalTrigger:
        return IntervalTrigger(seconds=1)

    async def run(self) -> None:
        coins = await fetch_latest_coins()
        for coin in coins:
            if MongoCoin.find_one({"pairAddress": coin.coinAddress}) is None:
                coin_detail = await fetch_coin_pair_data(coin.chainId, coin.coinAddress)
                print(coin_detail)
                # await MongoCoin(**coin_detail["pairs"][0]).insert()
