from pydantic import networks
from sqlalchemy.orm import Session
import random,string,hashlib
from . import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    new_salt = salt_gen()
    # password = user.password + new_salt
    db_user = models.User(salt=new_salt,email=user.email, hashed_passwd=user.password, nick_name=user.nick_name, birth=user.birth)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# def check_user(db: Session, user: schemas.User):

def salt_gen():
    letter = []
    for i in range(16):
        chars = random.choice(string.ascii_letters+string.digits)
        letter.append(chars)
    

    salt = ''.join(str(e) for e in letter)
    return salt

# def check_password(db: Session, ):
