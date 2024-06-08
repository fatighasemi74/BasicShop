from bson import ObjectId

class ProductService:
    def __init__(self, db):
        self.db = db

    async def create_product(self, name: str, description: str, price: float, stock_quantity: int):
        product_document = {
            "name": name,
            "description": description,
            "price": price,
            "stock_quantity": stock_quantity
        }

        result = await self.db["product"].insert_one(product_document)
        return str(result.inserted_id)

    async def get_product(self):
        cursor = self.db["product"].find({})
        products = await cursor.to_list(length=None)
        return products

    async def get_product_by_id(self, product_id):
        product = await self.db["product"].find_one({"_id": ObjectId(product_id)})
        return product

    async def update_product_by_id(self, product_id, update_fields):
        result = await self.db["product"].update_one(
            {"_id": ObjectId(product_id)},
            {"$set": update_fields}
        )
        return result.modified_count > 0

    async def delete_product_by_id(self, product_id):
        result = await self.db["product"].delete_one({"_id": ObjectId(product_id)})
        return result.deleted_count > 0