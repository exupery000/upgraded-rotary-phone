# hw17
# Написать функцию решения квадратного уравнения.
# def solve_quadratic_equation(a, b, c): # returns 2 values: either 2 roots or 2 Nones
#           pass

import math

def solve_quadratic_equation(a, b, c):
    d = b**2 - 4 * a * c
    x1 = (- b + math.sqrt(d)) / 2 * a
    x2 = (- b - math.sqrt(d)) / 2 * a
    if d > 0:
        return
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


x1, x2 = solve_quadratic_equation(a, b, c)
print(x1, x2)
