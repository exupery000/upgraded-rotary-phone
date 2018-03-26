# hw 24
# Для удобства проведения вступительных экзаменов всеx абитуриентов в MIT разбивают на группы
# в зависимости от первых букв их фамилии. Группы называются ‘A-I’, ‘J-P’, ‘Q-T’, ‘U-Z’.
# Название группы определяет в какую группу попадает абитуриент,
# в зависимости от первой буквы его/ее фамилии.
# Например, Will Smith попадает в группу ‘Q-T’,
# т.к. первая буква его фамилии попадает в диапазон букв от ‘Q‘ до ‘Т‘ (включительно!).
# Абитуриент Jay Z попадает в группу ‘U-Z’ и т.д.
# Написать функцию, которая получает список имен студентов вида
# ['Name1 Surname1', 'Name2 Surname2', 'Name3 Surname3', ...] и возвращает количество абитуриентов в группах,
# сформированных по их фамилиям, описанным выше образом.
# def group_by_surname(list_of_enrollees): # returns 4 ints#
#               pass


print('Задание 24'
      '\nДля удобства проведения вступительных экзаменов всеx абитуриентов в MIT разбивают на группы'
      '\nв зависимости от первых букв их фамилии. Группы называются ‘A-I’, ‘J-P’, ‘Q-T’, ‘U-Z’.'
      '\nНазвание группы определяет в какую группу попадает абитуриент, '
      '\nв зависимости от первой буквы его/ее фамилии.'
      '\nНапример, Will Smith попадает в группу ‘Q-T’,'
      '\nт.к. первая буква его фамилии попадает в диапазон букв от ‘Q‘ до ‘Т‘ (включительно!).'
      '\nАбитуриент Jay Z попадает в группу ‘U-Z’ и т.д.'
      '\nНаписать функцию, которая получает список имен студентов вида'
      '\n["Name1 Surname1", "Name2 Surname2", "Name3 Surname3", ...] и возвращает количество абитуриентов в группах,'
      '\nсформированных по их фамилиям, описанным выше образом.'
      '\n'
      '\ndef group_by_surname(list_of_enrollees): # returns 4 ints#'
      '\n       pass'
      '\n')


def group_by_surname(full_names_lst):
    group_a_i = 0
    group_a_i_lst = ''

    group_j_p = 0
    group_j_p_lst = ''

    group_q_t = 0
    group_q_t_lst = ''

    group_u_z = 0
    group_u_z_lst = ''

    for full_names in full_names_lst:
        name_part = full_names.split(' ')
        # print(name_part)
        first_name = name_part[1]
        # print(first_name)
        first_symbol = first_name[0]
        # print(first_symbol)
        # print('-------------------')
        if 'A' <= first_symbol <= 'I':
            group_a_i = group_a_i + 1
            group_a_i_lst = group_a_i_lst + full_names + ', '

        elif 'J' <= first_symbol <= 'P':
            group_j_p = group_j_p + 1
            group_j_p_lst = group_j_p_lst + full_names + ', '

        elif 'Q' <= first_symbol <= 'T':
            group_q_t = group_q_t + 1
            group_q_t_lst = group_q_t_lst + full_names + ', '

        elif 'U' <= first_symbol <= 'Z':
            group_u_z = group_u_z + 1
            group_u_z_lst = group_u_z_lst + full_names + ', '

    print('Группа "A-I"')
    print('Колличество абитуриентов: ', group_a_i)
    print(group_a_i_lst)
    print('-------------------')

    print('Группа "J-P"')
    print('Колличество абитуриентов: ', group_j_p)
    print(group_j_p_lst)
    print('-------------------')

    print('Группа "Q-T"')
    print('Колличество абитуриентов: ', group_q_t)
    print(group_q_t_lst)
    print('-------------------')

    print('Группа "U-Z"')
    print('Колличество абитуриентов: ', group_u_z)
    print(group_u_z_lst)
    print('-------------------')
    return group_a_i, group_j_p, group_q_t, group_u_z


full_names_lst = ['Name1 Aurname1', 'Name2 Burname2', 'Name3 Curname3',
                  'Name1 JJurname1', 'Name2 Purname2', 'Name3 Purname3',
                  'Name1 Qrname1', 'Name2 Turname2', 'Name3 Turname3',
                  'Name1 UJurname1', 'Name2 Uurname2', 'Name3 Zurname3']

group1, group2, group3, group4 = group_by_surname(full_names_lst)
print(group1, group2, group3, group4)
