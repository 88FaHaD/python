class Employee:
    def __init__(self, name):
        self.name = name

    def work(self):
        print(f"{self.name} is working")

class Manager(Employee):
    def work(self):
        print(f"{self.name} is managing")

class Developer(Employee):
    def work(self):
        print(f"{self.name} is developing")

# Usage
manager = Manager("John")
manager.work()  # Output: John is managing

developer = Developer("Alice")
developer.work()  # Output: Alice is developing
