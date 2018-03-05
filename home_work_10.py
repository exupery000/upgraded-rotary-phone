# hw10
print("Задание 10 \n"
      "Дана строка вида 'Leo Tolstoy*1828-08-28*1910-11-20'."
      "\nВ этой строке указаны имя писателя и через символ * даты рождения и смерти."
      "\nДаты указаны в формате 'YYYY-MM-DD'."
      "\nТребуется написать программу, которая по переданной строке определит "
      "\nвозраст писателя и распечает его имя и возраст."
      "\nНапример, для строки 'Leo Tolstoy*1828-08-28*1910-11-20' программа должна распечает: 'Leo Tolstoy, 82'."
      "\nДля строки 'Marcus Aurelius*121-04-26*180-03-17' - 'Marcus Aurelius, 59'."
      "\nПримечание: Т.к. имена писателей могут быть разной длины, то индексы символов "
      "\nразделителей ('*', '-') будут разными! Месяцы и дни для определения возраста можно игнорировать."
      )

print()
whole_string1 = input('Введите исходные данные - Имя, Фамилию, дату рождения, дату смерти,'
                      '\nпо примеру: Leo Tolstoy*1828-08-28*1910-11-20: ')

# разобьем строку на 3 части: имя_фамилия, дата рождения, дата смерти
var1 = whole_string1.split('*')

name_surename = var1[0]
birth_date = var1[1]
death_date = var1[2]

# выделим дату рождения
var2 = birth_date.split('-')
birth_year = var2[0]

# выделим дату смерти
var3 = death_date.split('-')
death_year = var3[0]

# посчитаем сколько лет прожил человек
live_year = int(death_year) - int(birth_year)

# вывод финальной информации
final = name_surename + ", " + str(live_year)
print(final)
