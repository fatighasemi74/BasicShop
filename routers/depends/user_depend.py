from fastapi import Depends
from services.user_service import UserService
from use_cases.user_use_case import UserUseCase
from database import InMemoryDatabase

def get_user_use_case(db=Depends(InMemoryDatabase.get_db)) -> UserUseCase:
    user_service = UserService(db)
    return UserUseCase(user_service)