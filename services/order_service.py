import uuid
from interfaces.iorder import IOrder
from typing import List
from schemas.order import ProductItem
from schemas.enums import OrderStatus



class OrderService(IOrder):
    def __init__(self, db):
        self.db = db
        if 'orders' not in self.db:
            self.db['orders'] = {}
        if 'products' not in self.db:
            self.db['products'] = {}

    async def create_order(self, user_id: int, items: List[ProductItem]):
        total_cost = 0
        item_data = []
        for item in items:
            product = self.db["products"].get(item.product_id)
            if not product:
                raise ValueError(f"product with id {item.product_id} not found.")
            if product['stock_quantity'] < item.quantity:
                raise ValueError(f"not enough stock for product id {item.product_id}")
            
            item_cost = product['price'] * item.quantity
            total_cost += item_cost

            item_cost = product['price'] * item.quantity
            total_cost += item_cost

            item_data.append({
                "product_id": item.product_id,
                "quantity": item.quantity,
                "cost": item_cost
            })
        order_id = str(uuid.uuid4())
        order_document = {
            "order_id": order_id,
            "user_id": user_id,
            "item_ids": item_data,
            "total_cost": total_cost,
            "status": OrderStatus.PENDING.value
        }

        self.db["orders"][order_id] = order_document
        return order_id


    async def get_orders(self):
        return list(self.db["orders"].values())

    async def get_order_by_id(self, order_id):
        return self.db["orders"].get(order_id)


    async def get_order_by_user(self, user_id):
        return [order for order in self.db["orders"].values() if order["user_id"] == user_id]

    async def get_order_by_product(self, product_id):
        return [order for order in self.db["orders"].values() if any(item["product_id"] == product_id for item in order["items"])]

    async def update_order_by_id(self, order_id, update_fields):
        if order_id in self.db["orders"]:
            self.db["orders"][order_id].update(update_fields)
            return True
        return False
    
    async def delete_order_by_id(self, order_id):
        if order_id in self.db["orders"]:
            del self.db["orders"][order_id]
            return True
        return False