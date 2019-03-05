#!/usr/bin/env python
#-*- coding:utf-8 -*-

import requests


# ############### 一、认证 #################

# # 1、基本认证
# url = 'http://httpbin.org/basic-auth/user/passwd'
# # 未认证
# r1 = requests.get(url)
# print(r1.text)
# print("未提供用户名密码：%s" %r1.status_code)
# # 基本认证
# r2 = requests.get(url, auth=('user','passwd'))
# print("已提供用户名密码：%s" %r2.status_code)

# # 2.数字认证
# from requests.auth import HTTPDigestAuth
# url = 'http://httpbin.org/digest-auth/auth/user/pass'
# r = requests.get(url, auth=HTTPDigestAuth('user','pass'))
# print(r.text)

# 3.OAuth认证


# ############### 二、代理 #################

# # 1、方法一：proxy参数
# proxies = {
#     "https":"http://41.118.132.69:4433"
# }
# r = requests.post("http://httpbin.org/post", proxies=proxies)
# print(r.text)

# 2、方法二：设置环境变量
"""
$ export HTTP_PROXY="http://10.10.1.10:3128"
$ export HTTPS_PROXY="http://10.10.1.10:1080"

$ python
>>> import requests
>>> requests.get('http://example.org')
"""
# r = requests.get('http://example.org')
# print(r.text)

# # 3、HTTP Basic Auth使用代理方法：http://user:password@host/
# url = "http://httpbin.org/post"
# proxies = {'http':'http://user:password@10.10.1.10:3128/'}
# r = requests.post(url=url, proxies=proxies)
# print(r.text)

# ############## 三、证书验证 #############
# 1.SSL证书（HTTPS）



