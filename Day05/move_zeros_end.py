lst = list(map(int, input().split()))
result = []

for x in lst:
    if x != 0:
        result.append(x)

zeros = len(lst) - len(result)
result += [0] * zeros
print(result)
