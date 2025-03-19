from datetime import datetime

from apscheduler.triggers.interval import IntervalTrigger

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
