from fastapi import HTTPException, APIRouter, Depends, Body
from schemas.product import ProductCreateRequest, ProductModel
from use_cases.product_use_case import ProductUseCase
from database import Database

router = APIRouter()

@router.post("/products/", status_code=201, response_model=ProductModel)
async def create_product(product_request: ProductCreateRequest, db = Depends(Database.get_db)):
    product_use_case = ProductUseCase(db)
    try:
        product_id = await product_use_case.place_order(
            name=product_request.name,
            description=product_request.description,
            price=product_request.price,
            stock_quantity=product_request.stock_quantity
        )
        return {
            "product_id": product_id,
            "name": product_request.name,
            "description": product_request.description,
            "price": product_request.price,
            "stock_quantity": product_request.stock_quantity
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str)