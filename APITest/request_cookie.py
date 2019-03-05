#!/usr/bin/env python
#-*- coding:utf-8 -*-


import requests
import json

# # 1.获取cookie
# url = "http://www.baidu.com"
# r = requests.get(url)
# # 将RequestsCookieJar转换成字典
# c = requests.utils.dict_from_cookiejar(r.cookies)
#
# print(r.cookies)
# print(c)
#
# for a in r.cookies:
#     print("a.name====>%s\na.value====>%s"%(a.name,a.value))


# # 2.发送cookie
# host = 'http://127.0.0.1:8000/' # 开启http://httpbin.org/服务
# endpoint = 'cookies'
# url = ''.join([host,endpoint])
# print(url)
# # 方式一：简单发送
# cookies = {"name":"amy"}
# r_sample = requests.get(url,cookies=cookies)
# print(r_sample.text)
#
# # 方式二：复杂发送？？？
# host = 'http://httpbin.org/' # 开启http://httpbin.org/服务
# endpoint = 'cookies'
# url = ''.join([host,endpoint])
# s2 = requests.session() # 初始化一个session对象
# # AttributeError: requests对象没有属性cookies、'RequestsCookiesJar'
# jar = requests.cookies.RequestsCookiesJar()
# jar.set('test-key','test-value',domain='httpbin.org',path='/xxx/uuu')
#
# s2.cookies.update(jar) # 更新-已存在于服务中的信息
# r_complex = s2.get(url,cookies=jar)
# print(r_complex.text)

##########


# ################## 官网示例练习 ##################
# # 响应中的cookie
# url = "http://example.com/some/cookie/setting/url"
# r = requests.get(url)
# # print(r.cookies)
# r.cookies["example_cookie_name"]

# # 访问响应中的cookie
# url = 'http://example.com/some/cookie/setting/url'
# r = requests.get(url)
#
# r.cookies['example_cookie_name']

# # 使用 cookies 参数，发送cookies到服务器
# host = 'http://127.0.0.1:8000/' # 开启http://httpbin.org/服务
# endpoint = 'cookies'
# url = ''.join([host,endpoint])
# cookies = dict(cookies_are = "working")
#
# r = requests.get(url,cookies=cookies)
# print(r.text)


#Cookie 的返回对象为 RequestsCookieJar，它的行为和字典类似，但接口更为完整，适合跨域名跨路径使用。
# 可以把 Cookie Jar 传到 Requests 中：
# jar = requests.cookies.RequestsCookieJar()
# jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
# jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
# url = 'http://httpbin.org/cookies'
# r = requests.get(url, cookies=jar)
# print(r.text)

# Cannot find reference 'cookies' in '__init__.py
j = requests.cookies.RequestsCookieJar()
# /cookies路径下发送成功，其他路径失败
j.set('test-name','amy',domain='httpbin.org',path='/cookies')
j.set('test-gender','female',domain='httpbin.org',path='/elsewhere')
url = 'http://httpbin.org/cookies'
r = requests.get(url,cookies=j)
# print(r.text)

# 方式二：cookies的复杂发送
url = 'http://httpbin.org/cookies' # 开启http://httpbin.org/服务
ses = requests.session()

jar1 = requests.cookies.RequestsCookieJar()
jar1.set('test-key','test-value',domain='httpbin.org',path='/cookies')
ses.cookies.update(jar1) # 更新-已存在于服务中的信息

jar2 = requests.cookies.RequestsCookieJar()
jar2.set('test-name','amy',domain='httpbin.org',path='/cookies')
# jar2.set('test-name','amy',domain='httpbin.org',path='/xxx/uuu')

coo = {"cookies_are":'working'}

r_complex = ses.get(url,cookies=jar2)
print(r_complex.text)


