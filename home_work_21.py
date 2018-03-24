# hw 21
# Написать функцию возвращающую наибольшую цифру случайно сгенерированного
# 12 ти-значного натурального числа.
# def get_max_digit(number): # returns int
#     pass


print('Задание 21'
      '\nНаписать функцию возвращающую наибольшую цифру случайно сгенерированного'
      '\n12 ти-значного натурального числа.'
      '\ndef get_max_digit(number): # returns int'
      '\n       pass'
      '\n')


def get_max_digit(number):
    max_num = 0
    print('Введенное / сгенерированное число: ', number)
    for num in str(number):
        # print(num)
        if max_num < int(num):
            max_num = int(num)
        # print(min_num)
        # print()
    return max_num


number = int(input('Enter number: '))
print('Максимальная цифра: ', get_max_digit(number))
