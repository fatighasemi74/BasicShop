from bson import ObjectId
from typing import List
from schemas.order import ProductItem
from schemas.enums import OrderStatus



class OrderService:
    def __init__(self, db):
        self.db = db

    async def create_order(self, user_id: int, items: List[ProductItem]):
        total_cost = 0
        item_data = []
        for item in items:
            product = await self.db["product"].find_one({"_id": ObjectId(item.product_id)})
            print(product)
            if not product:
                raise ValueError(f"product with id {item.product_id} not found.")
            if product['stock_quantity'] < item.quantity:
                raise ValueError(f"not enough stock for product id {item.product_id}")
            
            item_cost = product['price'] * item.quantity
            total_cost += item_cost

            await self.db["product"].update_one(
                {"_id": item.product_id},
                {"$inc": {"stock_quantity": -item.quantity}}
            )

            item_data.append({
                "product_id": item.product_id,
                "quantity": item.quantity,
                "cost": item_cost
            })
        
        order_document = {
            "user_id": user_id,
            "item_ids": item_data,
            "total_cost": total_cost,
            "status": OrderStatus.PENDING.value
        }

        result = await self.db["order"].insert_one(order_document)
        return str(result.inserted_id)


    async def get_orders(self):
        cursor = self.db["order"].find({})
        orders = await cursor.to_list(length=None)
        return orders

    async def get_product_by_id(self, order_id):
        order = await self.db["orders"].find_one({"_id": ObjectId(order_id)})
        return order

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