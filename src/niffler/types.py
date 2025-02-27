from pydantic import BaseModel


class XAIConfig(BaseModel):
    api_key: str
    base_url: str
    model: str


class XConfig(BaseModel):
    bearer_token: str


class DEXScreenerConfig(BaseModel):
    api_pairs: str
    api_latest: str
    api_top: str
