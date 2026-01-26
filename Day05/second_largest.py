lst = list(map(int, input().split()))
largest = None
second = None

for x in lst:
    if largest is None or x > largest:
        second = largest
        largest = x
    elif second is None or (x > second and x != largest):
        second = x

print(second)
