#!/usr/bin/env python
#-*- coding:utf-8 -*-

import socket

def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    s.bind(('127.0.0.1',8801))
    s.listen(5)

    while True: # 通信循环
        print('server is working...')
        conn,addr = s.accept()
        recv_data = conn.recv(1024)

        f = open("index-selector1.html",mode="r",encoding="utf-8")
        send_data = f.read()
        # a bytes-like object is required, not 'str'
        conn.sendall(bytes("HTTP/1.1 201 OK\r\n\r\n%s" %send_data,"utf-8"))
        f.close()
        conn.close

if __name__ == '__main__':
    main()
