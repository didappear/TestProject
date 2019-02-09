#!/usr/bin/env python
#-*- coding:utf-8 -*-


# ################# 练习：计算圆的周长 #################
from math import pi

class Circle:
    def __init__(self,radius):
        self.radius = radius

    @property
    def area(self):
        area = pi * (self.radius ** 2)
        return area

    @property
    def perimeter(self):
        perimeter = 2 * pi * self.radius
        return perimeter

c = Circle(10)
print(c.radius)
print(c.area)
print(c.perimeter)
