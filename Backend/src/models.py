from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, DateTime, Time, Float
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(254), unique=True, index=True)
    nick_name = Column(String(32), unique=True)
    hashed_passwd = Column(String(60))
    birth = Column(Date)
    is_active = Column(Boolean, default=False)

    event = relationship("Event")
class Category(Base):
    __tablename__ = "category"
    id = Column(Integer,primary_key=True, index=True)
    name = Column(String(20))
    hold_place = Column(String(10))
    
    event = relationship("Event")
class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    types = Column(String, ForeignKey('category.name'))
    name = Column(String(128))
    description = Column(String(1024))
    host_id = Column(Integer, ForeignKey('user.id'))
    register_deadline = Column(DateTime)
    start_date = Column(DateTime)
    over_date = Column(DateTime)
    during_time = Column(Time)
    Auth_hour = Column(Float)
    number_of_attendable = Column(Integer)
    number_of_registerd = Column(Integer)


