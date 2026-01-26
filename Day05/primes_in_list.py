def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

lst = list(map(int, input().split()))
primes = []

for x in lst:
    if is_prime(x):
        primes.append(x)

print(primes)
