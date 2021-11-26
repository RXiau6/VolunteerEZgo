from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Date
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(254), unique=True, index=True)
    nick_name = Column(String(32), unique=True)
    hashed_passwd = Column(String(60))
    birth = Column(Date)
    is_active = Column(Boolean, default=False)
