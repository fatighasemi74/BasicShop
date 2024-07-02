from pydantic import BaseModel, EmailStr
from typing import Optional
from .enums import UserRole

class UserCreateRequest(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    role: UserRole
    password: str
    bio: Optional[str] = None

class UserModel(BaseModel):
    user_id: str 
    first_name: str
    last_name: str
    email: EmailStr
    email_verified: bool = False
    role: UserRole
    is_active: bool = True
    bio: Optional[str] = None

    class Config:
        orm_mode = True
        use_enum_values = True


class LoginRequest(BaseModel):
    email: EmailStr
    password: str