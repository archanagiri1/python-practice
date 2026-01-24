def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


n = int(input("Enter n: "))

print("Prime numbers and factorials:")

for i in range(1, n + 1):
    if is_prime(i):
        print(i, "->", factorial(i))
