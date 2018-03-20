# hw 19
# Написать функцию для поиска разницы между максимальным и минимальным числом среди
# num_limit случайно сгенерированных чисел в указанном числовом диапазоне.
# def diff_min_max(num_limit, lower_bound, upper_bound): # returns int
#     pass


import random


def diff_min_max(num_limit, lower_bound, upper_bound):
    curr_min = upper_bound
    curr_max = lower_bound
    for i in range(num_limit):
        rand_num = random.randint(lower_bound, upper_bound)
        print(rand_num)
        if curr_min > rand_num:
            curr_min = rand_num
        if curr_max < rand_num:
            curr_max = rand_num
    print()
    print('Min = %d, Max = %d' % (curr_min, curr_max))

    result = curr_max - curr_min
    return result

print('Задание 19'
      '\nНаписать функцию для поиска разницы между максимальным и минимальным числом среди'
      '\nnum_limit случайно сгенерированных чисел в указанном числовом диапазоне.'
      '\n'
      '\ndef diff_min_max(num_limit, lower_bound, upper_bound): # returns int'
      '\n       pass'
      '\n')


num_limit = int(input('Enter num limit: '))
lower_bound = int(input('Enter lower bound: '))
upper_bound = int(input('Enter lower bound: '))
print('Difference:', diff_min_max(num_limit, lower_bound, upper_bound))
