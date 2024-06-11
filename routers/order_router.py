from fastapi import HTTPException, APIRouter, Depends, Path
from services.order_service import OrderService
from database import InMemoryDatabase
from typing import List
from schemas.order import ProductItem, CreateOrderRequest, Order  
from use_cases.order_use_case import OrderUseCase


router = APIRouter()



@router.post("/orders/", status_code=201)
async def create_order(order_request: CreateOrderRequest):
    db = InMemoryDatabase.get_db()
    order_service = OrderService(db)
    try:
        order_id = await order_service.create_order(order_request.user_id, order_request.items)
        return {"order_id": order_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/orders/", response_model=List[Order], status_code=200)
async def get_orders(db=Depends(InMemoryDatabase.get_db)):
    order_use_case = OrderUseCase(db)
    try:
        orders = await order_use_case.get_orders()
        return orders
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/orders/{order_id}", response_model=Order, status_code=200)
async def get_order_by_id(order_id: str = Path(..., description="The ID of the order to retrieve"), db=Depends(InMemoryDatabase.get_db)):
    order_use_case = OrderUseCase(db)
    try:
        order = await order_use_case.get_order_by_id(order_id)
        if not order:
            raise HTTPException(status_code=404, detail="order not found")
        return order
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
