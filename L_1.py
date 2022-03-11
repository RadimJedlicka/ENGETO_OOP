class SmartFridge:

    def __init__(self, brand, model):

        self.brand = brand
        self.model = model

    def greet(self):
        print(f'Hello from {self.brand} {self.model}')

my_fridge = SmartFridge("Bosch", "neco")
print(my_fridge)
#
my_fridge.greet()

# my_fridge.brand = "Bosch"
# my_fridge.model = "GSDF"
#
# print(my_fridge.brand)
# print(my_fridge.model)

# my_fridge = SmartFridge("Bosch", "EFADA")
#
# print(my_fridge.brand)
# print(my_fridge.model)

