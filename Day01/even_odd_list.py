n =int(input("Enter n:"))

numbers=[]
even_numbers=[]
odd_numbers=[]

for i in range(1,n+1):
    numbers.append(i)

    if 1%2 ==0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)

print("Original list:", numbers)
print("Even numbers:", even_numbers)
print("Odd numbers", odd_numbers)