from fastapi import HTTPException, APIRouter, Depends, Body
from schemas.user import UserCreateRequest, UserModel
from use_cases.user_use_case import UserUseCase

from database import Database

router = APIRouter()

@router.post("/users/", response_model=UserModel, status_code=201)
async def create_user(user_request: UserCreateRequest, db=Depends(Database.get_db)):
    user_use_case = UserUseCase(db)
    try:
        user_id = await user_use_case.place_order(**user_request.dict())
        return {
            **user_request.dict(),
            "user_id": user_id,
            "email_verified": False,
            "is_active": True
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))