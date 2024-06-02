from pydantic import BaseModel, Field
from typing import List
from .enums import OrderStatus
from bson import ObjectId


class Order(BaseModel):
    order_id: int
    user_id: int
    item_ids: List[int]
    total_cost: float
    status: OrderStatus = OrderStatus.PENDING 
    quantity: int
    order_id: str = Field(default_factory=lambda: str(ObjectId()), alias="_id")

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str  # Convert ObjectId to string for JSON responses
        }
