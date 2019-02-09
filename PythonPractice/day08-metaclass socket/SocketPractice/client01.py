#!/usr/bin/env python
#-*- coding:utf-8 -*-

import socket


phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.connect(("127.0.0.1", 8081)) # 拨通电话

while True: # 通信循环
    send_msg = input("请输入>>>").strip()
    if not send_msg: #1.防止客户端发空。服务端收不到空消息。
        continue
    phone.send(send_msg.encode("utf-8")) # 发消息，二进制形式

    back_msg = phone.recv(1024) # 收消息
    print(back_msg.decode("utf-8")) # 消息解码

phone.close()




