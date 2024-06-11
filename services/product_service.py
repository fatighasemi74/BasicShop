from bson import ObjectId

class ProductService:
    def __init__(self, db):
        self.db = db
        if 'products' not in self.db:
            self.db['products'] = []

    async def create_product(self, name: str, description: str, price: float, stock_quantity: int):
        product_id = str(len(self.db['products']) + 1)
        product_document = {
            "product_id": product_id,
            "name": name,
            "description": description,
            "price": price,
            "stock_quantity": stock_quantity
        }

        result = self.db['products'].append(product_document)
        return product_id

    async def get_products(self):
        return self.db['products']

    async def get_product_by_id(self, product_id):
        for product in self.db['products']:
            if product['product_id'] == product_id:
                return product
        return None

    async def update_product_by_id(self, product_id, update_fields):
        for index, product in enumerate(self.db['products']):
            if product['product_id'] == product_id:
                self.db['products'][index].update(update_fields)
                return True
        return False

    async def delete_product_by_id(self, product_id): 
        initial_count = len(self.db['products'])
        self.db['products'] = [product for product in self.db['products'] if product['product_id'] != product_id]
        return len(self.db['products']) != initial_count