from sys import argv
from itertools import cycle

n = argv[1]
j = 0
list = [2, 4, 'a', 53, 2.33]
for i in cycle(list):
    print(i, end=' ')
    j += 1
    if j > int(n) * len(list) - 1:
        break
