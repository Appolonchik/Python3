#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#*****************************************
#src\test_qs.py
#*****************************************

'''Программа должна спросить у пользователя количество точек
для сортировки. Число точек должно находиться в заданном диапазоне.
Необходимо создать список со случайными числами по колличеству точек.
Применить нашу, которую напишем, быструю сортировку для этого списка.
Посчитать время сортировки и сравнить с временем штатной сортировки.
Необходимо вывести статистику по отсортированному массиву.'''

import bisort as bs

n = bs.sprosi_chislo()
print(n)

print('END')
