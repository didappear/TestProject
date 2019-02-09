#!/usr/bin/env python
#-*- coding:utf-8 -*-
from gevent import monkey; monkey.patch_all()
import socket
import gevent

"""
单线程实现Socket
"""

# 链接循环 -- 并发的是链接
def server(ip,port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((ip, port))
    server.listen(5)

    while True:
        conn, addr = server.accept()
        # print('client %s:%s' % (addr[0], addr[1]))
        gevent.spawn(talk,conn,addr)

def talk(conn,addr):
    # 通信循环
        try:
            while True:
                msg = conn.recv(1024)
                # msg为空，结束循环
                if not msg: break
                print('client %s:%s, msg: %s' %(addr[0], addr[1], msg))
                conn.send(msg.upper())
        except Exception as e:
            print(e)
        finally:
            conn.close()


if __name__ == '__main__':
    server('127.0.0.1',8080)
