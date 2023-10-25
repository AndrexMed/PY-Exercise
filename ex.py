# class Product:
#     def __init__(self, product_id, name, description, cost, quantity, margin):
#         self.product_id = product_id
#         self.name = name
#         self.description = description
#         self.cost = cost
#         self.quantity = quantity
#         self.margin = margin
#         self.price_of_sale = self.calculate_price_of_sale()

#     def calculate_price_of_sale(self):
#         try:
#             price_of_sale = self.cost / (1 - self.margin)
#             return price_of_sale
#         except ZeroDivisionError:
#             return 0

# class ProductManager:
#     def __init__(self):
#         self.products = {}

#     def register_product(self, product):
#         if isinstance(product, Product):
#             self.products[product.product_id] = product

#     def list_products(self):
#         for product_id, product in self.products.items():
#             print(f"Product ID: {product_id}")
#             print(f"Name: {product.name}")
#             print(f"Description: {product.description}")
#             print(f"Cost: {product.cost}")
#             print(f"Quantity: {product.quantity}")
#             print(f"Price of Sale: {product.price_of_sale}")
#             print("-" * 20)


# product1 = Product(1, "Product 1", "Description 1", 10.0, 100, 0.1)
# product2 = Product(2, "Product 2", "Description 2", 20.0, 50, 0.15)

# product_manager = ProductManager()

# product_manager.register_product(product1)
# product_manager.register_product(product2)

# product_manager.list_products()
# class Product:
#     def __init__(self, product_id, name, description, cost, quantity, margin):
#         self.product_id = product_id
#         self.name = name
#         self.description = description
#         self.cost = cost
#         self.quantity = quantity
#         self.margin = margin
#         self.price_of_sale = self.calculate_price_of_sale()

#     def calculate_price_of_sale(self):
#         try:
#             price_of_sale = self.cost / (1 - self.margin)
#             return price_of_sale
#         except ZeroDivisionError:
#             return 0

# class ProductManager:
#     def __init__(self):
#         self.products = {}

#     def register_product(self, product):
#         if isinstance(product, Product):
#             self.products[product.product_id] = product

#     def list_products(self):
#         for product_id, product in self.products.items():
#             print(f"Product ID: {product_id}")
#             print(f"Name: {product.name}")
#             print(f"Description: {product.description}")
#             print(f"Cost: {product.cost}")
#             print(f"Quantity: {product.quantity}")
#             print(f"Price of Sale: {product.price_of_sale}")
#             print("-" * 20)


# product1 = Product(1, "Product 1", "Description 1", 10.0, 100, 0)
# product2 = Product(2, "Product 2", "Description 2", 20.0, 50, 0.15)

# product_manager = ProductManager()

# product_manager.register_product(product1)
# product_manager.register_product(product2)

# product_manager.list_products()
class Product:
    def __init__(self, productId, productName, productDescription, productCost, productQuantity, productMargin) -> None:
        self.productId = productId
        self.nameProduct = productName
        self.productDescription = productDescription
        self.productCost = productCost
        self.productQuantity = productQuantity
        self.productMargin = productMargin
        self.price_of_sale = self.calculate_price_of_sale()

    def calculate_price_of_sale(self):
        try:
          price_of_sale = self.productCost / (1 - self.productMargin)
          return price_of_sale
        except ZeroDivisionError:
            return 0
        
class ProductService:
    def __init__(self) -> None:
        self.products_inventory = {}

    
    def menu(self):
         while True:
            print("\nMenú:")
            print("1. Register a product")
            print("2. List of products")
            print("3. Exit")

            option = int(input("Select a option: "))

            if option == 1:
                product_id = int(input("\nEnter id or reference of product: "))
                product_name = input("Enter name of product: ")
                product_description = input("Enter a description of product: ")
                product_cost = float(input("Enter a cost of product: "))
                product_quantity = int(input("Enter a quantity of products: "))
                product_margin = float(input("Enter the margin of advantage (percent): "))

                newProduct = Product(product_id, product_name, product_description, product_cost, product_quantity, product_margin)

                self.registerProduct(newProduct)
                print("\n<=== Product created ==>\n")

            elif option == 2:
                self.list_of_products()
            elif option == 3:
                print("Good bye")
                break
            else:
                print("\n<== Enter a valid option ==>\n")


    def registerProduct(self, product):
        if isinstance(product, Product):
            self.products_inventory[product.productId] = product
        else:
            print("Error")

    def list_of_products(self):
        if len(self.products_inventory) == 0:
            print("\n<== No products registered ==>\n")
        else:    
            for productId, product in self.products_inventory.items():
                print(f"\nProduct Id: {productId}")
                print(f"Name: {product.nameProduct}")
                print(f"Description: {product.productDescription}")
                print(f"Cost: {product.productCost}")
                print(f"Quantity: {product.productQuantity}")
                print(f"Price of Sale: {product.price_of_sale}")
                print("-" * 20)

productSvc = ProductService()
productSvc.menu()