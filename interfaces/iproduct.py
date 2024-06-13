from abc import ABC, abstractmethod
from typing import Optional, Dict, List

class IProduct(ABC):
    @abstractmethod
    async def create_product(self, name: str, description: str, price: float, stock_quantity: int) -> str:
        pass

    @abstractmethod
    async def get_product_by_id(self, product_id: str) -> Optional[Dict]:
        pass

    @abstractmethod
    async def get_products(self) -> List[Dict]:
        pass

    @abstractmethod
    async def update_product_by_id(self, product_id: str, update_fields: Dict) -> bool:
        pass

    @abstractmethod
    async def delete_product_by_id(self, product_id: str) -> bool:
        pass
