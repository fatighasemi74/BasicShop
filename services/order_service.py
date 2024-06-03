from schemas.order import Order

class OrderService:
    def __init__(self, db):
        self.db = db

    async def create_order(self, user_id: int, product_id: int, quantity: int):
        order_document = {
            "user_id": user_id,
            "product_id": product_id,
            "quantity": quantity,
        }
        result = await self.db["orders"].insert_one(order_document)
        return result.inserted_id

    async def get_order(self):
        cursor = self.db["orders"].find({})
        orders = await cursor.to_list(length=None)
        return orders
    
    async def get_order_by_user(self, user_id):
        cursor = self.db["orders"].find({"user_id": user_id})
        orders = await cursor.to_list(length=None)
        return orders

    async def get_order_by_product(self, product_id):
        cursor = self.db["orders"].find({"product_id": product_id})
        orders = await cursor.to_list(length=None)
        return orders
    
    async def update_order_by_id(self, order_id, update_fields):
        result = await self.db["orders"].update_one(
            {"_id": order_id},
            {"$set": update_fields}
        )
        if result.modified_count:
            return True
        else:
            return False
    
    async def delete_order_by_id(self, order_id):
        result = await self.db["orders"].delete_one({"_id": order_id})
        if result.deleted_count:
            return True  
        else:
            return False