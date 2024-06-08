from fastapi import HTTPException, APIRouter
from services.order_service import OrderService
from database import Database
from typing import List
from schemas.order import ProductItem, CreateOrderRequest  


router = APIRouter()



@router.post("/orders/")
async def create_order(order_request: CreateOrderRequest):
    db = Database.get_db()
    order_service = OrderService(db)
    try:
        order_id = await order_service.create_order(order_request.user_id, order_request.items)
        return {"order_id": order_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
