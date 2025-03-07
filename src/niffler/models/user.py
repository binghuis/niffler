from beanie import Document
from pydantic import Field


class User(Document):
    name: str = Field(max_length=50)
    age: int = Field(gt=0)
    email: str

    class Settings:
        name = "users"
