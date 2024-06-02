# from fastapi import FastAPI
# from routers import order_router
# from database import Database
# app = FastAPI()

# @app.on_event("startup")
# async def startup_event():
#     # Initialize the database connection
#     db = Database.get_db()

# @app.on_event("shutdown")
# async def shutdown_event():
#     # Properly close the database connection
#     if Database.client:
#         Database.client.close()
# # app.include_router(user_router.router)
# # app.include_router(product_router.router)
# app.include_router(order_router.router)


from fastapi import FastAPI, HTTPException, APIRouter
from services.order_service import OrderService
from database import Database

router = APIRouter()

app = FastAPI()
db = Database.get_db()
order_service = OrderService(db)

@app.post("/orders/")
async def create_order(user_id: int, product_id: int, quantity: int):
    try:
        order = await order_service.create_order(user_id, product_id, quantity)
        return order
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/")
async def hello():
    
    # Assuming you have collections named 'user', 'product', 'order'
    await db.user.insert_one({"name": "John Doe", "email": "john@example.com"})
    await db.product.insert_one({"name": "Widget", "price": 19.99})
    await db.order.insert_one({"product_name": "Widget", "quantity": 2})
    
    print("Data inserted")

