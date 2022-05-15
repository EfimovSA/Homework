from sys import argv
from itertools import count

n = argv[1]
for i in count(int(n)):
    print(i)
    if i > 9:
        break
