from functools import reduce


def mult(x, y):
    return x * y


list = (i for i in range(100, 1001) if i % 2 == 0)
total = reduce(mult, list)
print(total)
