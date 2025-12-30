from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class ChangePassword(BaseModel):
    email: EmailStr
    old_password: str
    new_password: str

class UserProfile(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    createdat: datetime

    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
