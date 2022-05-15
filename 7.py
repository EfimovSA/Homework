from itertools import count
from math import factorial

n = 0
user_n = 10


def fact():
    for i in count(1):
        yield factorial(i)


for el in fact():
    print(el)
    n += 1
    if n >= user_n:
        break
