# hw 25
# Создайте список на 50 элементов из всех нечётных чисел от 1 до 99 и передайте его в функцию,
# которая переставляет его элементы в случайном порядке (например, 99 11 43 19 … 7 91 3 1).
# Примечание: использовать метод random.shuffle не допускается.
# def shuffle_list(list_to_shuffle): # no return (shuffles list in place)
#     pass


print('Задание 25'
      '\nСоздайте список на 50 элементов из всех нечётных чисел от 1 до 99 и передайте его в функцию,'
      '\nкоторая переставляет его элементы в случайном порядке (например, 99 11 43 19 … 7 91 3 1).'
      '\nПримечание: использовать метод random.shuffle не допускается.'
      '\n'
      '\ndef shuffle_list(list_to_shuffle): # no return (shuffles list in place)'
      '\n       pass'
      '\n')

import random

lst = [i for i in range(1, 100) if i % 2 != 0]
print('Создадим список, длиной в %d элементов' % (len(lst)))
print(lst)
print('------------------------')


def shuffle_lst(lst):
    base_lst = lst
    new_lst = []
    while len(new_lst) != len(base_lst):
        for element in lst:
            element = random.choice(lst)
            if element not in new_lst:
                new_lst.append(element)
    print('Сравним длины базового списка', len(base_lst))
    print('И Нового перемешанного списка', len(new_lst))
    print('------------------------')
    return new_lst


print('Сравним сами списки'
      '\nБазовый'
      '\n', shuffle_lst(lst))
print('------------------------')
print('Новый'
      '\n', lst)

print('------------------------')
print('------------------------')
print('------------------------')
import random

lst = [i for i in range(1, 100) if i % 2 != 0]
print(lst)
print(id(lst))


def shuffle_list(list_to_shuffle):
    for element in list_to_shuffle:
        first_random_index = random.randint(0, len(list_to_shuffle) - 1)
        second_random_index = random.randint(0, len(list_to_shuffle) - 1)
        list_to_shuffle[first_random_index], list_to_shuffle[second_random_index] = list_to_shuffle[
                                                                                        second_random_index], \
                                                                                    list_to_shuffle[first_random_index]
    return list_to_shuffle


print('--------------------------')
print(shuffle_list(lst))
print(len(lst))
print(id(lst))


print('------------------------')
print('------------------------')
print('------------------------')

import random

lst = [i for i in range(1, 100) if i % 2 != 0]
print(lst)
print(id(lst))

sequence_number = len(lst)
while sequence_number > 1:
    sequence_number = sequence_number - 1
    rand_number = random.randint(0, sequence_number)
    lst[rand_number], lst[sequence_number] = lst[sequence_number], lst[rand_number]

print(lst)
print(id(lst))