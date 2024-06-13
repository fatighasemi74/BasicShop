from pydantic import BaseModel
from typing import List
from .enums import OrderStatus

class ProductItem(BaseModel):
    product_id: str
    quantity: int

class Order(BaseModel):
    order_id: str 
    user_id: int
    item_ids: List[ProductItem]
    total_cost: float
    status: OrderStatus = OrderStatus.PENDING 

    class Config:
        orm_mode = True
        use_enum_values = True


class CreateOrderRequest(BaseModel):
    user_id: int
    items: List[ProductItem]