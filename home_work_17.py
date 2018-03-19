# hw17
# Написать функцию решения квадратного уравнения.
# def solve_quadratic_equation(a, b, c): # returns 2 values: either 2 roots or 2 Nones
#           pass

import math


def solve_quadratic_equation(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (- b + math.sqrt(d)) / (2 * a)
        x2 = (- b - math.sqrt(d)) / (2 * a)
        return x1, x2

    elif d == 0:
        x = (- b + math.sqrt(d)) / (2 * a)
        return x, None

    else:
        return None, None


print('Задание 17'
      '\nНаписать функцию решения квадратного уравнения.'
      '\ndef solve_quadratic_equation(a, b, c): # returns 2 values: either 2 roots or 2 Nones'
      '\n       pass'
      '\n')

a = int(input('Enter "a": '))
b = int(input('Enter "b": '))
c = int(input('Enter "c": '))

res1, res2 = solve_quadratic_equation(a, b, c)
# print(res1, res2)

if res1 == None and res2 == None:
    print('Нет корней!')

elif res2 == None:
    print('Один корень, х =', res1)
else:
    print('Два корня, x1 = %.4f, x2 = %.4f' % (res1, res2))
