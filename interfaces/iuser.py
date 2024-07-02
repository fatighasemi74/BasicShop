from abc import ABC, abstractmethod
from pydantic import EmailStr
from typing import Optional, Dict, List
from schemas.enums import UserRole

class IUser(ABC):
    @abstractmethod
    async def create_user(self, first_name: str, last_name: str, email: EmailStr, role: UserRole, password: str, bio: Optional[str] = None) -> str:
        pass

    @abstractmethod
    async def get_user_by_id(self, user_id: str) -> Optional[Dict]:
        pass

    @abstractmethod
    async def get_users(self) -> List[Dict]:
        pass

    @abstractmethod
    async def update_user_by_id(self, user_id: str, update_fields: Dict) -> bool:
        pass

    @abstractmethod
    async def delete_user_by_id(self, user_id: str) -> bool:
        pass

    @abstractmethod
    async def set_user_active_status(self, user_id: str, is_active: bool) -> bool:
        pass

    @abstractmethod
    async def verify_user_email(self, user_id: str) -> bool:
        pass