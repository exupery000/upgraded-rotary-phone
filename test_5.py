# 5. Создать программу, выводящую на экран ближайшее к 10 из двух чисел, введенных пользователем.
# Например, среди чисел 8,5 и 11,45 ближайшее к десяти 11,45.

import math


def comparison(var1, var2):
    point_of_comparison = 10.0
    print('------------------------')
    print('Сравниваем с числом %.2f' % point_of_comparison)
    segment1 = abs(float(point_of_comparison - var1))
    segment2 = abs(float(point_of_comparison - var2))
    # print(segment1)
    # print(segment2)
    if segment1 > segment2:
        print('Ближайшее к %.2f число' % point_of_comparison)
        return float(var2)
    elif segment1 == segment2:
        print('Оба числа равно удалены от точки сравнения!')
    else:
        print('Ближайшее к %.2f число' % point_of_comparison)
        return float(var1)


var1 = (float(input('Введите первое число для сравнения: ')))
var2 = (float(input('Введите второе число для сравнения: ')))

print(comparison(var1, var2))
