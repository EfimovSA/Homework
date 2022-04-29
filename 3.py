def my_func(x, y, z):
    num = [x, y, z]
    num.sort()
    sum = num[1] + num[2]
    return sum


print(my_func(3, 2, 1))
print(my_func(1, 2, 3))
