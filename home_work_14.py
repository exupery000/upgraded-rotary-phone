# hw14
# Написать функцию, которая будет проверять четность некоторого числа.
# def is_even(number): # returns boolean value
#           pass

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


print('Задание 14'
      '\nНаписать функцию, которая будет проверять четность некоторого числа'
      '\ndef is_even(number): # returns boolean value'
      '\n       pass')

n = int(input('Enter a number: '))

if is_even(n):
    print('Number ' + str(n) + ' is Even!')
else:
    print('Number ' + str(n) + ' is Uneven!')
