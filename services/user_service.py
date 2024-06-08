from pydantic import EmailStr
from bson import ObjectId
from typing import Optional
from schemas.enums import UserRole

class UserService:
    def __init__(self, db):
        self.db = db

    async def create_user(self, first_name: str, last_name: str, email: EmailStr, role: UserRole, bio: Optional[str] = None):
        user_document = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "email_verified": False,  
            "role": role.value,  
            "is_active": True, 
            "bio": bio
        }
        result = await self.db["user"].insert_one(user_document)
        return str(result.inserted_id)  

    async def get_user_by_id(self, user_id):
        user = await self.db["user"].find_one({"_id": ObjectId(user_id)})
        if user:
            user['user_id'] = user.pop('_id')
        return user

    async def get_users(self):
        cursor = self.db["user"].find({})
        users = await cursor.to_list(length=None)
        return users

    async def update_user_by_id(self, user_id, update_fields):
        result = await self.db["user"].update_one(
            {"_id": ObjectId(user_id)},
            {"$set": update_fields}
        )
        return result.modified_count > 0

    async def delete_user_by_id(self, user_id):
        result = await self.db["user"].delete_one({"_id": ObjectId(user_id)})
        return result.deleted_count > 0

    async def set_user_active_status(self, user_id, is_active: bool):
        result = await self.db["user"].update_one(
            {"_id": ObjectId(user_id)},
            {"$set": {"is_active": is_active}}
        )
        return result.modified_count > 0

    async def verify_user_email(self, user_id):
        result = await self.db["user"].update_one(
            {"_id": ObjectId(user_id)},
            {"$set": {"email_verified": True}}
        )
        return result.modified_count > 0