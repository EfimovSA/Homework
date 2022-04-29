a = int(input('Введите действительное положительное число: '))
b = int(input('Введите целое отрицательное число: '))


def func_1(x, y):
    return x ** y


def func_2(x, y):
    res = x
    for i in range(1, abs(y)):
        res *= x
    return 1 / res


print('a в степени b =', func_1(a, b))
print('a в степени b =', func_2(a, b))
