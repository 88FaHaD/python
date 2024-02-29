def pet(animal):
    animal.talk()
    animal.walk()

class duck():
    def talk(self):
        print('quack quack')
    def walk(self):
        print('duck is walking ')

class cat():
    def talk(self):
        print('meow meow')
    def walk(self):
        print('cat is walking  ')

d=duck()
pet(d)
c=cat()
pet(c)