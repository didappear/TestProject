#!/usr/bin/env python
#-*- coding:utf-8 -*-

import socketserver

class MyHandler(socketserver.BaseRequestHandler):
    def handle(self):
            client_msg,s = self.request
            print('client_msg:%s s:%s' %(client_msg, s))
            s.sendto(client_msg.upper(),self.client_address)

s = socketserver.ThreadingUDPServer(('127.0.0.1',8080),MyHandler) #通信循环
s.serve_forever()




