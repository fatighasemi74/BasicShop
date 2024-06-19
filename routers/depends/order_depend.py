from fastapi import Depends
from database import InMemoryDatabase
from use_cases.order_use_case import OrderUseCase
from services.order_service import OrderService


def get_order_use_case(db=Depends(InMemoryDatabase.get_db)) -> OrderUseCase:
    order_service = OrderService(db)
    return OrderUseCase(order_service)