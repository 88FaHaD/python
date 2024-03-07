def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Usage
num = int(input("Enter a number: "))
if is_prime(num):
    print("It's a prime number!")
else:
    print("It's not a prime number.")