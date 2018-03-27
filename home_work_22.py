# hw 22
# Случайным образом программа выбирает целое число от 1 до 10 и предлагает пользователю его угадать.
# Пользователь вводит число, а программа проверяет его и, если пользователь не угадал,
# то говорит больше или меньше. После чего опять просит угадать.
# И так пока пользователь не угадает выбранное число.


print('Задание 22'
      '\nСлучайным образом программа выбирает целое число от 1 до 10 и предлагает пользователю его угадать.'
      '\nПользователь вводит число, а программа проверяет его и, если пользователь не угадал,'
      '\nто говорит больше или меньше. После чего опять просит угадать.'
      '\nИ так пока пользователь не угадает выбранное число.'
      '\n')


import random


def greeting():
    print('---------')
    print('Let\'s play!')
    print('Try to guess the number that I made')
    print('Please make your choice: ')
    print('From 1 to 10')
    print('---------')
    print('q: Exit')


def game():
    while True:
        print('Hello user!')
        greeting()
        computer_choice = random.randint(1, 10)

        while True:
            user_choice = input('> ')
            if user_choice == 'q':
                print('Bye!')
                return False

            valid_user_choice = user_choice.isnumeric() and 1 <= int(user_choice) <= 10
            if not valid_user_choice:
                print('Enter valid data: 1..3 or \'q\'')

                continue
            user_choice = int(user_choice)
            if computer_choice == user_choice:
                print('===========================')
                print('You Win! Your number is %d and my number is %d ' % (user_choice, computer_choice))
                print('Game Over!')
                print('===========================')
                break

            elif computer_choice > user_choice:
                print('===========================')
                print('Wrong! =( Too low, choose above')
                print('===========================')

            else:
                print('===========================')
                print('Wrong! =( Too high, choose below')
                print('===========================')


game()
