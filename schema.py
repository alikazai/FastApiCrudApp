from pydantic import BaseModel

# UserBase class is a class on which other users class like UserCreate and User is based on
class UserBase(BaseModel):
    username: str


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
