from abc import ABC, abstractmethod

from apscheduler.triggers.base import BaseTrigger


class BaseTask(ABC):
    @property
    @abstractmethod
    def id(self) -> str:
        pass

    @property
    @abstractmethod
    def trigger(self) -> BaseTrigger:
        pass

    @abstractmethod
    async def run(self) -> None:
        pass
