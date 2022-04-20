income_value = int(input('Введите значение выручки: '))
cost_value = int(input('Введите значение издержек: '))

if income_value > cost_value:
    print('Фирма олучила прибыль')
elif income_value == cost_value:
    print('Выручка равна издержкам')
else:
    print('Фирма получила убыток')