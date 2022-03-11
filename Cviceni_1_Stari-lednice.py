# Tvým úkolem je implementovat novou metodu uvnitř třídy SmartFridge.
# Metoda by nám měla při zavolání oznámit stáří konkrétní lednice (instance).
# Metoda by mělo spočítat stáří lednice na základě datumu jejího vytvoření.

from datetime import date


class SmartFridge:
    fridge_count = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.birth_date = date.today()                  # Nový atribut, který zaznamená datum vytvoření lednice
        SmartFridge.fridge_count += 1

    def greet(self):
        print(f'Hello from {self.brand} {self.model}!')

    def tell_age(self):                                 # Nová metoda, která spočítá stáří lednice
        td = date.today() - self.birth_date
        print(f'I am {td.days} days old.')


fridge1 = SmartFridge("LG", "GLASSAD")
fridge1.tell_age()
fridge1.greet()
print(fridge1.brand)
