#!/usr/bin/env python
#-*- coding:utf-8 -*-

import socket
import sys

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.connect(("127.0.0.1", 8080)) # 拨通电话

while True: # 通信循环
    send_cmd = input("请输入>>>").strip()
    if not send_cmd: #1.防止客户端发空。服务端收不到空消息。
        continue
    phone.send(send_cmd.encode("utf-8")) # 发消息，二进制形式

    cmd_res = phone.recv(1024) # 收消息
    os_encoding = sys.getdefaultencoding()
    print(cmd_res.decode(os_encoding)) # 消息解码

phone.close()




