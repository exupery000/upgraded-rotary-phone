# hw8
print("Задание 8 \n"
      "Дана строка с именем студента, в которой имя предшествует фамилии, например  ‘Mark Zuckerberg‘."
      "\nНаписать программу, которая преобразует эту строку, ставя фамилию на первое место, а имя на второе."
      "\nТ.е. ‘Mark Zuckerberg‘ -> ‘Zuckerberg Mark‘.")
print("Введите Имя и Фамилию студента")

name_surename = input().split(" ", 1)
a = name_surename[0]
b = name_surename[1]
list = [b, a]
print(' '.join(list))

