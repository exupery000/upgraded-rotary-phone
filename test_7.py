# 7. Найти сумму десяти первых чисел ряда Фибоначчи.


def fibonachi_nums(num):
    group1 = 0
    group2 = 1
    fibonachi_sum = 0
    for i in range(num):
        curent = group1 + group2
        group1 = group2
        group2 = curent
        fibonachi_sum = fibonachi_sum + curent
        print('Текущее число Фибоначи %d, текущая сумма %d' % (curent, fibonachi_sum))
    return fibonachi_sum


var1 = int(input('Сумму скольких цифр Фибоначи вы хотите посчитать: '))
print('Общая сумма %d чисел Фибоначи: %d' % (var1, fibonachi_nums(var1)))
