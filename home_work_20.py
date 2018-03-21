# hw20
# Написать функцию для поиска разницы сумм всех четных и всех нечетных чисел
# среди 100 случайно сгенерированных чисел в произвольном числовом диапазоне.
# Т.е. от суммы четных чисел вычесть сумму нечетных чисел.
# def diff_even_odd(num_limit, lower_bound, upper_bound): # returns int
#               pass


import random


def diff_even_odd(num_limit, lower_bound, upper_bound):
    total_even = 0
    total_odd = 0
    for i in range(num_limit):
        rand_num = random.randint(lower_bound, upper_bound)
        print(rand_num, i)
        if rand_num % 2 == 0:
            total_even += rand_num
            # print(total_odd)
            # print(total_even)
            # print()

        else:
            total_odd += rand_num
            # print(total_odd)
            # print(total_even)
            # print()
    print('---------------')
    print('Num of limit:', num_limit)
    print('Lower bound:', lower_bound)
    print('Upper bound:', upper_bound)
    print('Total even:', total_even)
    print('Total odd:', total_odd)
    print('---------------')
    res1 = total_even - total_odd
    return res1


print('Задание 20'
      '\nНаписать функцию для поиска разницы сумм всех четных и всех нечетных чисел'
      '\nсреди 100 случайно сгенерированных чисел в указанном числовом диапазоне'
      '\nТ.е. от суммы четных чисел вычесть сумму нечетных чисел.'
      '\n'
      '\ndef diff_even_odd(num_limit, lower_bound, upper_bound): # returns int'
      '\n       pass'
      '\n')

num_limit = int(input('Enter num limit: '))
lower_bound = int(input('Enter lower bound: '))
upper_bound = int(input('Enter lower bound: '))

print('Difference of even and odd is:', diff_even_odd(num_limit, lower_bound, upper_bound))
