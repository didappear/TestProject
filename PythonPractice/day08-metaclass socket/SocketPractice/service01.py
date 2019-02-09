#!/usr/bin/env python
#-*- coding:utf-8 -*-


import socket

# AF_INET：socket internet ，SOCK_STREAM TCP协议。
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #买手机
# 解决OSError: [Errno 48] Address already in use问题。重用IP地址
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
# 绑定服务端地址和端口
phone.bind(("127.0.0.1",8081)) #插电话卡

# 允许监听的数量
phone.listen(5) #开机
# 链接循环
while True:
    print("starting……")
    # 等待接收客户端消息：
    conn, addr = phone.accept() #接电话。服务端基于conn这个链接收消息。
    print("connect is %s,\n address is %s" %(conn,addr))
    # 与conn的通信循环
    while True: #2.客户端终止链接，服务端退出循环
        try: # 针对windows平台下客户端断开链接
            client_msg = conn.recv(1024) #收消息
            if not client_msg: #针对Linux平台下客户端断开链接
                break
            print("client_msg is %s" %client_msg)
            conn.send(client_msg.upper()) #发消息
        except Exception: #万能异常，什么异常都包括在内。通常异常处理加到你无法控制的异常出现时
            break
    conn.close()
phone.close()
"""
windows 平台下客户端单方面断开链接，服务端会抛异常。
linux 平台下客户端单方面断开链接，服务端不会抛异常。服务端conn.recv会一直收空：client_msg is b''，程序会一直与坏了的链接进行死循环。
"""