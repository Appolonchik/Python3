#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Пользователь вводит два целых числа: a и в.
Ввыведите числа от а до в включительно,
в порядке возрастания, если а < в, или в
порядке убывания в противном случае.'''

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

if a < b:
    for i in range(a,b + 1):
        print(i, end = ' ')
else:
    for i in range(a,b - 1, - 1):
        print(i, end = ' ')

print('\nEND')
