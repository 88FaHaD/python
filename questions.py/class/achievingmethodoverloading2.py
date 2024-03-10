class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

# Creating an instance of Calculator
calc = Calculator()

# Overloaded methods
print("Adding two numbers:", calc.add(8, 3))  # Outputs: 5
print("Adding three numbers:", calc.add(2, 3, 4))  # Outputs: 9
