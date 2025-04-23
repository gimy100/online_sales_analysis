from product import Product
from product_manager import ProductManager

# Creează instanța ProductManager
manager = ProductManager()

# Adaugă produse arbitrare
produs1 = Product("Laptop", 3500, 5)
produs2 = Product("Mouse", 100, 20)
produs3 = Product("Monitor", 700, 10)

manager.add_product(produs1)
manager.add_product(produs2)
manager.add_product(produs3)

# Afișează toate produsele
print("=== Lista produse ===")
manager.show_all_products()

# Afișează valoarea totală a inventarului
manager.total_inventory_value()

# Șterge un produs existent
print("\n=== Ștergere produs: Mouse ===")
manager.remove_product("Mouse")

# Afișează lista după ștergere
print("\n=== Lista produse după ștergere ===")
manager.show_all_products()

# Încearcă să ștergi un produs care nu există
print("\n=== Încercare ștergere produs inexistent: Telefon ===")
manager.remove_product("Monitor")
