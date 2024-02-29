# when the child lass tries to change the function of parent class we call it method overiding


class rectangle:
    def show(self):
        return 2*2
class square(rectangle):
    def show(self):
        return 3*3


r=rectangle()
print(r.show())

s=square()
print(s.show())