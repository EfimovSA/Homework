a = int((input('Введите а: ')))
b = int((input('Введите b: ')))
count = 1

while a < b:
    a *= 1.1
    count += 1

print(count)