def max_value(lst):
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val

print(max_value([4, 9, 1, 7]))
