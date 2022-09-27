# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой
# находится эта точка (или на какой оси она находится).

x, y = map(int, input('Введите две координаты точки через пробел: ').split())
if (x == 0 or y == 0):
    print('Точка лежит на оси')
elif (x > 0 and y > 0):
    print('1 четверть')
elif (x < 0 and y > 0):
    print('2 четверть')
elif (x < 0 and y < 0):
    print('3 четверть')
else:
    print('4 четверть')
