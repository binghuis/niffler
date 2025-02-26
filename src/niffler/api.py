from functools import lru_cache


class Apis:
    top_coin_from_dexscreener = "https://api.dexscreener.com/token-boosts/top/v1"
    latest_coin_from_dexscreener = "https://api.dexscreener.com/token-boosts/latest/v1"
    coin_detail_from_dexscreener = "https://api.dexscreener.com/token-pairs/v1/"


@lru_cache
def get_apis():
    return Apis()
