from typing import Optional
from pydantic import BaseModel

# UserBase class is a class on which other users class like UserCreate and User is based on
class UserBase(BaseModel):
    username: str
    is_active: Optional[str] = None


# UserCreate is used for validation and sending data to the server
class UserCreate(UserBase):
    first_name: str
    last_name: str
    email: str
    password: str


# User to send values and rows from the database.
class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
