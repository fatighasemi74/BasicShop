from pydantic import BaseModel

class ProductModel(BaseModel):
    product_id: int
    name: str
    description: str
    price: float
    stock_quantity: int