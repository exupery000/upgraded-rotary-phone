# 6. Определить является ли строка изограммой
# (https://en.wikipedia.org/wiki/Isogram ),
# т.е. что все буквы в ней за исключением пробелов встречаются только один раз.
# Например, строки 'Питон', 'downstream', 'книга без слов'
# являются изограммами, а само слово 'изограмма' - нет.


# word = input('Type a word to scan for is_isogramm: ')


def is_isogramm(word):
    comparison_lst = []
    for letter in word:
        if letter == ' ':
            comparison_lst.append(letter)
        if letter not in comparison_lst:
            comparison_lst.append(letter)
        # print(sample)

    while len(comparison_lst) == len(word):
        return True
    else:
        return False


var1 = input('Введите слово, которое вы бы хотели проверить: ')
print('Проверим является ли слово "%s" изограммой' % var1)
if is_isogramm(var1):
    print('Да, это изограмма')
else:
    print('Нет, это не изограмма')
