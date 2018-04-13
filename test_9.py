# 9. Нормировать одномерный список случайных чисел.
# Нормирование означает приведение всех значений массива к интервалу [-1;1],
# причем максимальное абсолютное значение элементов после нормирование
# должно быть равно 1. Например, последовательность [-5, 3, 4]
# после нормирование будет выглядеть [-1, 0.6, 0.8]

import random

print('Возьмем некий произвольно сгенерированный список из 10-ти элементов'
      '\nв пределах от "-5" до "5"')
print('--------------------------------------')
lst1 = [random.randint(-10, 10) for i in range(10)]
print(lst1)
print('--------------------------------------')
print()


def normalize_lst(lst):
    absolute_max = max(lst, key=abs)

    # absolute_elem = 0
    # for i in lst:
    #     if abs(i) > abs(absolute_elem):
    #         absolute_elem = i
    # print(absolute_elem)

    for i in range(len(lst)):
        lst[i] = lst[i] / abs(absolute_max)
    return lst, absolute_max


var1, var2 = normalize_lst(lst1)

print('Определим максимальное абсолютное значение: ', var2)
print('Выведем нормированный список: ', var1)

