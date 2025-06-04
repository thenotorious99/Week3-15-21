class Laptop:
    def __init__(self, brand, ram, processor):
            self.brand = brand
            self.ram = ram
            self.processor = processor

    def info_laptop(self):
        return f"Brand: {self.brand}, Ram: {self.ram}, Processor: {self.processor}"

laptop = Laptop("Dell", "1TB", "16CPU")

print(laptop.info_laptop())