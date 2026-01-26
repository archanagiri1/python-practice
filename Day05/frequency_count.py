lst = list(map(int, input().split()))
freq = {}
for x in lst:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1
print(freq)
