n = int(input("Enter number: "))
flag = True

if n < 2:
    flag = False
else:
    for i in range(2, n):
        if n % i == 0:
            flag = False
            break

print("Prime" if flag else "Not Prime")
