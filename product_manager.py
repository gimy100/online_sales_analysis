from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def show_all_products(self):
        for product in self.products:
            product.display_info()

    def total_inventory_value(self):
        total = sum(product.price * product.quantity for product in self.products)
        print(f"Valoarea totală a inventarului: {total} RON")
# În interiorul clasei ProductManager din product_manager.py

def remove_product(self, product_name):
    """Șterge un produs din listă după nume."""
    initial_length = len(self.products) # Lungimea initiala a listei
    # Folosim list comprehension pentru a crea o nouă listă
    # care conține doar produsele al căror nume NU se potrivește
    self.products = [p for p in self.products if p.name != product_name]
    if len(self.products) < initial_length:
        print(f"Produsul '{product_name}' a fost șters.")
    else:
        print(f"Produsul '{product_name}' nu a fost găsit.")

# Asigură-te că ai importat clasa Product dacă o folosești în type hints
# from product import Product # (dacă este necesar, depinde de cum ai structurat)
