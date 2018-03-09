# hw13
# Пользователь вводит длины катетов прямоугольного треугольника.
# Написать функцию, которая вычислит площадь треугольника и его периметр.
# Результат работы функции должен вернуть два значения.
# def triangle_square_and_perimeter(a, b): # returns 2 values
# 			pass

print("Задание 13"
      "\nПользователь вводит длины катетов прямоугольного треугольника."
      "\nНаписать функцию, которая вычислит площадь треугольника и его периметр."
      "\nРезультат работы функции должен вернуть два значения."
      "\ndef triangle_square_and_perimeter(a, b): # returns 2 values"
      "\n       pass")
print()


def triangle_square_and_perimeter(a, b):
    triangle_square = (a * b) / 2
    triangle_perimeter = a + b + ((a**2 + b**2)**0.5)
    return triangle_square, triangle_perimeter


a = input('Введите исходные данные - катеты a :')
b = input('Введите исходные данные - катеты b :')


res1, res2 = triangle_square_and_perimeter(int(a), int(b))


print()
print("Площадь:", res1)
print("Периметр:", res2)
