# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Создать абстрактный класс Clothes (одежда). Сделать в этом классе свойство cloth_size
# (используя декоратор @property) - размер ткани, необходимый для производства одежды.
# Это свойство должно вычислять размерт ткани, вызывая абстрактный метод self.get_size().
# Сделать два производных класса одежды: Suit (костюм) и Coat (Пальто).
# В конструктор Suit должен принимать параметр height (рост), а Coat - size (размер).
# Для определения расхода ткани по каждому типу одежды внутри метода get_size() использовать формулы:
#
# для пальто: (size/6.5 + 0.5)
# для костюма: (2*height + 0.3)
# Создать список из 10 единиц одежды случайно выбирая один из двух возможных типов со случайным параметром.
# Распечатать список одежды: размер требуемой ткани, тип и параметр.
# Рассчитать и вывести на экран общий объем ткани, необходимый для пошива всей одежды из этого списка,
# используя свойство cloth_size. Например:
#
# 30.3 - Suit (height: 15)
# 20 - Coat (size: 3)
# 13.5 - Coat (size: 2)
# 4.3 - Suit (size: 2)
# ...
# Итого: 250.3

from abc import ABC, abstractmethod
from random import choice, randint


class Clothes(ABC):
    @property
    def cloth_size(self):
        return self.get_size()

    @abstractmethod
    def get_size(self):
        pass


class Suit(Clothes):
    def __init__(self, param):
        self.height = param

    def get_size(self):
        return f'{(2 * self.height + 0.3):.2f}'

    def __str__(self):
        return f'{self.get_size()} - Suit (height: {self.height})'


class Coat(Clothes):
    def __init__(self, param):
        self.size = param

    def get_size(self):
        return f'{(self.size/6.5 + 0.5):.2f}'

    def __str__(self):
        return f'{self.get_size()} - Coat (size: {self.size})'


cloth = []
for _ in range(10):
    cloth.append(choice([Coat(randint(0, 15)), Suit(randint(0, 8))]))

cloth_need = 0
for i in cloth:
    print(i)
    cloth_need += float(i.cloth_size)
print(f'Итого: {cloth_need:.2f}')
