class Electronics:
    def __init__(self, brand):
        self.brand = brand

    def power_on(self):
        print(f"Powering on {self.brand}")

class Laptop(Electronics):
    def power_on(self):
        print(f"Booting up {self.brand} laptop")

class Smartphone(Electronics):
    def power_on(self):
        print(f"Starting {self.brand} smartphone")

# Usage
laptop = Laptop("Dell")
laptop.power_on()  # Output: Booting up Dell laptop

phone = Smartphone("Apple")
phone.power_on()  # Output: Starting Apple smartphone
