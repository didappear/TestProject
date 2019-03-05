#!/usr/bin/env python
#-*- coding:utf-8 -*-

from multiprocessing import Process
import random
import time

# # 创建进程，方式1
# def piao(name):
#     print("%s is piaoing" %name)
#     time.sleep(random.randint(1,3))
#     print("%s has piaoed" %name)
#
# postfile1.txt = Process(target=piao, args=("adler",), name="<adler_piao>")
# postfile1.txt.start()
# print("主进程")
#
# # 创建进程，方式2
#
# class Piao(Process):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#     def run(self):
#         print("%s is piaoing" %self.name)
#         time.sleep(random.randint(1,3))
#         print("%s has piaoed" %self.name)
#
# p2 = Piao("Bill")
# p2.start()
# print("还是主进程")

# # 多进程共享一个终端
# def share_terminal(name):
#     print(name)
#
# for i in range(100000):
#     p = Process(target=share_terminal,args=('process name is %s' %i,))
#     p.start()

# 多进程共享一套文件系统
# 开多个会造成冲突
def share_file(filename,content):
    with open(filename,mode='a', encoding='utf-8') as b_file:
        b_file.write(content)

# if __name__ == '__main__':
for i in range(10):
    p = Process(target=share_file,args=('b.txt','process %s\n'%str(i)))
    p.start()








