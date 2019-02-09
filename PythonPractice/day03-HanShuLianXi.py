#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "LJ"
# Date: 2019/1/21

"""
# 函数定义
def auth(user:str,password:str)->int:
    '''
    auth function
    :param user: 用户名
    :param password: 密码
    :return: 认证结果
    '''
    if user == 'amy' and password == '123':
        return 1

user=input('用户名>>: ').strip()
pwd=input('密码>>: ').strip()
res=auth(user,pwd)
print(res)

def foo():
    print('from foo')
    bar()
def bar():
    print('from bar')
foo() # 不会报错

"""
# # 序列的解压
# t = (1, 2, 3, 4)
# a, _, _, _= t
# print('a=%s' %a)
#
# p,*_ = t
# print('p=%s' %p)
#
# x, *_, y = t
# print('x=%s, y=%s' %(x,y))

#
# def wrapper(*args,**kwargs):
#     print(args) #args=(1,2,3)
#     print(kwargs) #kwargs={'a':1,'b':2}
# wrapper(1,2,3,a=1,b=2)
#
#
# def foo(x,y,z):
#     print('from foo',x,y,z)
# def wrapper(*args,**kwargs):
#     print(args) #args=(1,2,3)
#     print(kwargs) #kwargs={'a':1,'b':2}
#     # 报错：TypeError: foo() got an unexpected keyword argument 'a'
#     foo(*args,**kwargs) #foo(*(1,2,3),**{'a':1,'b':2}) #foo(1,2,3,b=2,a=1)
# wrapper(1,2,3,a=1,b=2)
#
#
# def foo(x,y,z):
#     print('from foo,x=%s, y=%s, z=%s' %(x,y,z))
#
# def wrapper(*args,**kwargs):
#     print(args) # args=(1,)
#     print(kwargs) # kwargs={'y': 3, 'z': 2}
#     foo(*args,**kwargs) # foo(*(1,),**{'y': 3, 'z': 2}) <==>foo(1,y=3,z=2)
# wrapper(1,z=2,y=3)

# ################## 练习 ##################
# # 1、写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成批量修改操作
# def modify_file(filepath, oldtext, newtext):
#     import os
#     with open(filepath,mode='r',encoding='utf-8') as f_read,\
#         open('swap.txt',mode='w',encoding='utf-8') as f_write:
#         for line in f_read:
#             if oldtext in line:
#                 line = line.replace(oldtext,newtext)
#             f_write.write(line)
#     os.remove(filepath)
#     os.rename('swap.txt',filepath)
#
# modify_file('/Users/kun/Documents/MyCode/PythonPractice/FunctionTest.txt','被测试文本','修改后文本')
#
# # 2、写函数，计算传入字符串中【数字】、【字母】、【空格] 以及【其他】的个数
# def count_str_type(str):
#     res = {
#         'num':0,
#         'string':0,
#         'space':0,
#         'other':0
#     }
#     for i in str:
#         if i.isdigit():
#             res['num'] += 1
#         elif i.isalpha():
#             res['string'] += 1
#         elif i.isspace():
#             res['space'] += 1
#         else:
#             res['other'] += 1
#     print(res)
#     return res
#
# count_str_type('hello Python编程 123 ABC **++**')
#
# # # 3、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
# def tell_len(obj):
#     """
#     :param obj: 字符串、列表、元组
#     :return:
#     """
#     if len(obj) > 5:
#         print('传入对象长度大于5！')
#     else:
#         print('传入对象长度小于5！')
#
# tell_len('hello Python!')
# tell_len([1,2,3,4])
#
#
# # 4、写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# def list_len(list_obj):
#     """
#     :param obj: 列表
#     :return:
#     """
#     if len(list_obj) > 2:
#         new_list = list_obj[0:2]
#     else:
#         print('传入列表长度小于等于2！')
#     return new_list
#
# res = list_len([1,2,3,4])
# print(res)
#
# # 5、写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
# def obj_uneven(obj):
#     '''
#     :param obj:列表或元组
#     :return:
#     '''
#     new_list = obj[::2]
#     return new_list
# # res = obj_uneven(('a','b','c','d','e','f'))
# res = obj_uneven((1,2,3,4,5,6,7))
# print(res)
#
# # 6、写函数，检查字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# # dic = {"k1": "v1v1", "k2": [11,22,33,44]}
# # PS:字典中的value只能是字符串或列表
# def dic_check(dict_obj):
#     new_dict = {}
#     for k,v in dict_obj.items():
#         # new_dict = {} # new_dict 位置错误
#         if len(v) > 2:
#             new_dict[k] = v[0:2]
#         else:
#             new_dict[k] = v
#     return new_dict
# # dic1 = {"k1": "v1v1", "k2": [11,22,33,44]}
# dic2 = {'k1':'abcdef','k2':[1,2,3,4],'k3':('a','b','c'),'k4':'kk'}
# res = dic_check(dic2)
# print(res)

# 用文件处理方式模仿SQL语句增删改查 select insert update delete where
'''
staff_id name age phone dept enroll_date
逗号，分隔
在文件存储时可以这样表示
1,Alex Li,22,13651054608,IT,2013-04-01

现需要对这个员工信息文件，实现增删改查操作
1. 可进行模糊查询，语法至少支持下面3种:
   1. select name,age from staff_table where age > 22
   2. select  * from staff_table where dept = "IT"
   3. select  * from staff_table where enroll_date like "2013"
   4. 查到的信息，打印后，最后面还要显示查到的条数 
2. 可创建新员工纪录，以phone做唯一键，staff_id需自增
3. 可删除指定员工信息纪录，输入员工id，即可删除
4. 可修改员工信息，语法如下:
   1. UPDATE staff_table SET dept="Market" WHERE where dept = "IT"
'''

import os
import shutil
import time

# 将用员工信息存入文件db1.emp
def select(*args,**kwargs):
    print("""请输入查询语句，如：
    1. select name,age from staff_table where age > 22
    2. select  * from staff_table where dept = "IT"
    3. select  * from staff_table where enroll_date like "2013"
    """)
    user_input = input(">>>")
    # 将条件语句以空格" "拆分为列表
    select_list = user_input.split(" ")
    # 查询结果
    found_info = []
    table_title = ['name', 'age', 'phone', 'dept', 'enroll_date']
    with open('staff_table.emp', mode='r', encoding='utf-8') as f:
        for line in f:
            # 每个员工信息
            user_info = line.strip().split(',')

    pass


def insert(*args,**kwargs):
    pass

def update(*args,**kwargs):
    pass

def delete(*args,**kwargs):
    pass



while True:
    print("""员工信息查询：
    1.模糊查询
    2.创建新员工纪录
    3.删除指定员工信息
    4.可修改员工信息
    5.退出
    """)
    menu_dict = {'1':select,'2':insert,'3':update,'4':delete}
    user_input = input("请选择>>").strip()
    if user_input in menu_dict.keys():
        menu_dict[user_input]()
    elif user_input == '5':
        exit('Good Bye!')
    else:
        print("输入错误，请重新选择！")

































