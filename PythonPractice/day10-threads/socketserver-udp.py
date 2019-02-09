#!/usr/bin/env python
#-*- coding:utf-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1',8080))

# 只有通信循环，没有链接循环
while True:
    client_msg, client_addr = s.recvfrom(1024)
    print(client_msg)
    s.sendto(client_msg.upper(),client_addr)
