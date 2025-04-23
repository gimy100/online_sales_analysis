# Analiza Vânzărilor Online

Acest proiect simulează o parte a funcționalității unui sistem de vânzări online, concentrându-se pe gestionarea produselor și pe un coș de cumpărături simplu.

## Clase Implementate

* **`Product` (`product.py`):** Reprezintă un produs individual cu următoarele atribute:
    * `name`: Numele produsului (string).
    * `price`: Prețul produsului (float).
    * `quantity`: Cantitatea disponibilă în stoc (integer).
    Metode:
    * `__init__(self, name, price, quantity)`: Constructorul clasei.
    * `display_info(self)`: Afișează informațiile produsului.
    * `update_quantity(self, new_quantity)`: Actualizează cantitatea produsului.

* **`ProductManager` (`product_manager.py`):** Gestionează o listă de obiecte `Product`.
    Metode:
    * `__init__(self)`: Constructorul clasei.
    * `add_product(self, product)`: Adaugă un obiect `Product` în listă.
    * `show_all_products(self)`: Afișează informațiile tuturor produselor.
    * `total_inventory_value(self)`: Calculează și afișează valoarea totală a inventarului.
    * `remove_product(self, product_name)`: Șterge un produs după nume.

* **`Cart` (`cart.py`):** Reprezintă un coș de cumpărături, conținând o listă de produse.
    Atribute:
    * `cart_items`: O listă de obiecte `Product` aflate în coș.
    Metode:
    * `__init__(self)`: Constructorul clasei.
    * `add_item(self, product)`: Adaugă un produs în coș.
    * `calculate_total(self)`: Calculează valoarea totală a produselor din coș.
    * `display_cart(self)`: Afișează conținutul coșului și valoarea totală.

## Funcționalități Implementate

* **Gestionarea Produselor:** Posibilitatea de a adăuga, vizualiza și (într-o anumită măsură) șterge produse din inventar prin intermediul clasei `ProductManager`.
* **Coș de Cumpărături:** Implementarea unui coș de cumpărături (`Cart`) care permite adăugarea de produse, calcularea valorii totale și afișarea conținutului.
* **Adăugare Aleatorie în Coș:** Fișierul `main.py` adaugă în mod aleatoriu 3 produse din inventar în coș.

## Fișiere Importante

* `main.py`: Fișierul principal care demonstrează utilizarea claselor `ProductManager` și `Cart`.
* `product.py`: Definește clasa `Product`.
* `product_manager.py`: Definește clasa `ProductManager`.
* `cart.py`: Definește clasa `Cart`.
* `.gitignore`: Specifică fișierele și directoarele pe care Git ar trebui să le ignore (inclusiv `config.json` și capturile de ecran).
* `config.json`: (Ignorat de Git) Un fișier de configurare simulat care ar putea conține date sensibile.
* `README.md`: Acest fișier, care oferă o prezentare generală a proiectului.

## Cum să rulezi proiectul

1.  Asigură-te că ai Python instalat pe sistemul tău.
2.  Clonează repository-ul (dacă este cazul).
3.  Navighează la directorul proiectului în terminal.
4.  Rulează fișierul `main.py` folosind comanda: `python main.py`

## Autor

[Ciuperca Cristian]

## Data 23/04/2025

[Data creării sau a ultimei actualizări]