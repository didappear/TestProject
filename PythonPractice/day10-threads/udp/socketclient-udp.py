#!/usr/bin/env python
#-*- coding:utf-8 -*-

import socket

c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# 只有通信循环，没有链接循环
while True:
    msg = input('小写变大写>>>').strip()
    c.sendto(msg.encode('utf-8'),('127.0.0.1',8080))
    s_msg,s_addr = c.recvfrom(1024)
    print('from server:%s, msg: %s' %(s_addr, s_msg))

