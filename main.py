# main.py
import random
from product_manager import ProductManager
from cart import Cart
from product import Product

def main():
    product_manager = ProductManager()
    product_manager.add_product(Product("Laptop Pro", 1500.00, 5))
    product_manager.add_product(Product("Mouse Wireless", 30.00, 60))
    product_manager.add_product(Product("Tastatură Mecanică", 120.00, 20))
    product_manager.add_product(Product("Monitor 4K", 400.00, 10))
    product_manager.add_product(Product("Căști Noise Cancelling", 150.00, 35))

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