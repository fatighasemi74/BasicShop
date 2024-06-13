from interfaces.iproduct import IProduct

class ProductService(IProduct):
    def __init__(self, db):
        self.db = db
        if 'products' not in self.db:
            self.db['products'] = {}

    async def create_product(self, name: str, description: str, price: float, stock_quantity: int):
        product_id = str(len(self.db['products']) + 1)
        product_document = {
            "product_id": product_id,
            "name": name,
            "description": description,
            "price": price,
            "stock_quantity": stock_quantity
        }

        self.db['products'][product_id] = product_document
        return product_id

    async def get_products(self):
        return list(self.db['products'].values())

    async def get_product_by_id(self, product_id):
        return self.db['products'].get(product_id)

    async def update_product_by_id(self, product_id, update_fields):
        if product_id in self.db['products']:
                self.db['products'][product_id].update(update_fields)
                return True
        return False

    async def delete_product_by_id(self, product_id): 
        if product_id in self.db['products']:
            del self.db['products'][product_id]
            return True
        return False