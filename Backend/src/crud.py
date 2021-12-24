from os import name
from pydantic import networks
from sqlalchemy import types
from sqlalchemy.orm import Session
import random,string,hashlib
from sqlalchemy.sql.expression import false, true

from sqlalchemy.sql.functions import mode
from . import models, schemas

def get_user(db: Session, user_id: int):
    m = db.query(models.User).filter(models.User.id == user_id).first()
    print (m.__dict__)
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):

    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    for m in db.query(models.User).offset(skip).limit(limit).all():
        print (m.__dict__)
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    new_salt = salt_gen()
    db_user = models.User(
        salt=new_salt,
        email=user.email, 
        hashed_passwd=user.password, 
        nick_name=user.nick_name, 
        birth=user.birth)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_event_by_name(db: Session, name: str):
    return db.query(models.Event).filter(models.Event.name == name).first()

def check_repeat (db: Session,payload: schemas.AttendBase):
    event_list = db.query(models.Attend).filter(models.Attend.event_id == payload.event_id).all()
    for i in range (len(event_list)):
        l2d = event_list[i].__dict__
        if (l2d["attend_id"] == payload.attend_id):
            return True
    return False

def user_auth(db: Session, user: schemas.UserLogin):
    if (db.query(models.User).filter(models.User.email != user.email)):
        print (db.query(models.User).filter(models.User.email).first())
        print (user.email)
        return True
    if (db.query(models.User).filter(models.User.hashed_passwd != user.password)):
        print (db.query(models.User).filter(models.User.hashed_passwd).first())
        print (user.password)
        return True
    return False

def create_event(db: Session,event:schemas.EventCreate):
    db_event = models.Event(
        types=event.types,
        name=event.name,
        description=event.description,
        # host_id="1",
        register_deadline=event.register_deadline,
        start_date=event.start_date,
        over_date=event.over_date,
        Auth_hour=event.Auth_hour,
        number_of_attendable=event.number_of_attendable
        )
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

def attend_event(db: Session,attend:schemas.AttendBase):
    db_attend = models.Attend(
        attend_id=attend.attend_id,
        event_id=attend.event_id
        )
    db.add(db_attend)
    db.commit()
    db.refresh(db_attend)
    return db_attend

def get_events(db: Session, skip: int = 0, limit: int = 12):
    return db.query(models.Event).offset(skip).limit(limit).all()

def salt_gen():
    letter = []
    for i in range(16):
        chars = random.choice(string.ascii_letters+string.digits)
        letter.append(chars)
    

    salt = ''.join(str(e) for e in letter)
    return salt

