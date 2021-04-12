# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Cmplx:
    def __init__(self, real_part, imag_part):
        self.real_part = real_part
        self.imag_part = imag_part

    def __str__(self):
        return f'({self.real_part} + {self.imag_part}j)'

    def __add__(self, other):
        add_cmplx = Cmplx(self.real_part + other.real_part, self.imag_part + other.imag_part)
        return add_cmplx

    def __mul__(self, other):
        mul_cmplx = Cmplx(self.real_part * other.real_part - self.imag_part * other.imag_part,
                          self.imag_part * other.real_part + self.real_part * other.imag_part)
        return mul_cmplx


a = Cmplx(1, 4)
b = Cmplx(6, 5)
print(a)
print(b)
print(a + b)
print(a * b)
