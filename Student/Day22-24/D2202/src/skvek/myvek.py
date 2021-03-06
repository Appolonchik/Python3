#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# myvek.py
#
from decimal import Decimal
from math import sqrt, floor, degrees, radians, sin, cos, atan2

class InssufficientData(Exception): 
    pass
class ALotofData(Exception):
    pass
class NotCorrectData(Exception):
    pass

TOCHNOST = Decimal('0.01')

class Vektor(object):
    
    def __init__(self, *, x=None, y=None, alfa=None, r=None):
        if not x is None: # Пользователь указал x
            if y is None:
                raise InssufficientData('Have x, but no y')
            else:
                if not alfa is None or r != None:
                    raise ALotofData('Указали x, а еще r или alfa ;-(')
        else: # Пользователь не указал х. Должно быть только r и alfa
            if not y is None:
                raise InssufficientData('Have y, but no x')
            else:
                if alfa is None or r is None:
                    raise InssufficientData('No alfa or no r')
                
            
        if not x is None: # Пользователь ввел x и y
            if not (
                    isinstance(x, (int,float, Decimal)) 
                    and isinstance(y, (int, float, Decimal))):
                raise NotCorrectData('x and y should be int of float')
            self.__vx = Decimal(x).quantize(TOCHNOST)
            self.__vy = Decimal(y).quantize(TOCHNOST)
            self.__valfa = Decimal(degrees(atan2(y, x))).quantize(TOCHNOST)
            self.__vr = Decimal(sqrt(x*x+y*y)).quantize(TOCHNOST)
            
        else: # Пользователь ввел r и alfa
            if not (
                    isinstance(r, (int,float, Decimal)) 
                    and isinstance(alfa, (int, float, Decimal))):
                raise NotCorrectData('r and alfa should be int of float') 
            if r < 0:
                raise NotCorrectData('r souuld be >= 0')
            _alfa = alfa - floor((alfa+180) / 360) * 360
            self.__valfa = Decimal(_alfa).quantize(TOCHNOST)
            self.__vr = Decimal(r).quantize(TOCHNOST)
            self.__vx = Decimal(r * cos(radians(_alfa))).quantize(TOCHNOST)
            self.__vy = Decimal(r * sin(radians(_alfa))).quantize(TOCHNOST)
            
    def output(self):
        print(f'x = {self.__vx:9.4f}, y = {self.__vy:9.4f},    '
              f'alfa = {self.__valfa:9.4f}, r = {self.__vr:9.4f}')
        
    
    @property
    def x(self):
        return self.__vx
    
    @property
    def y(self):
        return self.__vy
    
    @property
    def r(self):
        return self.__vr
    
    @property
    def alfa(self):
        return self.__valfa  
    
    @alfa.setter
    def alfa(self, new_alfa):
        if not isinstance(new_alfa, (int, float, Decimal)):
            raise NotCorrectData('alfa should be int of float')        
        _alfa = new_alfa - floor((new_alfa+180) / 360) * 360
        self.__valfa = Decimal(_alfa).quantize(TOCHNOST)
        self.__vx = Decimal(self.r * Decimal(cos(radians(_alfa)))).quantize(TOCHNOST)
        self.__vy = Decimal(self.r * Decimal(sin(radians(_alfa)))).quantize(TOCHNOST)        
    
    def __str__(self):
        res = f'x={self.x:9.4f} y={self.y:9.4f}    alfa={self.alfa:9.4f} r={self.r:9.4f}'
        return res
    
    def __repr__(self):
        res = f'Vector(x:{self.x:8.4f} y:{self.y:8.4f}    alfa:{self.alfa:8.4f} r:{self.r:8.4f})'
        return res    
    
    def __add__(self, other):
        if isinstance(other, Vektor):
            return Vektor(x=self.x + other.x,
                          y=self.y + other.y)
        else:
            return NotImplemented   
        
    def __sub__(self, other):
        if isinstance(other, Vektor):
            return Vektor(x=self.x - other.x,
                          y=self.y - other.y)
        else:
            return NotImplemented   
        
    def __mul__(self, other):
        if isinstance(other, (int, float, Decimal)):
            return Vektor(x=self.x * Decimal(other),
                          y=self.y * Decimal(other))
        elif isinstance(other, Vektor):
            return (self.x * other.x + self.y * other.y).quantize(TOCHNOST)
        else:
            return NotImplemented
        
    def __rmul__(self, other):
        if isinstance(other, (int, float, Decimal)):
            return Vektor(x=self.x * Decimal(other),
                          y=self.y * Decimal(other))
        else:
            return NotImplemented        
    #__rmul__ = __mul__ - Второй вариант решения чтобы не писать доп. функцию