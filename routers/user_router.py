from fastapi import HTTPException, APIRouter, Depends
from schemas.user import UserCreateRequest, UserModel, LoginRequest
from use_cases.user_use_case import UserUseCase
from .depends.user_depend import get_user_use_case
from typing import List
from security.auth_utils import create_access_token

router = APIRouter()

@router.post("/users/", response_model=UserModel, status_code=201)
async def create_user(user_request: UserCreateRequest, user_use_case: UserUseCase = Depends(get_user_use_case)):
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
async def get_users(user_use_case: UserUseCase = Depends(get_user_use_case)):
    try:
        users = await user_use_case.get_users()
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/users/{user_id}", response_model=UserModel, status_code=200)
async def get_user_by_id(user_id: str, user_use_case: UserUseCase = Depends(get_user_use_case)):
    try:
        user = await user_use_case.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/login")
async def login(login_request: LoginRequest, user_use_case: UserUseCase = Depends(get_user_use_case)):
    try:
        user = await user_use_case.authenticate_user(login_request.email, login_request.password)
        if user:
            access_token = create_access_token(data={"user_id": user["user_id"]})
            return {"access_token": access_token, "token_type": "bearer"}
        else:
            raise HTTPException(status_code=401, detail="Invalid email or password")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))