import os
import motor.motor_asyncio

# Environment variables for configuration
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "ShopDatabase")

class Database:
    client = None
    db = None

    @classmethod
    def get_db(cls):
        if cls.client is None:
            cls.client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
            cls.db = cls.client[DB_NAME]
        return cls.db