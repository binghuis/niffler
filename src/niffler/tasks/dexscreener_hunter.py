from apscheduler.triggers.interval import IntervalTrigger

from niffler.integrations.coin import fetch_latest_coins

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
        # print(coins)
        # for coin in coins:
        #     if MongoCoin.find_one({"pairAddress": coin["tokenAddress"]}) is None:
        #         coin_detail = await fetch_coin_detail(
        #             coin["chainId"], coin["tokenAddress"]
        #         )
        #         await MongoCoin(**coin_detail["pairs"][0]).insert()
