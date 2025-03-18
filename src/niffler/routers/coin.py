from fastapi import APIRouter

from niffler.services.coin import ServiceCoin

router = APIRouter(prefix="/coin", tags=["coins"])


@router.get("/")
async def list_coins():
    return await ServiceCoin.get_all()


@router.get("/save")
async def save_coin():
    return await ServiceCoin.save("Bitcoin", "BTC")


@router.get("/list")
async def get_coin():
    return await ServiceCoin.get_by_id("61f8b2a6b5b4f5f4b4b4b4b4")


@router.get("/update")
async def update_coin():
    return await ServiceCoin.update(
        "61f8b2a6b5b4f5f4b4b4b4b4", name="Bitcoin", symbol="BTC"
    )
