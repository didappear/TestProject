#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
中国人
对象1：张三
    特征:
        国籍=中国
        姓名=张三
        性别=女
        年龄=18
    技能：
        说汉语
        吃饭
        睡觉

对象2：李四
    特征:
        国籍=中国
        姓名=李四
        性别=男
        年龄=28
    技能：
        说汉语
        吃饭
        睡觉



现实中的中国人类
    相似的特征:
        国籍=中国
    相似的技能：
        说汉语
        吃饭
        睡觉
"""

class Chinese:
    country = "China"
    count = 0
    def __init__(self,name,age,gender):
        self.name = name,
        self.age = age,
        self.gender = gender
    count += 1

    def speak(self):
        print("is speaking Chinese")

    def eat(self):
        print('is eating')

    def sleep(self):
        print('is sleeping')

Chinese.country
Chinese.country="China"
Chinese.x = 1
print(Chinese.x)