#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 序列化的过程： dic --> res=json.dumps(dics) -->
# 把字典用json.dumps()转换成json认识的字符串，然后把这个字符串写到文件中
# 反序列化
# 把文件读出来，把json可识别的字符串，用json.loads()转换为对应的数据类型


# ############################### hashlib ###############################
import hashlib

m = hashlib.md5()
m.update('hello'.encode('utf-8'))
print(m.hexdigest())
m.update('world'.encode('utf-8')) # 基于上一次的结果进行校验，helloworld
print(m.hexdigest())


m2 = hashlib.md5()
m2.update('helloworld'.encode('utf-8'))
print(m2.hexdigest())






