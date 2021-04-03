# 4. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw() (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три производных класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе переопределить метод draw(). Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры каждого класса и положить их в список. Проитерироваться по этому списку и вызвать метод draw()
# для каждого элемента.

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Рисуем ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Рисуем карандашом')


class Handle(Stationery):
    def draw(self):
        print('Рисуем маркером')

ex_1 = Stationery('ex_1')
ex_2 = Pen('ex_2')
ex_3 = Pencil('ex_3')
ex_4 = Handle('ex_4')

lst = [ex_1, ex_2, ex_3, ex_4]

for i in lst:
    i.draw()