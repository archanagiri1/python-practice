lst = list(map(int, input().split()))
n = max(lst)
total = n * (n + 1) // 2
sum_list = 0
for x in lst:
    sum_list += x
print(total - sum_list)
