#!/usr/bin/env python
#-*- coding:utf-8 -*-


try:
    f = open('a.txt',mode='r',encoding='utf-8')
    next(f)
    next(f)
    next(f)
    next(f)
# except Exception as e:
#     print(e)
finally:
    print("执行finally……")
    f.close()
