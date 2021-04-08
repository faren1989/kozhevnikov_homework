# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
# формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
from datetime import datetime


class Data:
    def __init__(self, user_date):
        self.user_date = user_date

    def __str__(self):
        return self.user_date

    @classmethod
    def str_to_int(cls, user_date):
        day, month, year = user_date.split('-')
        day = int(day)
        month = int(month)
        year = int(year)
        return f'{type(day), day}\n{type(month), month}\n{type(year), year}'

    @staticmethod
    def date_validation(user_date):

        def day_validation(param, max_days):
            if 0 < param <= max_days:
                return f'{user_date} - формат даты корректен'
            else:
                return f'День {day} - некорректный формат'

        day, month, year = user_date.split('-')
        try:
            day = int(day)
            month = int(month)
            year = int(year)
        except ValueError:
            exit('Некорректный формат даты')
        if year in range(0, datetime.today().year + 1):
            if month in range(1, 13):
                if month in [1, 3, 5, 7, 8, 10, 12]:
                    return day_validation(day, 31)

                elif month in [4, 6, 9, 11]:
                    return day_validation(day, 30)

                elif month == 2 and year % 4 == 0:
                    return day_validation(day, 29)

                elif month == 2 and year % 4 != 0:
                    return day_validation(day, 28)
            else:
                return f'Месяц {month} - некорректный формат'
        else:
            return f'Год {year} - некорректный формат'


a = Data('12-11-2011')
print(a)
print(Data.str_to_int('12-11-2011'))
print(Data.date_validation('28-12-2021'))
