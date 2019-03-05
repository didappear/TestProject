#!/usr/bin/env python
#-*- coding:utf-8 -*-


# # 字符串格式化 format
# res4='{} {} {}'.format('amy',18,'female')
# print(res4)
# print('{1},{2},{0}'.format('amy','female',18))
# res6 = '{name}-{gender}-{age}'.format(gender='female',name='amy',age=18)
# print(res6)

# # json序列化
# import json
# # 序列化
# dic = {'name':'amy', 'age':18, 'gender':'female'}
# print(type(dic))
# j = json.dumps(dic)
# print(type(j))
# # 反序列化
# # 不认单引号
# #json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes
# # j_dic = "{'name':'amy', 'age':18, 'gender':'female'}"
# j_dic = '{"name":"amy", "age":18, "gender":"female"}'
# j2 = json.loads(j_dic)
# print(j2)


