from datetime import timedelta, datetime, timezone
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status,Request
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from pydantic import BaseModel
from database import SessionLocal
from models import Users
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer
from jose import jwt, JWTError
from fastapi.templating import Jinja2Templates
from config import settings

router = APIRouter(prefix="/auth", tags=["Auth"])

SECRET_KEY = settings.JWT_SECRET
ALGORITHM = settings.JWT_ALGORITHM

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
templates= Jinja2Templates(directory="templates")

## PAGES ###

@router.get('/login-page')
def render_login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.get('/register-page')
def render_register_page(request:Request):
    return templates.TemplateResponse("register.html",{"request": request})


###------###
class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str
    phone_number: str

class Token(BaseModel):
    access_token: str
    token_type: str


### ENDPOINTS ###
def authenticate_user(username: str, password: str,db) :
    user = db.query(Users).filter(Users.username ==username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password,user.hashed_password):
        return False
    return user

def create_access_token(username:str , user_id :int ,role:str, expires_delta : timedelta):
    encode = {'sub':username, 'id':user_id,'role':role}
    expires = datetime.now(timezone.utc) + expires_delta
    encode.update({'exp':expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


async def get_current_user(token:Annotated[str,Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id = payload.get("id")
        user_role :str =payload.get("role")
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Could not validate user")
        return {'username': username, 'id': user_id,'role': user_role}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user")



@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, request: CreateUserRequest):

    user = Users(
        username=request.username,
        email=request.email,
        first_name=request.first_name,
        last_name=request.last_name,
        hashed_password=bcrypt_context.hash(request.password),
        role=request.role,
        is_active=True,
        phone_number=request.phone_number
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return "Successfully created new user"


@router.post("/token",response_model=Token)
async def login_for_access_token(form_data : Annotated[OAuth2PasswordRequestForm,Depends()],db: db_dependency,):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )

    user_obj = db.query(Users).filter(Users.username == form_data.username).first()

    token = create_access_token(
        username=user.username,
        user_id=user.id,
        role=user.role,
        expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {'access_token': token, 'token_type': 'bearer'}