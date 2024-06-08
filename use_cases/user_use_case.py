from services.user_service import UserService
from schemas.user import UserRole
from typing import Optional
from database import Database

class UserUseCase:
    def __init__(self, db):
        self.user_service = UserService(db)

    async def place_order(self, first_name: str, last_name: str, email: str, role: UserRole, bio: Optional[str] = None):
        user_id = await self.user_service.create_user(first_name, last_name, email, role, bio)
        return user_id