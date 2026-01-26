lst = list(map(int, input().split()))
dup = []
for x in lst:
    if lst.count(x) > 1 and x not in dup:
        dup.append(x)
print(dup)
