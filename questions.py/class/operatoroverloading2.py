class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # Create a new Point object with the sum of coordinates
        return Point(self.x + other.x, self.y + other.y)

# Create two Point objects
point1 = Point(3, 4)
point2 = Point(1, 2)

# Add the points together
result = point1 + point2

# Print the result
print("Resulting point:", result.x, result.y)
