#!/usr/bin/env python
#-*- coding:utf-8 -*-

import socketserver

# def MyHandler(socketserver.BaseRequestHandler): # 一个不该犯的错误
#     pass

class MyHandler(socketserver.BaseRequestHandler):# 通信循环
    def handle(self):
        while True:
            res = self.request.recv(1024)
            print('client: %s, msg: %s' %(self.client_address, res))
            self.request.send(res.upper())

if __name__ == '__main__':
    # 链接循环
    s = socketserver.ThreadingTCPServer(('127.0.0.1',8080),MyHandler)
    s.allow_reuse_address = True
    s.serve_forever()