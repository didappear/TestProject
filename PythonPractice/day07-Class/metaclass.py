#!/usr/bin/env python
#-*- coding:utf-8 -*-

# class Chinese(object):
#     country = "China"
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def talk(self):
#         print("speak Chinese")
# print(Chinese)
#
# # ####### 模拟类的创建过程 #######
# # 类的三要素：1、类名 2、继承的父类 3、类体的执行结果（类的名称空间）
# # 步骤1、创建类的基本信息
# class_name = "Chinese"
# class_bases = (object,)
# class_body = """
# country = "China"
# def __init__(self,name,age):
#     self.name = name
#     self.age = age
# def talk(self):
#     print("speak Chinese")
# """
# class_dict = {}
# exec(class_body, globals(), class_dict)
#
# # 步骤2、用type实例化出Chinese类
# Chinese2 = type(class_name, class_bases, class_dict)
# print(Chinese2)


# 控制Foo()实例化的过程

class MyMeta(type):
    def __init__(self, cls_name, cls_bases, cls_dic):
        # print(cls_dic) # 这里不调用super()方法能直接打印出结果，是因为MyMeta()执行时自动处理了？？
        for key,value in cls_dic.items():
            if key.startswith("__"):
                continue
            if not callable(value):
                continue
            if not value.__doc__:
                raise TabError("%s 必须要有注释" %key)
        super().__init__(cls_name, cls_bases, cls_dic)

class Foo(metaclass=MyMeta):
    # MyMeta('Foo', (object,), {})
    # MyMeta.__init__(Foo, 'Foo', (object,), {})
    x = 1
    def f1(self):
        '''函数f1'''
        print("Foo.f1")
    def f2(self):
        '''函数f2'''
        print("Foo.f2")









