from random import random
import os
from passlib.context import CryptContext
from jose import jwt
from jose.exceptions import JOSEError
from fastapi import HTTPException, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from decouple import config

SECRET = config('SECRET')
ALGORITHM = config('ALGORITHM')

class AuthUtils:
    '''Token needs to implement exp date'''
    def __init__(self):
        self.password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.JWT_ALGORITHM = ALGORITHM
        self.JWT_SECRET_KEY = SECRET


    async def get_hashed_password(self, password:str) -> str:
        return self.password_context.hash(password)

    async def verify_password(self, password:str, hashed_password:str)-> bool:
        return self.password_context.verify(password, hashed_password)

    async def create_access_token(self, subject:str) -> str:
        to_encode = {"sub": subject}
        encoded_jwt = jwt.encode(to_encode, self.JWT_SECRET_KEY, self.JWT_ALGORITHM)
        return encoded_jwt
    
    async def validate_access_token(self, credentials: HTTPAuthorizationCredentials=Depends(HTTPBearer())):
        token = credentials.credentials

        try:
            payload = jwt.decode(token, self.JWT_SECRET_KEY, algorithms=[self.JWT_ALGORITHM])
    
            print("payload: ", payload)
        except JOSEError as e:
            raise HTTPException(
                status_code=401,
                detail=str(e)
            )
        return payload

authUtils = AuthUtils()