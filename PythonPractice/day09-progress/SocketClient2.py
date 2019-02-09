#!/usr/bin/env python
#-*- coding:utf-8 -*-

import socket
from multiprocessing import Process,Pool

# 接收链接
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 链接服务端
client.connect(('127.0.0.1', 8080))

while True:
    msg = input("请输入>>>").strip()
    if not msg: continue
    client.send(msg.encode('utf-8'))
    msg = client.recv(1024)
    res = msg.decode('utf-8')
    print(res)







