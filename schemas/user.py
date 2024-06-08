from pydantic import BaseModel, EmailStr, Field, validator
from bson import ObjectId
from typing import Optional
from .enums import UserRole

class UserCreateRequest(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    role: UserRole
    bio: Optional[str] = None

class UserModel(BaseModel):
    user_id: str = Field(default_factory=lambda: str(ObjectId()), alias="_id")
    first_name: str
    last_name: str
    email: EmailStr
    email_verified: bool = False
    role: UserRole
    is_active: bool = True
    bio: Optional[str] = None

    @validator('user_id', pre=True, always=True)
    def convert_id(cls, v):
        return str(v)

    class Config:
        orm_mode = True
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: lambda oid: str(oid)  # Convert ObjectId to string for JSON responses
        }
