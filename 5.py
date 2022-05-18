# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
from random import randint

n = []
f = open('5.txt', 'w+')
for i in range(0, 10):
    n.append(str(randint(0, 100)))

f.write(' '.join(n))
f.seek(0)

print(sum(int(i) for i in f.read().split()))

f.close()