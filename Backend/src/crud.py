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
<<<<<<< HEAD
    salt = salt_gen()
    
    fake_hashed_password = user.password + salt
    db_user = models.User(email=user.email, hashed_passwd=fake_hashed_password)
=======
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_passwd=fake_hashed_password, nick_name=user.nick_name, birth=user.birth)
>>>>>>> 079dcd78ae1e1f0ce1bec321584ccef6c0b3852a
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def salt_gen():
    letter = []
    for i in range(1,16):
        chars = random.choice(string.ascii_letters+string.digits)
        letter.append(chars)
    

    salt = ''.join(str(e) for e in letter)
    return salt

def hashing():
    