from beanie import Document
from pydantic import Field


class User(Document):
    username: str = Field(max_length=50)
    userpassword: str = Field(max_length=50)

    class Settings:
        name = "users"
