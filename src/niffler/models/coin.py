from typing import Dict, List

from beanie import Document

from niffler.schemas.coin import PairDataResponseCoin, PairDataResponseInfo


class MongoCoin(Document):
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

    class Settings:
        name = "coins"
