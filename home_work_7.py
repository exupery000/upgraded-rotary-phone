# hw7
print("Задание 7 \n"
      "Преобразовать строку с американским форматом даты в европейский. "
      "\nНапример, \"05.17.2016\" преобразуется в \"17.05.2016\"")
print("Введите нужную дату в американском формате: MM.DD.YYYY")
date_american = input()
date_euro = date_american[3:6] + date_american[0:3] + date_american[6:10]
print(date_euro)
