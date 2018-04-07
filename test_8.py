# 8. В одномерном списке поменять местами минимальный и максимальный элементы.
# Остальные оставить на своих местах.
import math
import random


def change_lst(lst):
    max_elem = - math.inf
    for i in range(len(lst)):
        if lst[i] > max_elem:
            max_elem = lst[i]

    min_elem = math.inf
    for i in range(len(lst)):
        if lst[i] < min_elem:
            min_elem = lst[i]
    # print(min_elem, max_elem)
    # print(lst.index(min_elem))
    # print(lst.index(max_elem))
    ind_min = lst.index(min_elem)
    ind_max = lst.index(max_elem)
    lst[ind_min], lst[ind_max] = lst[ind_max], lst[ind_min]

    print('Найдем максимальное и минимальное значение'
          '\nСоответственно Max elem = %d и Min elem = %d' % (max_elem, min_elem))
    print('Поменяем их местами и выведем на экран новый список')

    return lst


var1 = int(input('Список из скольки элементов вы хотите создать: '))
lst = [random.randint(1, 100) for I in range(var1)]
print(lst)
print(change_lst(lst))
