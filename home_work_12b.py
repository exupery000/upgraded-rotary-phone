# hw12
# Написать функцию, которая рассчитывает сумму всех цифр некоторого трехзначного числа,
# введенного пользователем в консоли, без использования операторов цикла.
# a) cо строками,
# б) без использования строк.
# def sum_of_digits(number): # returns int
# 			pass
#

# Выполним способом "б", подсказка от Артура =)


def sum_of_digits(number):
    first_digit = number // 100
    second_digit = (number % 100) // 10
    third_digit = number % 10
    sum = first_digit + second_digit + third_digit
    return sum

print("Задание 12"
      "\nНаписать функцию, которая рассчитывает сумму всех цифр некоторого трехзначного числа,"
      "\nвведенного пользователем в консоли, без использования операторов цикла.")

print()
number = int(input('Введите исходные данные - 3-х значное число: '))

print("Сумма цифр числа равна:", sum_of_digits(number))
