# 3. Осуществить программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс «Клетка». В его конструкторе инициализировать параметр, соответствующий
# количеству ячеек клетки (целое число). В классе должны быть реализованы методы перегрузки
# арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Эти методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и округление
# до целого числа деления клеток, соответственно.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться
# сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять, только если разность количества ячеек
# двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки — произведение количества ячеек этих двух клеток.
# Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное
# деление количества ячеек этих двух клеток.
# Добавить к классу метод print(columns), распечатыващий на экране звездочки рядами по columns
# звездочек в одном ряду в количестве равном числу ячеек клетки.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, если в клетке 12 ячеек, а запросили напечатать по 5 звездочек в ряду, то на экране должно быть:
#
# *****
# *****
# **

class Cell:

    def __init__(self, mini_cell):
        self.mini_cell = mini_cell

    def __add__(self, other):
        add_cell = Cell(self.mini_cell + other. mini_cell)
        return add_cell

    def __sub__(self, other):
        if self.mini_cell > other.mini_cell:
            sub_cell = Cell(self.mini_cell - other.mini_cell)
            return sub_cell
        elif other.mini_cell > self.mini_cell:
            sub_cell = Cell(other.mini_cell - self.mini_cell)
            return sub_cell
        else:
            raise ValueError('Разница в количестве ячеек равна нулю')

    def __mul__(self, other):
        mul_cell = Cell(self.mini_cell * other.mini_cell)
        return mul_cell

    def __truediv__(self, other):
        if self.mini_cell > other.mini_cell:
            div_cell = Cell(self.mini_cell // other.mini_cell)
            return div_cell
        else:
            div_cell = Cell(other.mini_cell // self.mini_cell)
            return div_cell

    def __str__(self):
        return f'{self.mini_cell}'

    def print(self, columns):
        cell_point = '*' * columns
        strings, points = divmod(self.mini_cell, columns)
        for _ in range(strings):
            print(cell_point)
        cell_point = '*' * points
        print(cell_point)


a = Cell(13)
b = Cell(4)
print(a)
print(b)
print(a + b)
print(a - b)
print(a / b)
print(a * b)

d = Cell(15)
d.print(6)
