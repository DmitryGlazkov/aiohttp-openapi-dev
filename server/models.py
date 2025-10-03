from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    name: str = Field(min_length=1, max_length=50)


class User(BaseModel):
    id: int
    name: str
