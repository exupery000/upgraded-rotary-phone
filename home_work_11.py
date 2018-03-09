# Написать функцию, которая будет переводить градусы в радианы.
# Используя эту функцию вывести на экран значения косинусов углов в 60, 45 и 40 градусов.
# def degrees2radians(degrees): # returns float
# 			pass

import math

# функция для перевода углов в радианы
def degrees2radians(degrees):
    radians = (degrees * math.pi) / 180
    return radians


cosinus_of_degree_in_rad = math.cos(degrees2radians(60))
print("Косинус угла 60 градусов")
print(cosinus_of_degree_in_rad)

print()
cosinus_of_degree_in_rad = math.cos(degrees2radians(45))
print("Косинус угла 45 градусов")
print(cosinus_of_degree_in_rad)

print()
cosinus_of_degree_in_rad = math.cos(degrees2radians(40))
print("Косинус угла 40 градусов")
print(cosinus_of_degree_in_rad)
