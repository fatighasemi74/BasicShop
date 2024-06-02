from schemas.order import Order

class OrderService:
    def __init__(self, db):
        self.db = db

    async def create_order(self, user_id: int, product_id: int, quantity: int):
        # Use self.db for database operations
        order_document = {
            "user_id": user_id,
            "product_id": product_id,
            "quantity": quantity,
        }
        result = await self.db["orders"].insert_one(order_document)
        return result.inserted_id