# hw 23
# Согласно древней индийской легенде создатель шахмат за своё изобретение попросил у раджи незначительную,
# на первый взгляд, награду: столько пшеничных зёрен, сколько окажется на шахматной доске,
# если на первую клетку положить одно зерно, на вторую — два зерна, на третью — четыре зерна и т. д.
# Оказалось, что такого количества зерна нет на всей планете (оно равно 2**64 − 1 зерен.
# Посчитайте, начиная с какой клетки по счету, общее количество зерен,
# которое должен был бы отдать раджа изобретателю было больше 1 000 000 зерен
# и сколько конкретно зерен он должен был бы отдать.
# def chess_reward(): # returns 2 ints (cell number and total number of corns)
#     pass


print('Задание 23'
      '\nСогласно древней индийской легенде создатель шахмат за своё изобретение попросил у раджи незначительную,'
      '\nна первый взгляд, награду: столько пшеничных зёрен, сколько окажется на шахматной доске,'
      '\nесли на первую клетку положить одно зерно, на вторую — два зерна, на третью — четыре зерна и т. д.'
      '\nОказалось, что такого количества зерна нет на всей планете (оно равно 2**64 − 1 зерен.'
      '\nПосчитайте, начиная с какой клетки по счету, общее количество зерен,'
      '\nкоторое должен был бы отдать раджа изобретателю было больше 1 000 000 зерен'
      '\nи сколько конкретно зерен он должен был бы отдать.'
      '\n'
      '\ndef chess_reward(): # returns 2 ints (cell number and total number of corns)'
      '\n       pass'
      '\n')


def chess_reward():
    cell_number = 0
    print('\n-----------')
    print('Chess Table:')
    print('-----------')
    for i in range(1, 8 + 1):
        for j in range(1, 8 + 1):
            cell_number += 1
            print('%4d' % cell_number, end=' ')
        print()

    print()
    cell_number = 0
    cur_number_of_corns = 0
    total_number_of_corns = 0
    for i in range(1, 8 + 1):
        for j in range(1, 8 + 1):
            cur_number_of_corns = 2 ** cell_number
            cell_number += 1
            total_number_of_corns += cur_number_of_corns
            print('Номер клетки: %d, '
                  'колличество зерен на клетке: %d, '
                  'общее колличество зерен в этот момент: %d' %
                  (cell_number, cur_number_of_corns, total_number_of_corns))
            if total_number_of_corns >= 1000000:
                print('Вот он! Момент "М"')
                print()
                return cell_number, total_number_of_corns


res1, res2 = chess_reward()
print('Начиная с клетки № %d (включительно) общее колличество зерен будет: %d '
      '\nи продолжит увеличиваться каждый раз в двое' % (res1, res2))