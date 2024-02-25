class Cuboid:
    def __init__(self, l, b, h):
        self.length = l
        self.breadth = b
        self.height = h

    def lid_area(self):
        return self.length * self.breadth

    def total_area(self):
        return 2 * (self.length * self.breadth + self.breadth * self.height + self.length * self.height)

    def volume(self):
        return self.height * self.breadth * self.length

c1 = Cuboid(2, 3, 4)

print('volume is ',c1.volume())
print('total area is ',c1.total_area())
print('lid area is ', c1.lid_area())