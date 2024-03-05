class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print(f"Driving {self.brand}")

class Car(Vehicle):
    def drive(self):
        print(f"Driving {self.brand} car")

class Bike(Vehicle):
    def drive(self):
        print(f"Riding {self.brand} bike")

# Usage
car = Car("Toyota")
car.drive()  # Output: Driving Toyota car

bike = Bike("Honda")
bike.drive()  # Output: Riding Honda bike
