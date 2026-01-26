lst = list(map(int, input().split()))
result = []
for x in lst:
    if x not in result:
        result.append(x)
print(result)
