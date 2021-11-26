from typing import List, Optional

from pydantic import BaseModel

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    nick_name: str
    birth: str
    password: str
    

class User(UserBase):
    id: int
    is_active: bool
    class Config:
        orm_mode = True