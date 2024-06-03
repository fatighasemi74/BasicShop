from pydantic import BaseModel, EmailStr, Field
from bson import ObjectId
from typing import Optional
from .enums import UserRole

class UserModel(BaseModel):
    user_id: str = Field(default_factory=lambda: str(ObjectId()), alias="_id")
    first_name: str
    last_name: str
    email: EmailStr
    email_verified: bool = False
    role: UserRole
    is_active: bool = True
    bio: Optional[str] = None

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str  # Convert ObjectId to string for JSON responses
        }
