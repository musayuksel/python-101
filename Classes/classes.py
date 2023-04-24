class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self._price = max(price, 0)

    def full_name(self):
        return f"{self.brand} {self.model}"

    def get_price(self):
        return self._price

    def set_price(self, new_price):
        self._price = max(new_price, 0)

    def __str__(self):
        return f"{self.brand} {self.model} and price is {self._price}"


phone1 = Phone("Nokia", "1100", 300)
print(f"Brand: {phone1.full_name()}")
print(f"Price: {phone1.get_price()}")

phone1.set_price(200)
print(f"Price: {phone1.get_price()}")

print(phone1)
