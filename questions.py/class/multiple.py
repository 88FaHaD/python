# Multiple Inheritance
class Flyable:
    def fly(self):
        return "Can fly"

class Swimmable:
    def swim(self):
        return "Can swim"

class Duck(Flyable, Swimmable):
    def name(self):
        return "Duck"

# Instances
duck = Duck()

# Multiple Inheritance Example
print(duck.fly())   
print(duck.swim())  
print(duck.name())  
