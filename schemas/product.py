from bson import ObjectId
from pydantic import BaseModel, Field, validator


class ProductCreateRequest(BaseModel):
    name: str
    description: str
    price: float
    stock_quantity: int

class ProductModel(BaseModel):
    product_id: str 
    name: str
    description: str
    price: float
    stock_quantity: int

    @validator('product_id', pre=True, always=True)
    def convert_id(cls, v):
        return str(v)


    class Config:
        orm_mode = True
        use_enum_values = True
