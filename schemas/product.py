from pydantic import BaseModel


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


    class Config:
        orm_mode = True
        use_enum_values = True
