#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Пользователь вводит строку из нескольких слов.
Выведите све слова с четными индексами:
>Пользователь строку нескольких '''

print(' '.join(input('>:').split()[::2]))

print('END')
