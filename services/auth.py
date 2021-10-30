from passlib.hash import bcrypt
from jose import jwt, JWTError
from pydantic import ValidationError

from fastapi import (
    HTTPException, 
    status,
    Depends
)

from ..models.auth import User, Token
from ..settings import settings
from .. import tables

from datetime import datetime, timedelta


class AuthService:
    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        return bcrypt.verify(plain_password, hashed_password)
    
    @classmethod
    def hashed_password(cls, password: str) -> str:
        return bcrypt.hash(password)

    @classmethod
    def validate_token(cls, token: str) -> User:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={
                'WWW-Authenticate': 'Bearer'
            }
        )
        
        try:
            payload = jwt.decode(
                token,
                settings.jwt_secret,
                algorithms=[settings.jwt_algorithm]
            )
        except JWTError:
            raise exception from None
        
        user_data = payload.get('user')

        try:
            user = User.parse_obj(user_data)
        except ValidationError:
            raise exception from None

        return user
    
    @classmethod
    def create_token(cls, user: tables.User) -> Token:
        user_data = User.from_orm(user)

        now = datetime.now()
        payload = {
            "iat": now,
            "nbf": now,
            "exp": now + timedelta(seconds=settings.jwt_expiration),
            "sub": str(user_data.id),
            "user": user_data.dict()
        }
        token = jwt.encode(
             payload,
             settings.jwt_secret,
             algorithms=settings.jwt_algorithm
        )
 
        return Token(access_token=token)

