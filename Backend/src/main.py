from typing import List
import datetime 

#Fastapi

from fastapi import Depends, FastAPI, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware


from sqlalchemy.orm import Session
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.sql.expression import column, false, true

#from . import crud, models, schemas
from . import crud, models, schemas
from . import cookie as cookies
from uuid import UUID
from .database import SessionLocal, engine
from .config import SQLALCHEMY_DATABASE_URL

#cookie - front

from fastapi_sessions.frontends.implementations import SessionCookie, CookieParameters

from . import config

cookie_params = CookieParameters()

## Uses UUID
cookie = SessionCookie(
    cookie_name="cookie",
    identifier="general_verifier",
    auto_error=True,
    secret_key=config.key,
    cookie_params=cookie_params,
)

# from .cookie import BasicVerifier,backend



verifier = cookies.BasicVerifier(
    identifier="general_verifier",
    auto_error=True,
    backend=cookies.backend,
    auth_http_exception=HTTPException(status_code=403, detail="invalid session"),
)

# main app
models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.get("/")
def root ():
    return {"message":"Welcome"}

@app.post("/register/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.post("/login/")
async def login_user(response:Response, from_data: schemas.UserLogin, db: Session = Depends(get_db) ):
    ## Auth
    db_user = crud.get_user_by_email(db, email=from_data.email)
    if db_user:
        if from_data.password != db_user.__dict__['hashed_passwd']:
            raise HTTPException(status_code=400, detail="密碼錯誤！")
    else:
        raise HTTPException(status_code=400, detail="查無此帳號")
    ## Cookie
    from uuid import uuid4
    session = uuid4()
    data = schemas.SessionData(username=db_user.__dict__['email'],expired=datetime.datetime.now() + datetime.timedelta(seconds=30))
    await cookies.backend.create(session, data)
    cookie.attach_to_response(response, session)
    ## return
    return HTTPException(status_code=200,detail="登入成功！")
        

@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
# event

@app.post ("/event/create/")
def create_event(event: schemas.EventCreate, db:Session = Depends(get_db)):
    if (crud.get_event_by_name):
        raise HTTPException(400,"活動名稱重複")
    return crud.create_event(db=db,event=event)

@app.get ("/events/{page_num}")
def get_events():
    return 0
# session route
# from uuid import uuid4
# @app.post("/create_session/{name}")
# async def create_session(name: str, response: Response):

#     session = uuid4()
#     data = schemas.SessionData(username=name,expired=datetime.datetime.now() + datetime.timedelta(seconds=30))
#     print (data)
#     await cookies.backend.create(session, data)
#     cookie.attach_to_response(response, session)
#     print (response.__dict__)
#     return f"created session for {name}"


@app.get("/whoami", dependencies=[Depends(cookie)])
async def whoami(session_data: schemas.SessionData = Depends(verifier)):
    if (datetime.datetime.now() > session_data.expired):
        raise HTTPException(status_code=400,detail="cookie expired,login agian")
    return session_data
    
@app.post("/delete_session")
async def del_session(response: Response, session_id: UUID = Depends(cookie)):
    await cookies.backend.delete(session_id)
    cookie.delete_from_response(response)
    return "deleted session"