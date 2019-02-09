#!/usr/bin/env python
#-*- coding:utf-8 -*-


import socket
import subprocess

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #买手机
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) # 重用IP地址
phone.bind(("127.0.0.1",8080)) #插电话卡
# 允许监听的数量
phone.listen(5) #开机

# 链接循环
while True:
    print("starting……")
    # 等待接收客户端消息：
    conn, addr = phone.accept() #接电话。
    print("address is %s", addr)
    # 与conn的通信循环
    while True:
        try:
            cmd = conn.recv(1024) #收消息
            if not cmd:
                break
            print("cmd is %s" %cmd)
            res = subprocess.Popen(cmd.decode('utf-8'),shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            err = res.stderr.read()
            if err:
                cmd_res = err
            else:
                cmd_res = res.stdout.read()
            conn.send(cmd_res) #发消息
        except Exception: #万能异常，什么异常都包括在内。
            break
    conn.close()
phone.close()
