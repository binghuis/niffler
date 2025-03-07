from niffler.models.user import User


async def get_all_users(skip: int, limit: int):
    return await User.find().skip(skip).limit(limit).to_list()
