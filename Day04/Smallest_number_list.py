nums = list(map(int, input("Enter numbers: ").split()))
smallest = nums[0]

for n in nums:
    if n < smallest:
        smallest = n

print(smallest)
