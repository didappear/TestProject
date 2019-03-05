#!/usr/bin/env python
#-*- coding:utf-8 -*-

# post(url, data=None, json=None, **kwargs)
# #1、带数据的post -字典类型，不传时form为空 "form": {},
# import requests
# import json
# host = 'http://127.0.0.1:8000/' # http://httpbin.org/
# endpoint = 'post'
# url = ''.join([host,endpoint])
# data = {"key1":"value1", "key2":"value2"}
#
# r = requests.post(url,data=data)
# res = r.json()
# # print(res)
# print(r.text)
"""
  "form": {
    "key1": "value1",
    "key2": "value2"
  },
"""

#2、带header的post -字典类型
# import requests
# import json
# host = 'http://127.0.0.1:8000/' # http://httpbin.org/
# endpoint = 'post'
# url = ''.join([host,endpoint])
# headers = {"User-Agent":"test request headers"}
#
# r1 = requests.post(url)
# r2 = requests.post(url,headers=headers)
# print(r1.text)
# print(r2.text)


#3、带json的post
# import requests
# import json
# host = 'http://127.0.0.1:8000/' # http://httpbin.org/
# endpoint = 'post'
# url = ''.join([host,endpoint])
# data = {
#     "sites":[
#         {"name":"baidu", "url":"www.baidu.com"},
#         {"name":"douban", "url":"www.douban.com"},
#         {"name":"weibo", "url":"www.weibo.com"},
#     ]
# }
#
# r1 = requests.post(url,json=data)
# print(r1.text)
# r2 = requests.post(url,json=json.dumps(data))
# print(r2.json())


#4、带参数的post
# 以字典类型post请求参数
# import requests
# import json
# host = 'http://127.0.0.1:8000/' # http://httpbin.org/
# endpoint = 'post'
# url = ''.join([host,endpoint])
# params = {
#     "name":"amy",
#     "clas":"3.2"
# }
# r1 = requests.post(url)
# # 'url': 'http://127.0.0.1:8000/post?clas=3.2&name=amy'
# r2 = requests.post(url,params=params)
# print(r1.json())
# print(r2.json())


# #5、普通文件上传
# import requests
# import json
# host = 'http://127.0.0.1:8000/' # http://httpbin.org/
# endpoint = 'post'
# url = ''.join([host,endpoint])
# files = {
#     'file':open('postfile1.txt','rb')
# }
# r = requests.post(url,files=files)
# # print(r.text)
# """
#   "files": {
#     "file": "hello world!\n11111\n22222\n33333"
#   },
#   """
#
#
# #6、定制化文件上传
# # 自定义文件名、文件类型、请求头
# # 字典，key为"files"，vlaue为数组。
# files2 = {
#     "files":('postfile2.JPG',open('postfile2.JPG','rb'),'img/JPG')
# }
# r2 = requests.post(url,files=files2)
# # print(r2.text)
# """
#   "files": {
#     "files": "data:img/JPG;base64,/9j/4AAQSkZJRgABAQAAAQABAAD……
#     }
# """
#
#
# ##7、多文件上传
# # 列表类型，每个元素为数组
# files3 = [
#     ('file01',('postfile1.txt',open('postfile1.txt','rb'))),
#     ('file02',('postfile2.JPG',open('postfile2.JPG','rb'),'image/JPG'))
# ]
# r3 = requests.post(url,files=files3)
# # print(r3.text)
#
#
# # 8、流式上传：打开文件过程中上传
# with open('postfile1.txt','rb') as f:
#     r4 = requests.post(url,data=f)
#
# print(r4.text)

# 发送数据为字符串，数据被直接发送出去
# 举例：Github API v3 接受编码为 JSON 的 POST/PATCH 数据
import requests
import json
url = "https://api.github.com/some/endpoint"
payload = {"some":"data"}
# 自行对 dict 进行编码
# r = requests.post(url,data=json.dumps(payload))
# print(r.text)

# 还可以使用 json 参数直接传递
r = requests.post(url=url,json=payload)
print(r.text)
