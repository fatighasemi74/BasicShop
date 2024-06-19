from services.order_service import OrderService
from interfaces.iorder import IOrder
from schemas.order import ProductItem
from typing import List, Dict

class OrderUseCase:
    def __init__(self, order_service: IOrder):
        self.order_service = order_service

    async def create_order(self, user_id: str, items: List[ProductItem]) -> str:
        return await self.order_service.create_order(user_id, items)

    async def get_orders(self) -> List[Dict]:
        orders = await self.order_service.get_orders()
        return orders

    async def get_order_by_id(self, order_id: str) -> dict:
        order = await self.order_service.get_order_by_id(order_id)
        return order
