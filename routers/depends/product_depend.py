from fastapi import Depends
from services.product_service import ProductService
from use_cases.product_use_case import ProductUseCase
from database import InMemoryDatabase

def get_product_use_case(db=Depends(InMemoryDatabase.get_db)) -> ProductUseCase:
    product_service = ProductService(db)
    return ProductUseCase(product_service)