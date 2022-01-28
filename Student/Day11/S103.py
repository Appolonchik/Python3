#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' Программа определяет площадь прямоугольного
треугольника по его катетам.'''
a = float(input('Введите первый катет: '))
b = float(input('Введите второй катет: '))
s = a * b / 2
print(a, b, s)
# Очень древний способ печати
print('Площадь с %7.3f и %7.3f равна %8.2f' % (a,b,s))
# Древний способ печати
txt = 'Площадь с {0:7.3f} и {1:7.3f} равна {2:8.2f}' .format(a,b,s)
print(txt)
# Современный способ печати с версии 3.6
print(f'Площадь с {a:7.3f} и {b:7.3f} равна {s:8.2f}')
#print(f'Площадь с {a} и {b} равна {a*b/2*float(input("A: ")):7.3f}')
# Ультрасовременный способ печати с версии 3.8
print(f'Площадь с {a = } и {b = } равна {a*b/2 = }')
print('END')