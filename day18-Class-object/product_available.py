class Product:
    def __init__(self, name_product, price, available):
        self.name_product = name_product
        self.price = price
        self.available = available

    def available_product(self):
        if self.available.lower() == "yes":
            return f"{self.name_product} is available."
        else:
            return f"{self.name_product} is NOT available."


product1 = Product("Toyota", 1900, "Yes")
product2 = Product("BMW", 2500, "No")

print(product1.available_product())  # Toyota is available.
print(product2.available_product())