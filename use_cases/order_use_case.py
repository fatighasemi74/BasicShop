from services.order_service import OrderService

class OrderUseCase:
    def __init__(self):
        self.order_service = OrderService()

    def place_order(self, user_id, product_id, quantity):
        return self.order_service.create_order(user_id, product_id, quantity)