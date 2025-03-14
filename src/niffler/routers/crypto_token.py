from fastapi import APIRouter

from niffler.services.crypto_token import CryptoTokenService

router = APIRouter(prefix="/crypto_token", tags=["crypto_token"])


@router.get("/")
async def list_crypto_tokens():
    return await CryptoTokenService.get_all_tokens()


@router.get("/save")
async def save_crypto_token():
    return await CryptoTokenService.save_token("Bitcoin", "BTC")


@router.get("/get")
async def get_crypto_token():
    return await CryptoTokenService.get_token_by_id("61f8b2a6b5b4f5f4b4b4b4b4")


@router.get("/update")
async def update_crypto_token():
    return await CryptoTokenService.update_token(
        "61f8b2a6b5b4f5f4b4b4b4b4", name="Bitcoin", symbol="BTC"
    )
