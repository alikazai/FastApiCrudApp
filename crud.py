from sqlalchemy.orm import Session
from model import User as ModelUser
from schema import UserCreate as SchemaUser
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Optional
from fastapi_sqlalchemy import db

SECRET_KEY = "9d5cda2ad22cffab445fa761d221ed44820dda4a0c18ac4fad93394bfc0877e4"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(username: str):
    return db.session.query(ModelUser).filter(ModelUser.username == username).first()


def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def create_user(user: SchemaUser):
    db_user = ModelUser(
        username=user.username, password=get_password_hash(user.password)
    )
    db.session.add(db_user)
    db.session.commit()
    db.session.refresh(db_user)
    return db_user
