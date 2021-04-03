# 5. Реализуйте базовый класс Car.
# при создании класса должны быть переданы атрибуты: color (str), name (str).
# реализовать в классе методы: go(speed), stop(), turn(direction), которые должны изменять состояние машины -
# для хранения этих свойств вам понадобятся дополнительные атрибуты - придумайте какие.
# добавьте метод is_police() - который возвращает True/False, в зависимости от того является ли этот автомобиль
# полицейским (см.дальше)
# Сделайте несколько производных классов: TownCar, SportCar, WorkCar, PoliceCar;
# Добавьте в базовый класс метод get_status(), который должен возвращать в виде строки название, цвет,
# текущую скорость автомобиля и направление движения (в случае если автомобиль едет), для полицейских автомобилей
# перед названием автомобиля должно идти слово POLICE;
# Для классов TownCar и WorkCar в методе get_status() рядом со значением скорости должна выводиться фраза "ПРЕВЫШЕНИЕ!",
# если скорость превышает 60 (TownCar) и 40 (WorkCar).
# Создайте по одному экземпляру каждого производного класса. В цикле из 10 итераций,
# для каждого автомобиля сделайте одно из случайных действий: go, stop, turn со случайными параметрами.
# После каждого действия показывайте статус автомобиля.

from random import randint, choice


class Car:

    def __init__(self, color, name, speed=0, direction='стоит на месте'):
        self.color = color
        self.name = name
        self.speed = speed
        self.direction = direction

    def go(self):
        self.speed = randint(0, 100)
        self.direction = choice(['Север', 'Юг', 'Восток', 'Запад'])
        return self.speed

    def stop(self):
        self.direction = 'стоит на месте'
        self.speed = 0
        return self.direction, self.speed

    def turn(self):
        self.direction = choice(['Север', 'Юг', 'Восток', 'Запад'])
        self.speed = randint(0, 100)
        return self.direction

    def is_police(self):
        if type(self) == PoliceCar:
            return True
        else:
            return False

    def get_status(self):
        if self.direction == 'стоит на месте' or self.speed == 0:
            return f'{self.color} {self.name} стоит на месте'
        else:
            return f'{self.color} {self.name} едет со скоростью {self.speed} в направлении {self.direction}а'


class TownCar(Car):
    def get_status(self):
        if self.direction == 'стоит на месте' or self.speed == 0:
            return f'{self.color} {self.name} стоит на месте'
        elif self.speed > 60:
            return f'{self.color} {self.name} едет со скоростью {self.speed}(ПРЕВЫШЕНИЕ!) в направлении {self.direction}а'
        else:
            return f'{self.color} {self.name} едет со скоростью {self.speed} в направлении {self.direction}а'


class SportCar(Car):
    def get_status(self):
        if self.direction == 'стоит на месте' or self.speed == 0:
            return f'{self.color} {self.name} стоит на месте и выпендривается'
        else:
            return f'{self.color} {self.name} едет со скоростью {self.speed} в направлении {self.direction}а и всех подрезает'


class WorkCar(Car):
    def get_status(self):
        if self.direction == 'стоит на месте' or self.speed == 0:
            return f'{self.color} {self.name} стоит на месте'
        elif self.speed > 40:
            return f'{self.color} {self.name} едет со скоростью {self.speed}(ПРЕВЫШЕНИЕ!) в направлении {self.direction}а'
        else:
            return f'{self.color} {self.name} едет со скоростью {self.speed} в направлении {self.direction}а'


class PoliceCar(Car):
    def get_status(self):
        if self.is_police() is True:
            if self.direction == 'стоит на месте' or self.speed == 0:
                return f'{self.color} POLICE {self.name} стоит на месте'
            else:
                return f'{self.color} POLICE {self.name} едет со скоростью {self.speed} в направлении {self.direction}а'


car_models = ['Volvo', 'Volkswagen', 'Fiat', 'Mustang', 'Ford']
car_colors = ['красный', 'зеленый', 'черный', 'белый']

car_1 = TownCar(choice(car_colors), choice(car_models))
car_2 = SportCar(choice(car_colors), choice(car_models))
car_3 = WorkCar(choice(car_colors), choice(car_models))
car_4 = PoliceCar(choice(car_colors), choice(car_models))

for i in range(10):
    action = randint(1, 3)
    if action == 1:
        car_1.go()
    elif action == 2:
        car_1.turn()
    elif action == 3:
        car_1.stop()
    print(car_1.get_status())
print('_______')

for i in range(10):
    action = randint(1, 3)
    if action == 1:
        car_2.go()
    elif action == 2:
        car_2.turn()
    elif action == 3:
        car_2.stop()
    print(car_2.get_status())
print('_______')

for i in range(10):
    action = randint(1, 3)
    if action == 1:
        car_3.go()
    elif action == 2:
        car_3.turn()
    elif action == 3:
        car_3.stop()
    print(car_3.get_status())
print('_______')

for i in range(10):
    action = randint(1, 3)
    if action == 1:
        car_4.go()
    elif action == 2:
        car_4.turn()
    elif action == 3:
        car_4.stop()
    print(car_4.get_status())
