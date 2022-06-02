# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2022 >= year >= 0:
                    return f'Дата верна'
                else:
                    return f'Этот год не наступил'
            else:
                return f'Такого месяца нет'
        else:
            return f'Такого дня нет'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


today = Data('5 - 6 - 2022')
print(today)
print(Data.valid(5, 7, 2023))
print(today.valid(12, 15, 2011))
print(Data.extract('22 - 11 - 2021'))
print(Data.valid(2, 6, 2000))
