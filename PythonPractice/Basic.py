#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "LJ"
# Date: 2019/1/10
'''
# 1、使用while循环输入 1 2 3 4 5 6 8 9 10（没有7）
i = 1
while i < 11:
    if i == 7:
        i += 1
        continue
    print(i)
    i = i + 1

# 2、求1-100的所有数的和
x = 1
y = 0
while x < 101:
    y = y + x
    x += 1

print('1-100所有数的和为：%s'%y)

# 3、输出 1-100 内的所有奇数
x = 1
while x < 100:
    if x%2 != 0:
        print('本次奇数为：%s' %x)
    x += 1

# 4、输出 1-100 内的所有偶数
x = 1
while x < 100:
    if x%2 == 0:
        print('本次偶数为：%s' %x)
    x += 1

# 5、求1-2+3-4+5 ... 99的所有数的和
a = 1
b = 0
while a < 100:
    if a%2 != 0:
        b = b + a
    else:
        b = b - a
    a += 1
print('1-2+3-4+5 ... 99的所有数的和：%s' %b)


# 6、公鸡5文钱一只，母鸡3文钱一只，小鸡1文钱3只，用100文钱买100只鸡,其中公鸡，母鸡，小鸡都必须要有，问公鸡，母鸡，小鸡要买多少只刚好凑足100文钱？
# 5x<100; 3y<100; z/3<100
# 5x + 3y + z/3 == 100; x + y + z == 100
for x in range(1,21):
    for y in range(1,34):
        for z in range(1,301):
            # money = 5*x + 3*y + z/3
            if 5*x + 3*y + z/3 == 100 and x + y + z == 100:
                print('公鸡：%s，母鸡：%s，小鸡：%s' %(x,y,z))



# 7、用户登陆（三次机会重试）
import getpass
i = 1
while i < 4:
    user = input("请输入用户名：")
    # getpass用户输入时不显示，但注意：只能在终端用，pycharm中不生效
    # pwd = getpass.getpass("请输入密码：")
    pwd = input("请输入密码：")
    if user == "amy" and pwd == "123":
        print("登录成功！")
        break
    else:
        print("用户名或密码错误，请重新输入！")
        i += 1

# name = input("请输入用户名：")
# print(name)
#
# import getpass
# pwd = getpass.getpass("请输入密码：")
# print(pwd)

content = "成员变量"
if "成员" in content:
    print("包含")
else:
    print("不包含")

'''
# name = "我叫艾米，今年18岁。"
# # 字符串反向输出
# list = []
# for i in name:
#     list.append(i)
# print(list[::-1])

name = ' aleX'
'''
v1 = name.strip()
print(v1)

v2 = name.startswith('al')
print(v2)

v3 = name.endswith('X')
print(v3)

# v4 = name.replace('l','p')
# print(v4)

# v5 = name.split('l')
# print(v5) #得到的值为列表 [' a', 'eX']

# vg = name.upper()
# print(vg)

# vh = name.lower()
# print(vh)

# i.name变量对应的值的第2个字符
# vi = name[1]
# print(vi)

# j. name变量对应的值的前3个字符
# vj = name[:3:]
# print(vj)

# k.输出name变量对应的值的后2个字符
vk = name[-2::]
print(vk)

# l.输出name变量对应的值中“e”所在索引的位置
vl = name.find('e')
print(vl)

# m.获取子序列，仅不包含最后一个字符。如：root获取roo
str_len = len(name) - 1
vm = name[0:str_len]
print(vm)

'''
# Pyton基础知识联系题二，习题3
li = ['alex', 'eric', 'rain']

# va = len(li)
# print(va)
#
# li.append('seven')
# print(li)

# #添加
# li.insert(0, 'Tony')
# print(li)

# #修改
# li[1] = 'Kelly'
# print(li)

# #删除
# li.remove('eric')
# print(li)

# # f.删除列表中的第2个元素，并输出删除的元素和源列表
# vg = li.pop(1)
# print(vg)
# print(li)

# # g.删除列表中的第3个元素，并输出删除元素后的列表。
# del li[2]
# vf = li.pop(2)
# print(vf)
# print(li)

# # h.删除列表中的第2到第3个元素，并输出删除元素后的列表。
# del li[1:3]
# print(li)

# # i.将列表中的所有元素反转，并输出反转后的列表
# li.reverse()
# print(li)

# # j.使用for、len、range输出列表的索引。
# list_len = len(li)
# for i in range(0,list_len):
#     print(i)
#     ele = li[i]
#     print(ele)


# k.使用enumrate输出列表元素和序号（序号从100开始）

# # i.使用for循环输出列表的所有元素
# for i in  li:
#     print(i)