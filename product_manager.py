from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def show_all_products(self):
        for product in self.products:
            print(f"Nume: {product.name}, Preț: {product.price}, Stoc: {product.quantity}")

    def total_inventory_value(self):
        total_value = sum(product.price * product.quantity for product in self.products)
        print(f"Valoarea totală a inventarului: {total_value}")

    def remove_product(self, product_name):
        initial_length = len(self.products)
        self.products = [product for product in self.products if product.name != product_name]
        if len(self.products) < initial_length:
            print(f"Produsul {product_name} a fost șters.")
        else:
            print(f"Produsul {product_name} nu a fost găsit în inventar.")