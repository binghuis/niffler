from typing import Optional

from beanie import PydanticObjectId

from niffler.models.coin import (
    MongoCoin,
)


class ServiceCoin:
    @staticmethod
    async def save(name: str, symbol: str) -> MongoCoin:
        token = MongoCoin(name=name, symbol=symbol)
        await token.insert()
        return token

    @staticmethod
    async def get_by_id(token_id: PydanticObjectId) -> MongoCoin:
        token = await MongoCoin.get(token_id)
        if token is None:
            raise ValueError(f"Token with id {token_id} not found")
        return token

    @staticmethod
    async def update(
        token_id: PydanticObjectId,
        name: Optional[str] = None,
        symbol: Optional[str] = None,
    ) -> MongoCoin:
        token = await MongoCoin.get(token_id)
        if token is None:
            raise ValueError(f"Token with id {token_id} not found")
        if name:
            token.name = name
        if symbol:
            token.symbol = symbol
        await token.save()
        return token

    @staticmethod
    async def delete(token_id: PydanticObjectId) -> bool:
        token = await MongoCoin.get(token_id)
        if token:
            await token.delete()
            return True
        return False

    @staticmethod
    async def get_all() -> list[MongoCoin]:
        tokens = await MongoCoin.find_all().to_list()
        return tokens
