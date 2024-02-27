# Multilevel Inheritance
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def bark(self):
        return "Dog barks"

class Labrador(Dog):
    def color(self):
        return "Labrador is black"

# Instances
labrador = Labrador()

# Multilevel Inheritance Example
print(labrador.speak())  # Output: Animal speaks
print(labrador.bark())   # Output: Dog barks
print(labrador.color())  # Output: Labrador is black

