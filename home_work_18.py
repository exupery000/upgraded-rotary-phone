# hw18
# Каждому символу в таблице символов Unicode соответствует число.
# Написать функцию, которая рассчитывает сумму чисел, которые соответствуют символам,
# стоящим между двумя заданными включительно. Например, в функцию передаются символы ‘x’ и ‘z’.
# Значит надо вычислить сумму кодов символов ‘x’,’y’,’z’.
# def sum_symbol_codes(first, last): # returns int
# 			pass


print('Задание 18'
      '\nКаждому символу в таблице символов Unicode соответствует число.'
      '\nНаписать функцию, которая рассчитывает сумму чисел, которые соответствуют символам,'
      '\nстоящим между двумя заданными включительно. Например, в функцию передаются символы ‘x’ и ‘z’.'
      '\nЗначит надо вычислить сумму кодов символов ‘x’,’y’,’z’.'
      '\n'
      '\ndef sum_symbol_codes(first, last): # returns int'
      '\n       pass'
      '\n')


def sum_symbol_codes(first, last):
    if ord(last) == ord(first):
        print('Symbol: "%s", Unicode: %s' % (first, ord(first)))
        res = ord(last)
        return res
    elif ord(first) + 1 == ord(last):
        print('First symbol: "%s", Unicode: %s' % (first, ord(first)))
        print('Last symbol: "%s", Unicode: %s' % (last, ord(last)))
        res = ord(first) + ord(last)
        return res
    else:
        total_num = 0
        for i in range(ord(first), (ord(last) + 1)):
            print('Symbol: "%s", Unicode: %s' % (chr(i), i))
            total_num += i
        return total_num


first = input('Enter first sumbol: ')
last = input('Enter last symbol: ')

print('Sum of symbol codes: ', sum_symbol_codes(first, last))
