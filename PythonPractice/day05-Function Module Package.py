#!/usr/bin/env python
#-*- coding:utf-8 -*-






# ############################ 协程函数 ############################
# def eater(name):
#     print("%s 准备吃东西" %name)
#     while True:
#         food = yield
#         print("%s 正在吃 %s" %(name, food))
#
# gener = eater("amy")
# next(gener) # <===> gener.send(None)
# gener.send("香菇")


# def start_g(func):
#     def wrapper(*args,**kwargs):
#         g = func(*args,**kwargs)
#         next(g)
#         return g
#     return wrapper
#
# @start_g
# def eater(name):
#     print("%s 准备吃东西" %name)
#     while True:
#         food = yield
#         print("%s 正在吃 %s" %(name, food))
#
# gener = eater("amy")
# gener.send("香菇")


# ############################ 二分法 ############################
li = [1,2,10,5,30,40,33,22,99,31]

li.sort(key=None, reverse=False)
print(li)

def dichotomy(find_num, seq):

    middle = len(li) // 2
    if x == li[middle]:
        print("找到输入值：%s 的索引为：%s" %(x,middle))
    else:
        max_result = max(x,li[middle])
        if x == max_result: # 如果x是最大值，
            pass





















