class Product:
    def __init__(self, product_id, name, description, cost, quantity, margin):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.cost = cost
        self.quantity = quantity
        self.margin = margin
        self.price_of_sale = self.calculate_price_of_sale()

    def calculate_price_of_sale(self):
        try:
            price_of_sale = self.cost / (1 - self.margin)
            return price_of_sale
        except ZeroDivisionError:
            return 0

class ProductManager:
    def __init__(self):
        self.products = {}

    def register_product(self, product):
        if isinstance(product, Product):
            self.products[product.product_id] = product

    def list_products(self):
        for product_id, product in self.products.items():
            print(f"Product ID: {product_id}")
            print(f"Name: {product.name}")
            print(f"Description: {product.description}")
            print(f"Cost: {product.cost}")
            print(f"Quantity: {product.quantity}")
            print(f"Price of Sale: {product.price_of_sale}")
            print("-" * 20)


product1 = Product(1, "Product 1", "Description 1", 10.0, 100, 0.1)
product2 = Product(2, "Product 2", "Description 2", 20.0, 50, 0.15)

product_manager = ProductManager()

product_manager.register_product(product1)
product_manager.register_product(product2)

product_manager.list_products()
