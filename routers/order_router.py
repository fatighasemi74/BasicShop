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