from fastapi import HTTPException, APIRouter, Depends, Body, Path
from schemas.user import UserCreateRequest, UserModel
from use_cases.user_use_case import UserUseCase
from typing import List

from database import InMemoryDatabase

router = APIRouter()

@router.post("/users/", response_model=UserModel, status_code=201)
async def create_user(user_request: UserCreateRequest, db=Depends(InMemoryDatabase.get_db)):
    user_use_case = UserUseCase(db)
    try:
        user_id = await user_use_case.create_user(**user_request.dict())
        return {
            **user_request.dict(),
            "user_id": user_id,
            "email_verified": False,
            "is_active": True
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/users/", response_model=List[UserModel], status_code=200)
async def get_users(db=Depends(InMemoryDatabase.get_db)):
    user_use_case = UserUseCase(db)
    try:
        users = await user_use_case.get_users()
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/users/{user_id}", response_model=UserModel, status_code=200)
async def get_user_by_id(user_id: str = Path(..., description="The ID of the user to retrieve"), db=Depends(InMemoryDatabase.get_db)):
    user_use_case = UserUseCase(db)
    try:
        user = await user_use_case.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))