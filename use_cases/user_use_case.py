from services.user_service import UserService
from schemas.user import UserRole
from typing import Optional
from interfaces.iuser import IUser

class UserUseCase:
    def __init__(self, user_service: IUser):
        self.user_service = user_service

    async def create_user(self, first_name: str, last_name: str, email: str, role: UserRole, bio: Optional[str] = None):
        user_id = await self.user_service.create_user(first_name, last_name, email, role, bio)
        return user_id

    async def get_users(self):
        users = await self.user_service.get_users()
        return users
    
    async def get_user_by_id(self, user_id: str):
        user = await self.user_service.get_user_by_id(user_id)
        return user