from bson import ObjectId
from pydantic import BaseModel, Field

class ProductModel(BaseModel):
    product_id: str = Field(default_factory=lambda: str(ObjectId()), alias="_id")
    name: str
    description: str
    price: float
    stock_quantity: int


    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str  # Convert ObjectId to string for JSON responses
        }
