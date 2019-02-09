#!/usr/bin/env python
#-*- coding:utf-8 -*-

import socket
from multiprocessing import Process

# 买手机
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 重用地址，防止
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 绑卡
server.bind(('127.0.0.1',8080))
# 监听客户端的上限
server.listen(4)

def talk(conn,addr):
    while True: # 通信循环
        try:
            print("连接中……")
            msg = conn.recv(1024)
            if not msg: break
            conn.send(msg.upper())
        except Exception:
            break

if __name__ == '__main__':
# 链接循环
    while True:
        conn,addr = server.accept()
        p = Process(target=talk,args=(conn,addr))
        p.start()