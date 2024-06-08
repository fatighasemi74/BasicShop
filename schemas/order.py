from pydantic import BaseModel, Field
from typing import List
from .enums import OrderStatus
from bson import ObjectId

class ProductItem(BaseModel):
    product_id: str
    quantity: int

class Order(BaseModel):
    order_id: str = Field(default_factory=lambda: str(ObjectId()), alias="_id")
    user_id: int
    item_ids: List[ProductItem]
    total_cost: float
    status: OrderStatus = OrderStatus.PENDING 
    # quantity: int

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str  # Convert ObjectId to string for JSON responses
        }

class CreateOrderRequest(BaseModel):
    user_id: int
    items: List[ProductItem]