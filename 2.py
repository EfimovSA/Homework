# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class DivisionByNull:
    def __init__(self, a, b):
        self.a = a
        self.br = b

    @staticmethod
    def divide_by_null(a, b):
        try:
            return (a / b)
        except:
            return (f"Деление на ноль недопустимо")


div = DivisionByNull(20, 40)
print(DivisionByNull.divide_by_null(20, 0))
print(DivisionByNull.divide_by_null(100, 20))
