from interfaces.iproduct import IProduct

class ProductUseCase:
    def __init__(self, product_service:IProduct):
        self.product_service = product_service

    async def create_product(self, name: str, description: str, price: float, stock_quantity: int):
        product_id = await self.product_service.create_product(name, description, price, stock_quantity)
        return product_id
    
    async def get_products(self):
        products = await self.product_service.get_products()
        return products

    async def get_product_by_id(self, product_id: str):
        product = await self.product_service.get_product_by_id(product_id)
        return product