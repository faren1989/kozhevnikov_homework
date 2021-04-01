# 3. Реализовать базовый класс Employee (сотрудник).
# определить атрибуты: name (имя), surname (фамилия), которые должны передаваться при создании экземпляра Employee;
# создать класс Position (должность) с аттрибутами employee (сотрудник/Employee), position (должность/str),
# income (вознаграждение/dict) - атрибуты также задаются при создании экземпляра класса;
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus};
# в классе Position реализовать методы получения полного имени сотрудника get_full_name() и дохода с учётом премии
# get_total_income() (wage + bonus);
# проверить работу примера на реальных данных: создать экземпляры классов Employee, Position,
# вывести на экран имя сотрудника, его должность и вознаграждение сотрудника, используя методы класса Position.

class Employee:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.name} {self.surname}'


class Position:

    def __init__(self, employee, position, income):
        self.employee = employee
        self.position = position
        self._income = income

    def get_full_name(self):
        print(self.employee)

    def get_total_income(self):
        print(self._income['wage'] + self._income['bonus'])


worker1 = Employee('John', 'Peterson')
worker2 = Employee('Susan', 'Jefferson')

incm_1 = {'wage': 50, 'bonus': 20}
incm_2 = {'wage': 100, 'bonus': 50}

worker_info_1 = Position(worker1, 'driver', incm_1)
worker_info_2 = Position(worker2, 'boss', incm_2)

worker_info_1.get_full_name()
print(worker_info_1.position)
worker_info_1.get_total_income()

worker_info_2.get_full_name()
print(worker_info_2.position)
worker_info_2.get_total_income()
