n = int(input('Введите целое положительное число: '))
max_number = n % 10
n = n // 10

while n > 0:
    if n % 10 > max_number:
        max_number = n % 10
    n = n // 10

print('Наибольшая цифра в числе:',max_number)

