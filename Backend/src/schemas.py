import datetime
from typing import List, Optional

from sqlalchemy.sql.sqltypes import String

from pydantic import BaseModel

from .database import Base

class SessionData (BaseModel):
    username: str
    expired: datetime.datetime

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    nick_name: str
    birth: str
    password: str

class UserLogin(UserBase):
    password: str
    

class User(UserBase):
    id: int
    is_active: bool
    class Config:
        orm_mode = True

class EventBase(BaseModel):
    name: str

class EventCreate(EventBase):
    types: str
    description: str
    register_deadline: str
    Auth_hour: float
    start_date: str
    over_date: str
    number_of_attendable: int
    host_id: str


class Event(EventBase):
    id: int
    # host_id: int
    number_of_registerd: int

class AttendAuth(UserBase):
    password: str
    event_id: int

class AttendBase(BaseModel):
    attend_id: int
    event_id: int
    
class Attend(AttendBase):
    id: int