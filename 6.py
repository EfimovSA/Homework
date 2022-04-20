income_value = int(input('Введите значение выручки: '))
cost_value = int(input('Введите значение издержек: '))

if income_value > cost_value:
    profit_rate = (income_value-cost_value) / income_value * 100
    print('Фирма олучила прибыль. Рентабельность составляет:',profit_rate,'%')
    staff_value = int(input('Введите количество сотрудников: '))
    print('Прибыль фирмы на одного сотрудника составляет:', (income_value-cost_value)/staff_value)
elif income_value == cost_value:
    print('Выручка равна издержкам')
else:
    print('Фирма получила убыток')