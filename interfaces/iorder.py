from abc import ABC, abstractmethod
from typing import List, Dict, Optional
from schemas.order import ProductItem

class IOrder(ABC):
    @abstractmethod
    async def create_order(self, user_id: int, items: List[ProductItem]) -> str:
        pass

    @abstractmethod
    async def get_orders(self) -> List[Dict]:
        pass

    @abstractmethod
    async def get_order_by_id(self, order_id: str) -> Optional[Dict]:
        pass

    @abstractmethod
    async def get_order_by_user(self, user_id: str) -> List[Dict]:
        pass

    @abstractmethod
    async def get_order_by_product(self, product_id: str) -> List[Dict]:
        pass

    @abstractmethod
    async def update_order_by_id(self, order_id: str, update_fields: Dict) -> bool:
        pass

    @abstractmethod
    async def delete_order_by_id(self, order_id: str) -> bool:
        pass