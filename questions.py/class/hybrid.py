class A:
    def method_a(self):
        return "Method A"

class B:
    def method_b(self):
        return "Method B"

class C(A, B):
    def method_c(self):
        return "Method C"

class D(C):
    def method_d(self):
        return "Method D"

# Instances
d = D()

# Hybrid Inheritance Example
print(d.method_a())  
print(d.method_b())  
print(d.method_c())  
print(d.method_d()) 