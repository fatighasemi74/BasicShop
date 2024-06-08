from services.product_service import ProductService
from database import Database

class ProductUseCase:
    def __init__(self, db):
        self.product_service = ProductService(db)

    async def place_order(self, name: str, description: str, price: float, stock_quantity: int):
        product_id = await self.product_service.create_product(name, description, price, stock_quantity)
        return product_id