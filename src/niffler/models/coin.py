from typing import Dict, List

from beanie import Document
from pydantic import BaseModel


class BaseToken(BaseModel):
    address: str  # 代币的合约地址
    name: str  # 代币的名称
    symbol: str  # 代币的符号


class QuoteToken(BaseModel):
    address: str  # 代币的合约地址
    name: str  # 代币的名称
    symbol: str  # 代币的符号


class Txns(BaseModel):
    m5: Dict[str, int]  # 过去5分钟内的交易数据（买入和卖出）
    h1: Dict[str, int]  # 过去1小时内的交易数据（买入和卖出）
    h6: Dict[str, int]  # 过去6小时内的交易数据（买入和卖出）
    h24: Dict[str, int]  # 过去24小时内的交易数据（买入和卖出）


class Volume(BaseModel):
    h24: float  # 过去24小时内的交易量
    h6: float  # 过去6小时内的交易量
    h1: float  # 过去1小时内的交易量
    m5: float  # 过去5分钟内的交易量


class PriceChange(BaseModel):
    m5: float  # 过去5分钟内的价格变化百分比
    h1: float  # 过去1小时内的价格变化百分比
    h6: float  # 过去6小时内的价格变化百分比
    h24: float  # 过去24小时内的价格变化百分比


class Liquidity(BaseModel):
    usd: float  # 以美元计价的流动性
    base: int  # 基础代币的流动性数量
    quote: float  # 报价代币的流动性数量


class Info(BaseModel):
    imageUrl: str  # 代币的图片 URL
    header: str  # 代币的头部图片 URL
    openGraph: str  # 代币的 OpenGraph 图片 URL
    websites: List[Dict[str, str]]  # 代币相关的网站链接
    socials: List[Dict[str, str]]  # 代币相关的社交媒体链接


class MongoCoin(Document):
    chainId: str  # 区块链的 ID（例如：solana）
    dexId: str  # 去中心化交易所的 ID（例如：raydium）
    url: str  # 代币对的 DexScreener 页面 URL
    pairAddress: str  # 代币对的合约地址
    baseToken: BaseToken  # 基础代币的信息
    quoteToken: QuoteToken  # 报价代币的信息
    priceNative: str  # 以原生代币计价的价格
    priceUsd: str  # 以美元计价的价格
    txns: Txns  # 交易数据
    volume: Volume  # 交易量数据
    priceChange: PriceChange  # 价格变化数据
    liquidity: Liquidity  # 流动性数据
    fdv: int  # 完全稀释估值
    marketCap: int  # 市值
    pairCreatedAt: int  # 代币对创建的时间戳
    info: Info  # 代币的附加信息

    class Settings:
        name = "coins"
