from typing import Optional

from beanie import PydanticObjectId

from niffler.models.crypto_token import (
    CryptoToken,
)


class CryptoTokenService:
    @staticmethod
    async def save_token(name: str, symbol: str) -> CryptoToken:
        token = CryptoToken(name=name, symbol=symbol)
        await token.insert()
        return token

    @staticmethod
    async def get_token_by_id(token_id: PydanticObjectId) -> CryptoToken:
        token = await CryptoToken.get(token_id)
        if token is None:
            raise ValueError(f"Token with id {token_id} not found")
        return token

    @staticmethod
    async def update_token(
        token_id: PydanticObjectId,
        name: Optional[str] = None,
        symbol: Optional[str] = None,
    ) -> CryptoToken:
        token = await CryptoToken.get(token_id)
        if token is None:
            raise ValueError(f"Token with id {token_id} not found")
        if name:
            token.name = name
        if symbol:
            token.symbol = symbol
        await token.save()
        return token

    @staticmethod
    async def delete_token(token_id: PydanticObjectId) -> bool:
        token = await CryptoToken.get(token_id)
        if token:
            await token.delete()
            return True
        return False

    @staticmethod
    async def get_all_tokens() -> list[CryptoToken]:
        tokens = await CryptoToken.find_all().to_list()
        return tokens
