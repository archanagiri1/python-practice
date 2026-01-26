lst = list(map(int, input().split()))
is_pal = True

for i in range(len(lst) // 2):
    if lst[i] != lst[-i - 1]:
        is_pal = False
        break

print("Palindrome" if is_pal else "Not Palindrome")
