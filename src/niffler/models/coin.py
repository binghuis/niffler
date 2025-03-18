from beanie import Document
from pydantic import Field


class MongoCoin(Document):
    name: str = Field(..., description="代币名")
    symbol: str = Field(..., description="代币符号")

    class Settings:
        name = "coins"
