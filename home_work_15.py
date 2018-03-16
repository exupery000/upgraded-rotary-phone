# hw15
# Написать функцию, которая отвечает на вопрос, пересекаются ли две заданные окружности на плоскости.
# Каждая окружность задается координатами центра и радиусом.
# def circles_intersect(x1, y1, r1, x2, y2, r2): # returns boolean value
#           pass


def circles_intersect(x1, y1, r1, x2, y2, r2):
    diag_between_centers = ((abs(x1 - x2)) ** 2 + (abs(y1 - y2)) ** 2) ** 0.5
    summ_of_radius = r1 + r2
    difference_of_radius = abs(r1 - r2)
    if r1 < diag_between_centers < summ_of_radius \
            or r2 < diag_between_centers < summ_of_radius \
            or diag_between_centers == summ_of_radius \
            or diag_between_centers == difference_of_radius \
            or difference_of_radius == 0 and diag_between_centers < r1:
        return True
    else:
        return False


print('Задание 15'
      '\nНаписать функцию, которая отвечает на вопрос, пересекаются ли две заданные окружности на плоскости.'
      '\nКаждая окружность задается координатами центра и радиусом.'
      '\n'
      '\ndef circles_intersect(x1, y1, r1, x2, y2, r2): # returns boolean value'
      '\n       pass'
      '\n')


x1 = 60
y1 = 60
r1 = 50

x2 = 75
y2 = 60
r2 = 30


if circles_intersect(x1, y1, r1, x2, y2, r2):
    print('Окружности пересекаются.')
else:
    print('Окружности не пересекаются.')