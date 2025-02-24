# Напишите функцию square, принимающую один аргумент — сторону квадрата
# — и возвращающую площадь квадрата.

import math

def square(a):
    return math.ceil(a*a)

a = float(input('Введите число: '))
print(f'Площадь квадрата - {square(a)}')