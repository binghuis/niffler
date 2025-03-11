from pydantic import BaseModel


class GrokConfig(BaseModel):
    api_key: str
    base_url: str
    model: str


class XConfig(BaseModel):
    bearer_token: str


class DEXScreenerConfig(BaseModel):
    api_pairs: str
    api_latest: str
    api_top: str


class DeepSeekConfig(BaseModel):
    api_key: str
    base_url: str
    model: str


class MongoConfig(BaseModel):
    admin_name: str
    admin_password: str
    url: str
    name: str


class KimiConfig(BaseModel):
    api_key: str
    base_url: str
    model: str
