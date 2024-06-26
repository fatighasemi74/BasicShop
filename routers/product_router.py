from fastapi import HTTPException, APIRouter, Depends, Path
from schemas.product import ProductCreateRequest, ProductModel
from use_cases.product_use_case import ProductUseCase
from .depends.product_depend import get_product_use_case
from database import InMemoryDatabase
from typing import List


router = APIRouter()

@router.post("/products/", status_code=201, response_model=ProductModel)
async def create_product(product_request: ProductCreateRequest, product_use_case: ProductUseCase = Depends(get_product_use_case)):
    try:
        product_id = await product_use_case.create_product(
            name=product_request.name,
            description=product_request.description,
            price=product_request.price,
            stock_quantity=product_request.stock_quantity
        )
        return ProductModel(
            product_id = product_id,
            name = product_request.name,
            description = product_request.description,
            price = product_request.price,
            stock_quantity = product_request.stock_quantity
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str)

@router.get("/products/", response_model=List[ProductModel], status_code=200)
async def get_products(product_use_case: ProductUseCase = Depends(get_product_use_case)):
    try:
        products = await product_use_case.get_products()
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@router.get("/products/{product_id}", response_model=ProductModel, status_code=200)
async def get_product_by_id(product_id: str, product_use_case: ProductUseCase = Depends(get_product_use_case)):
    try:
        product = await product_use_case.get_product_by_id(product_id)
        if not product:
            raise HTTPException(status_code=404, detail="product not found")
        return product
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))