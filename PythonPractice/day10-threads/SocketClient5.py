#!/usr/bin/env python
#-*- coding:utf-8 -*-
import socket
# 买手机
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 打电话
client.connect(('127.0.0.1',8080))

if __name__ == '__main__':
    # 通信循环
    while True:
        msg = input('请输入单词>>>').strip()
        # msg为空时，继续循环
        if not msg: continue
        client.send(msg.encode('utf-8'))

        res = client.recv(1024)
        print(res.decode('utf-8'))
