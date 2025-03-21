from typing import Dict, List

from pydantic import BaseModel


class LatestCoinResponseLink(BaseModel):
    type: str
    label: str
    url: str


class LatestCoinResponse(BaseModel):
    url: str
    chainId: str  # 代币所在的区块链链 ID
    coinAddress: str  # 代币在区块链上的地址
    icon: str  # 代币图标的 URL
    header: str  # 代币头部图片的 URL
    description: str
    links: List[LatestCoinResponseLink]


class PairDataResponseCoin(BaseModel):
    address: str  # 代币的地址
    name: str  # 代币的名称
    symbol: str  # 代币的符号


class PairDataResponseWebsite(BaseModel):
    url: str  # 网站的 URL


class PairDataResponseSocial(BaseModel):
    platform: str  # 社交媒体的平台名称
    handle: str  # 社交媒体账号的名称或 ID


class PairDataResponseInfo(BaseModel):
    imageUrl: str  # 代币图片的 URL
    websites: List[PairDataResponseWebsite]  # 相关网站的列表
    socials: List[PairDataResponseSocial]  # 相关社交媒体的列表


class PairDataResponse(BaseModel):
    chainId: str  # 区块链链 ID
    dexId: str  # 去中心化交易所的 ID
    url: str  # 交易对的 URL
    pairAddress: str  # 交易对的地址
    labels: List[str]  # 交易对的标签列表
    baseCoin: PairDataResponseCoin  # 基础代币的信息
    quoteCoin: PairDataResponseCoin  # 报价代币的信息
    priceNative: str  # 本地货币的价格
    priceUsd: str  # 美元价格
    txns: Dict[str, Dict[str, int]]  # 交易数据
    volume: Dict[str, int]  # 交易量数据
    priceChange: Dict[str, int]  # 价格变化数据
    liquidity: Dict[str, int]  # 流动性数据
    fdv: int  # 完全稀释估值
    marketCap: int  # 市值
    pairCreatedAt: int  # 交易对创建时间戳
    info: PairDataResponseInfo  # 附加信息
    boosts: Dict[str, int]  # 助推数据
