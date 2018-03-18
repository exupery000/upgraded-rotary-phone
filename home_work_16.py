# hw16
# Два поезда движутся на скорости V1 и V2 навстречу друг другу.
# Между ними 10 км. пути. Через 4 км пути первый поезд может свернуть на запасной путь.
# При заданных скоростях узнать столкнутся ли поезда.
# def have_trains_crashed(v1, v2): # returns boolean value
#           pass


def have_trains_crashed(v1, v2):
    s1 = 4
    s2 = 6
    t1 = s1 / v1
    t2 = s2 / v2
    if t1 >= t2:
        return True
    else:
        return False


print('Задание 16'
      '\nДва поезда движутся на скорости V1 и V2 навстречу друг другу.'
      '\nМежду ними 10 км. пути. Через 4 км пути первый поезд может свернуть на запасной путь.'
      '\nПри заданных скоростях узнать столкнутся ли поезда.'
      '\n'
      '\ndef have_trains_crashed(v1, v2): # returns boolean value'
      '\n       pass'
      '\n')


velocity1 = int(input('Enter Velocity1: '))
velocity2 = int(input('Enter Velocity2: '))
if have_trains_crashed(velocity1, velocity2):
    print('Столкновение неизбежно!!!')
    print('Столкновение неизбежно!!!')
    print('Столкновение неизбежно!!!')

else:
    print('Путь свободен. Двигайтесь с указанной скоростью.')
