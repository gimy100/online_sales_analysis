class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Nume: {self.name}, Preț: {self.price}, Cantitate: {self.quantity}")

    def update_quantity(self, new_quantity):
        if isinstance(new_quantity, int) and new_quantity >= 0:
            self.quantity = new_quantity
            print(f"Cantitatea pentru {self.name} a fost actualizată la {self.quantity}.")
        else:
            print("Cantitate invalidă. Trebuie să fie un număr întreg pozitiv.")