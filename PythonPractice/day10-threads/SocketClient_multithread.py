#!/usr/bin/env python
#-*- coding:utf-8 -*-
import socket
from threading import Thread
import threading

def client(server_ip, port):
    # 买手机
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 打电话
    client.connect((server_ip,port))

    count = 0
    while True:
        msg = '%s send msg: %s' %(threading.current_thread().getName(),count)
        client.send(msg.encode('utf-8'))

        res = client.recv(1024)
        print(res.decode('utf-8'))
        count+=1

if __name__ == '__main__':
    # 通信循环
    for i in range(10):
        t = Thread(target=client,args=('127.0.0.1',8080))
        t.start()