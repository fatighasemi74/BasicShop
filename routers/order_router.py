from fastapi import HTTPException, APIRouter, Depends, Path
from services.order_service import OrderService
from database import InMemoryDatabase
from typing import List
from schemas.order import CreateOrderRequest, Order  
from use_cases.order_use_case import OrderUseCase
from .depends.order_depend import get_order_use_case


router = APIRouter()



@router.post("/orders/", status_code=201)
async def create_order(order_request: CreateOrderRequest, order_use_case: OrderUseCase = Depends(get_order_use_case)):
    try:
        order_id = await order_use_case.create_order(order_request.user_id, order_request.items)
        order_details = await order_use_case.get_order_by_id(order_id)
        # return {"order_id": order_id}
        if not order_details:
            raise HTTPException(status_code=404, detail="Order not found")
        return order_details
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/orders/", response_model=List[Order], status_code=200)
async def get_orders(order_use_case: OrderUseCase = Depends(get_order_use_case)):
    try:
        orders = await order_use_case.get_orders()
        return orders
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/orders/{order_id}", response_model=Order, status_code=200)
async def get_order_by_id(order_id: str, order_use_case: OrderUseCase = Depends(get_order_use_case)):
    try:
        order = await order_use_case.get_order_by_id(order_id)
        if not order:
            raise HTTPException(status_code=404, detail="order not found")
        return order
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
