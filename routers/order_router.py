from fastapi import HTTPException, APIRouter
from services.order_service import OrderService
from database import Database

router = APIRouter()



@router.post("/orders/")
async def create_order(user_id: int, product_id: int, quantity: int):
    db = Database.get_db()
    order_service = OrderService(db)
    try:
        order = await order_service.create_order(user_id, product_id, quantity)
        return order
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
