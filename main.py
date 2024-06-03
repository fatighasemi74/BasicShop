from fastapi import FastAPI
from routers import order_router, product_router, user_router
from database import Database

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    # Initialize the database connection
    db = Database.get_db()

@app.on_event("shutdown")
async def shutdown_event():
    # Properly close the database connection
    if Database.client:
        Database.client.close()


app.include_router(user_router.router)
app.include_router(product_router.router)
app.include_router(order_router.router)

