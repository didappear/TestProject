#!/usr/bin/env python
#-*- coding:utf-8 -*-



# #1.不带参数的get
# import requests
# import json
# host = 'http://127.0.0.1:8000/' # http://httpbin.org/
# endpoint = 'get'
#
# url = ''.join([host,endpoint]) # http://127.0.0.1:8000/get
# r = requests.get(url)
# res = r.json() # json序列化
# print(type(r.text))
# print(eval(r.text)) # 把字符串形式的字典转成字典格式
# print(res)


# # 2.带参数的get，get(url, params=None, **kwargs)
# 参数可以作为位置参数、关键字参数
# import requests
# host = 'http://127.0.0.1:8000/' # http://httpbin.org/
# endpoint = 'get'
# url = ''.join([host,endpoint])
# params = {"show_env":"1"}
# # r = requests.get(url,params)
# r = requests.get(url=url,params=params)
# # 状态响应码
# print("r.status_code====>\n%s" %r.status_code)
# # 状态原因
# print("r.reason====>\n%s" %r.reason)
# # 返回cookies
# print("r.cookies====>\n%s" %r.cookies)
# #响应对象：Unicode类型
# # print("r.text====>\n%s" %eval(r.text))
# #响应对象：btyes类型
# # print("r.content====>\n%s" %r.content.decode('utf-8'))
# # requests内置的json解码器
# # print("r.json()====>\n%s" %r.json())
# # 编码方式
# print("r.encoding====>\n%s" %r.encoding)
# # 最终的url
# print("r.url====>\n%s" %r.url)
# # 返回请求消息的报头
# print("r.request.headers====>\n%s" %r.request.headers)
# # 以字典对象存储服务器响应头，若键不存在则返回None
# print("r.headers====>\n%s" %r.headers)
# #
# print("r.history====>\n%s" %r.history)
# # 返回原始响应体，也就是urllib的response对象，使用r.raw.read()读取
# print("r.raw====>\n%s" %r.raw)
# print("r.raw====>\n%s" %r.raw.read())
# # 失败请求抛出异常（非200请求）
# print("r.raise_for_status()====>\n%s" %r.raise_for_status())


# # 3.带header的get
# import requests
# import json
# host = 'http://127.0.0.1:8000/' # http://httpbin.org/
# endpoint = 'get'
# url = ''.join([host,endpoint])
# headers = {
#     "User-Agent":"test request headers"
# }
# # r = requests.get(url)
# r = requests.get(url,headers=headers)
# print(r.json())
# print(eval(r.text))
# print(eval(r.text)['headers']['User-Agent'])


#4、同时带参数和header:
import requests
import json
host = 'http://127.0.0.1:8000/' # http://httpbin.org/
endpoint = 'get'
url = ''.join([host,endpoint])
headers = {
    "User-Agent":"test request headers"
}
params = {"show_env":1}
r = requests.get(url=url,params=params,headers=headers)
res = r.json()
print(r.url)
print(eval(r.text)['headers']['User-Agent'])















