# cart.py

class Cart:
    def __init__(self):
        self.cart_items = []

    def add_item(self, product):
        self.cart_items.append(product)
        print(f"Produsul '{product.name}' a fost adăugat în coș.")

    def calculate_total(self):
        total = sum(item.price for item in self.cart_items)
        return total

    def display_cart(self):
        if not self.cart_items:
            print("Coșul este gol.")
            return

        print("Conținutul coșului:")
        for item in self.cart_items:
            print(f"- {item.name}: {item.price} PLN")
        print(f"Valoarea totală a coșului: {self.calculate_total()} PLN")