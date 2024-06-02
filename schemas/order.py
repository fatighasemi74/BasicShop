from pydantic import BaseModel
from typing import List
from .enums import OrderStatus


class Order(BaseModel):
    order_id: int
    user_id: int
    item_ids: List[int]
    total_cost: float
    status: OrderStatus = OrderStatus.PENDING 
