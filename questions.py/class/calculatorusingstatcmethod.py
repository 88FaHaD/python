class calculator:
    @staticmethod
    def add(a,b):
       return a+b
    @staticmethod
    def sub(a,b):
        return a-b
    @staticmethod
    def mul(a,b):
        return a*b
    @staticmethod
    def divide(a,b):
        return a/b
    
print(calculator.add(2,4))
print(calculator.sub(2,4))
print(calculator.divide(4,2))
print(calculator.mul(2,4))