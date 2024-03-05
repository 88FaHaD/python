class Animal:
    def __init__(self, species):
        self.species = species

    def speak(self):
        print(f"A {self.species} speaks")

class Dog(Animal):
    def speak(self):
        print(f"A {self.species} barks")

class Cat(Animal):
    def speak(self):
        print(f"A {self.species} meows")

# Usage
dog = Dog("dog")
dog.speak()  # Output: A dog barks

cat = Cat("cat")
cat.speak()  # Output: A cat meows
