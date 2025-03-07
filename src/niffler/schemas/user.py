from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    age: int
    email: str


class UserResponse(BaseModel):
    id: str
    name: str
    age: int
