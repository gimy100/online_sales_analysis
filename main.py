# main.py
import random
from product_manager import ProductManager
from cart import Cart
from product import Product

def main():
    product_manager = ProductManager()
    product_manager.add_product(Product("Laptop", 1200.00, 10))
    product_manager.add_product(Product("Mouse", 25.50, 50))
    product_manager.add_product(Product("Tastatură", 75.00, 30))
    product_manager.add_product(Product("Monitor", 300.00, 15))
    product_manager.add_product(Product("Căști", 90.75, 40))

    cart = Cart()

    available_products = product_manager.products
    if len(available_products) >= 3:
        random_products = random.sample(available_products, 3)
        for product in random_products:
            cart.add_item(product)
    else:
        print("Nu sunt suficiente produse disponibile pentru a adăuga 3 în coș.")

    cart.display_cart()

if __name__ == "__main__":
    main()