from pydantic import BaseModel, Field, validator
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


    @validator('order_id', pre=True, always=True)
    def convert_id(cls, v):
        return str(v)

    class Config:
        orm_mode = True
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: lambda oid: str(oid)  # Convert ObjectId to string for JSON responses
        }

class CreateOrderRequest(BaseModel):
    user_id: int
    items: List[ProductItem]