# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
import random


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn(self):
        if random.random() > 0.5:
            return f'{self.name} Повернула направо'
        else:
            return f'{self.name} Повернула налево'

    def show_speed(self):
        return f'Скорость {self.name} равна {self.speed} км/ч'


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print('Скорость превышена')
        else:
            print(f'Скорость {self.name} равна {self.speed} км/ч')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print('Скорость превышена')
        else:
            print(f'Скорость {self.name} равна {self.speed} км/ч')


class PoliceCar(Car):

    def police(self):
        if self.is_police:
            return f'{self.name} - полицейская машина'
        else:
            return f'{self.name} - гражданская машина'


p_car = PoliceCar(70, 'black', 'BA3', True)
s_car = SportCar(100, 'red', 'Ferrari', False)
t_car = TownCar(60, 'white', 'Opel', False)
w_car = WorkCar(50, 'gray', 'ГАЗ', False)
w_car.show_speed()
print(t_car.go())
print(w_car.stop())
print(w_car.turn())
print(p_car.police())
print(s_car.show_speed())
