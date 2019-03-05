#!/usr/bin/env python
#-*- coding:utf-8 -*-



# session
import requests
import json
# # 1.保持会话同步
# url1 = 'http://httpbin.org/cookies' # http://127.0.0.1/cookies
# url2 = "http://httpbin.org/cookies/set/sessioncookie/123456789"
#
# r1 = requests.get(url1)
# print(r1.text) # 没有cookies
# print("================")
#
# s = requests.session()
# r2 = s.get(url2) #cookie的信息存在了session中
# print(r2) # <Response [200]>
# print("================")
#
# r1_1 = s.get(url1)
# print(r1_1.text)

# # 2.保存会话信息
# host = "http://127.0.0.1:8000/"
# endpoint = "headers"
#
# url = ''.join([host,endpoint])
# header1 = {"test-name":"amy"}
# header2 = {"test-class":"3.2"}
#
# s = requests.session() #初始化一个session对象
# s.headers.update(header1) # 更新-已经存在于服务中的信息
# r = s.get(url,headers=header2) # 增加-发送的新信息
#
# print(r.text)

# # 3、删除已存在的会话信息，保存为None
# host = "http://127.0.0.1:8000/"
# endpoint = "headers"
#
# url = ''.join([host,endpoint]) #http://127.0.0.1/cookies
#
# header1 = {"test-name":"amy"}
# header2 = {"test-course":"python"}
#
# s = requests.session()
# s.headers.update(header1) # 已经存在于服务中的信息，会话层
# r1 = s.get(url,headers=header2) #发送新的信息，方法层
#
# print(r1.text)
# print("==============")
# s.headers["test-name"] = None #删除session里的指定信息
# r2 = s.get(url,headers = header2)
# # print(r2.text)


# # 4.提供默认数据
# s4 = requests.session()
# s4.auth = ('user','pass')
# s4.headers.update({'x-test1':'true'})
# # both 'x-test1' and 'x-test2' are sent
# r4 = s4.get('http://httpbin.org/headers',headers={'x-test2':'true'})
# print(r4.text)


# ############### 官网示例练习 ###############
# session对象具有主要的 Requests API 的所有方法。
# 包含在一个会话中的所有数据你都可以直接使用

# 1.跨请求保持一些 cookie
# 在同一个 Session 实例发出的所有请求之间保持 cookie
# s = requests.session()
# s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
# r = s.get("http://httpbin.org/cookies")
#
# print(r.text)

# # 2.通过为session对象的属性提供数据,为请求方法提供缺省数据/默认数据
# s = requests.session()
# s.auth = ('user', 'pass') #权限认证
# s.headers.update({'x-test':'true'})
#
# r1 = s.get('http://httpbin.org/headers', headers={'x-test2':'false'})
# r2 = s.get('http://httpbin.org/headers', headers={'x-test2':'false','x-test':'amytest'})
# # 任何我们传递给请求方法的字典都会与已设置的会话层数据合并。方法层的参数覆盖会话的参数。
# print(r1.text) # "X-Test": "true"
# print(r2.text) # "X-Test": "amytest"

# # 3.需要注意，就算使用了会话，方法级别的参数也不会被跨请求保持。
# s = requests.session()
# r1 = s.get('http://httpbin.org/cookies', cookies={'from_my':'browser'})
# print(r1.text)
# print("===========")
# r2 = s.get('http://httpbin.org/cookies')
# print(r2.text)

# 4.会话还可以用作前后文管理器,确保 with 区块退出后会话能被关闭，即使发生了异常
# with requests.session() as s:
#     r = s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
#     print(r.text)

# 从字典参数中移除一个值
# 省略字典参数中一些会话层的键。只需在方法层参数中将那个键的值设置为 None
s = requests.session()
url = 'http://httpbin.org/headers'

header1 = {'x-test1':'true'}
header2 = {'x-test1':None,'x-test2':'false'} # 删除会话层的键值对/元素
s.headers.update(header1) # 会话层参数
r = s.get(url,headers=header2) # 方法层参数

print(r.text)