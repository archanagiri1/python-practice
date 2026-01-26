lst = list(map(int, input().split()))
max_so_far = lst[0]
current = lst[0]

for i in range(1, len(lst)):
    current = max(lst[i], current + lst[i])
    max_so_far = max(max_so_far, current)

print(max_so_far)
