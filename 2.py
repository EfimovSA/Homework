# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.
i = 0

f = open('2.txt', 'r')
s = f.read().count('\n') + 1
print(f'Число строк в файле {f.name} - {s}')
f.seek(0)

while i < s:
    w = len(f.readline().split())
    i += 1
    print(f'В {i}-й строке {w} слов(а)')

f.close()
