from services.order_service import OrderService

class OrderUseCase:
    def __init__(self, db):
        self.order_service = OrderService(db)

    def create_order(self, user_id, items):
        return self.order_service.create_order(user_id, items)

    async def get_orders(self):
        products = await self.order_service.get_orders()
        return products

    async def get_order_by_id(self, order_id: str):
        order = await self.order_service.get_order_by_id(order_id)
        return order
