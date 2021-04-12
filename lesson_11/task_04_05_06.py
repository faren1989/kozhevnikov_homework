# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и
# передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

class Storage:
    def __init__(self, capacity):
        self.__capacity = capacity

    # @staticmethod
    # def storage_import(quantity):  # здесь проверка, что мы можем загрузить еще техники и вывод общей загрузки склада
    #     storage_usage = sum(OfficeEquipment.storage.values())
    #     if storage_usage + quantity > self.__capacity:
    #         raise ValueError(f'Мы не можем принять такое количество на склад. Объем склада превышен на '
    #                          f'{storage_usage + quantity - Storage.__capacity} единиц')

    def storage_export(self):  # здесь проверка, есть ли достаточное количество техники на складе
        pass

    def __str__(self):  # здесь вывод словаря, сколько какой техники на складе
        for key, value in OfficeEquipment.storage.items():
            print(f'{key} - на складе {value} шт.')
        storage_usage = sum(OfficeEquipment.storage.values())
        return f'Склад используется на {storage_usage/self.__capacity*100:.02f}%.\n' \
               f'Свободно {self.__capacity - storage_usage} мест'


class OfficeEquipment:
    storage = {}

    def __init__(self, firm, model, quantity):
        self.firm = firm
        self.model = model
        self.quantity = quantity
        OfficeEquipment.storage.setdefault(self.__class__.__name__, 0)
        OfficeEquipment.storage[self.__class__.__name__] += self.quantity
        # Storage.storage_import(self.quantity)

    def __str__(self):
        return f'{self.firm} {self.model}, на складе: {self.quantity} шт.'


class Printer(OfficeEquipment):
    pass


class Copier(OfficeEquipment):
    pass


class Scanner(OfficeEquipment):
    pass


a = Printer('HP', 'RW1500', 9)
b = Copier('Xerox', '69512q', 7)
c = Scanner('Panasonic', 'PQ560', 2)
d = Printer('HP', 'LaserJet', 3)
storage = Storage(50)

print(a)
print(b)
print(c)
print(d)
print('_______')
# print(OfficeEquipment.storage)
print(storage)
