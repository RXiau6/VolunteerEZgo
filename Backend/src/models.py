
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, DateTime, Time, Float
from sqlalchemy.orm import relation, relationship

from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(254), unique=True, index=True)
    nick_name = Column(String(32), unique=True)
    hashed_passwd = Column(String(60))
    birth = Column(Date)
    is_active = Column(Boolean, default=False)
    salt = Column(String(16))

    Event = relationship("Event", back_populates="User")
    Attend = relationship("Attend", back_populates="User")

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    types = Column(String(10))
    name = Column(String(128))
    description = Column(String(1024))
    host_id = Column(String(254), ForeignKey('users.email'))
    register_deadline = Column(DateTime)
    start_date = Column(DateTime)
    over_date = Column(DateTime)
    # during_time = Column(String(50))
    Auth_hour = Column(Float)
    number_of_attendable = Column(Integer)
    number_of_registerd = Column(Integer,default=0)

    Attend = relationship("Attend", back_populates="Event")
    User = relationship("User", back_populates="Event")

class Attend(Base):
    __tablename__ = "attend"

    id = Column(Integer, primary_key=True, index=True)
    attend_id = Column(Integer, ForeignKey('users.id'))
    event_id = Column(Integer, ForeignKey('events.id'))

    User = relationship("User",back_populates="Attend")
    Event = relationship("Event",back_populates="Attend")