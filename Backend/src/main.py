from typing import List
import datetime 

#Fastapi

from fastapi import Depends, FastAPI, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware


from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import column

#from . import crud, models, schemas
from . import crud, models, schemas
from .database import SessionLocal, engine
from .config import SQLALCHEMY_DATABASE_URL

#cookie - front

from fastapi_sessions.frontends.implementations import SessionCookie, CookieParameters

cookie_params = CookieParameters()

## Uses UUID
cookie = SessionCookie(
    cookie_name="cookie",
    identifier="general_verifier",
    auto_error=True,
    secret_key="DONOTUSE",
    cookie_params=cookie_params,
)


#session -backend 
from uuid import UUID
from fastapi_sessions.backends.implementations import InMemoryBackend

backend = InMemoryBackend[UUID, schemas.SessionData]()

#session BasicVerifier
from fastapi_sessions.session_verifier import SessionVerifier
from fastapi import HTTPException

class BasicVerifier(SessionVerifier[UUID, schemas.SessionData]):
    def __init__(
        self,
        *,
        identifier: str,
        auto_error: bool,
        backend: InMemoryBackend[UUID, schemas.SessionData],
        auth_http_exception: HTTPException,
    ):
        self._identifier = identifier
        self._auto_error = auto_error
        self._backend = backend
        self._auth_http_exception = auth_http_exception

    @property
    def identifier(self):
        return self._identifier

    @property
    def backend(self):
        return self._backend

    @property
    def auto_error(self):
        return self._auto_error

    @property
    def auth_http_exception(self):
        return self._auth_http_exception

    def verify_session(self, model: schemas.SessionData) -> bool:
        """If the session exists, it is valid"""
        return True


verifier = BasicVerifier(
    identifier="general_verifier",
    auto_error=True,
    backend=backend,
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
def login_user(from_data: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=from_data.email)
    if db_user:
        if from_data.password != db_user.__dict__['hashed_passwd']:
            raise HTTPException(status_code=400, detail="密碼錯誤！")
    else:
        raise HTTPException(status_code=400, detail="查無此帳號")
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

# @app.post ("/event/create/")
# def create_event(db:Session = Depends(get_db), event: schemas.EventCreate):
    
# session route
from uuid import uuid4
@app.post("/create_session/{name}")
async def create_session(name: str, response: Response):

    session = uuid4()
    data = schemas.SessionData(username=name,expired=datetime.datetime.now() + datetime.timedelta(seconds=30))

    await backend.create(session, data)
    cookie.attach_to_response(response, session)

    return f"created session for {name}"


@app.get("/whoami", dependencies=[Depends(cookie)])
async def whoami(session_data: schemas.SessionData = Depends(verifier)):
    if (datetime.datetime.now() > session_data.expired):
        raise HTTPException(status_code=400,detail="cookie expired,login agian")
    return session_data


@app.post("/delete_session")
async def del_session(response: Response, session_id: UUID = Depends(cookie)):
    await backend.delete(session_id)
    cookie.delete_from_response(response)
    return "deleted session"