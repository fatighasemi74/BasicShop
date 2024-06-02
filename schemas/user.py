from pydantic import BaseModel, EmailStr
from typing import Optional
from .enums import UserRole

class UserModel(BaseModel):
    user_id: int
    first_name: str
    last_name: str
    email: EmailStr
    email_verified: bool = False
    role: UserRole
    is_active: bool = True
    bio: Optional[str] = None