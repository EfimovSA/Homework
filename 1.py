def div(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print('На ноль делить нельзя!')

a = int(input('Веедите делимое: '))
b = int(input('Веедите делитель: '))

print('Частрое равно:', div(a,b))