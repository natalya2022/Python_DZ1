# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

a = int(input('Введите номер четверти от 1 до 4 => '))
print (['Неверный номер четверти','х > 0, y > 0','х < 0, y > 0','х < 0, y < 0','х > 0, y < 0'][ 0 if a>4 or a<1 else a ])