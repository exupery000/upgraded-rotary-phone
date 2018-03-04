# hw9
print("Задание 9 \n"
      "Написать программу, которая преобразует имя переменной в формате snake_case в формат CamelCase."
      "\nДля простоты считаем, что имя переменной всегда состоит из 3-х слов."
      "\nНапример: ‘employee_first_name’ -> ‘EmployeeFirstName’")
print("Введите переменную, состоящую из 3-х слов разделенных знаком '_'")

var1 = input().split("_", 2)
part1 = var1[0]
part2 = var1[1]
part3 = var1[2]

list = [part1.capitalize(), part2.capitalize(), part3.capitalize()]
print(''.join(list))
