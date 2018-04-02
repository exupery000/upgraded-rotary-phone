# hw 26
# Создайте список из 11 случайных целых чисел из отрезка [-1;1].
# Передайте его в функцию, которая определит какой элемент встречается в списке чаще всего и вернет этот элемент.
# Однако, если два каких-то элемента встречаются одинаковое количество раз, то вернуть None,
# а не самый часто встречающийся элемент, даже если дублирующиеся элементы не максимальны!
#
# def calc_frequency(lst): # returns the most frequent number or None
# 		pass

print('Задание 26'
      '\nСоздайте список из 11 случайных целых чисел из отрезка [-1;1].'
      '\nПередайте его в функцию, которая определит какой элемент встречается в списке '
      '\nчаще всего и вернет этот элемент.'
      '\nОднако, если два каких-то элемента встречаются одинаковое количество раз, то вернуть None,'
      '\nа не самый часто встречающийся элемент, даже если дублирующиеся элементы не максимальны!'
      '\n'
      '\ndef calc_frequency(lst): # returns the most frequent number or None'
      '\n       pass'
      '\n')

import random

lst = [random.randint(-1, 1) for i in range(11)]
print('Сгенерируем список из 11 чисел в промежутке от -1 до 1')
print(lst)


# lst = [-4, 5, 0, 9, 4, -3, 6, 3, 4, 7, -2, -7, -3, 9, -4, -6, -7, -1, -4, -8]
# print(lst)


def calc_frequency(lst):
    frequency = {}
    max = 0
    max_key = 0
    for digit in lst:
        frequency[digit] = frequency.get(digit, 0) + 1
    print('Определим частоту появления каждого числа')
    print(frequency)
    dict_lst = frequency.values()
    # print(dict_lst)
    # print(len(dict_lst))
    zipped_dict_lst = list(set(dict_lst))
    # print(zipped_dict_lst)
    # print(len(zipped_dict_lst))

    if len(frequency) == 1:
        return list(frequency.keys())[0]

    if len(zipped_dict_lst) < len(dict_lst):
        print('Согласно условию - два каких-то элемента встречаются одинаковое количество раз')
        return None

    for key in frequency:
        if frequency[key] > max:
            max = frequency[key]
            max_key = key
    print('Элемент "%d" встречается в списке %d раз' % (max_key, max))
    return max_key


calc_frequency(lst)
