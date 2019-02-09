#!/usr/bin/env python
#-*- coding:utf-8 -*-
from greenlet import greenlet
import gevent
import time

# # greenlet基本使用:单线程内任务的直接切换
# def eat(name):
#     print('%s is eating first' %name)
#     g2.switch('amy')
#     print('%s is eating second' %name)
#     g2.switch()
#
# def play(name):
#     print('%s is playing 1' %name)
#     g1.switch()
#     print('%s is playing 2' %name)
#
# g1 = greenlet(eat)
# g2 = greenlet(play)
# g1.switch(name='amy') # 每个greenlet对象可以在第一次switch时传入参数，以后都不需要

# # 顺序执行
# def f1():
#     res = 1
#     for i in range(100000000):
#         res += i
# def f2():
#     res = 1
#     for i in range(100000000):
#         res *= i
# start_time = time.time()
# f1()
# f2()
# end_time = time.time()
# print('顺序执行使用时间为：%s' %(end_time-start_time)) #23.31363606452942
#
# # greenlet单纯切换，降低运行速度。每个任务遇到IO，原地阻塞
# def f1():
#     res = 1
#     for i in range(100000000):
#         res += i
#         gf2.switch()
#
# def f2():
#     res = 1
#     for i in range(100000000):
#         res *= i
#         gf1.switch()
#
# start = time.time()
# gf1=greenlet(f1)
# gf2=greenlet(f2)
# gf1.switch()
# end = time.time()
# print('切换执行使用时间为：%s' %(end-start)) #121.3206000328064

# Gevent之同步与异步
from gevent import monkey; monkey.patch_all()
import time
import gevent
def task(pid):
    time.sleep(0.5)
    print('task %s has done!' %pid)

def synchronize():
    for i in range(10):
        task(i)

def asynchronize():
    g_l = []
    for i in range(10):
        g = gevent.spawn(task,i)
        g_l.append(g)
    gevent.joinall(g_l)

if __name__ == '__main__':
    print('synchronize:')
    synchronize()
    print('asynchronize:')
    asynchronize()


# # Gevent协程应用：爬虫
# from gevent import monkey; monkey.patch_all()
# import gevent
# import requests
# import time
#
# def get_page(url):
#     print("开始下载网页：%s" %url)
#     res = requests.get(url)
#     if res.status_code == 200:
#         print('%s bytes from %s' %(len(res.text),url))
# start = time.time()
# g1 = gevent.spawn(get_page, 'https://www.douban.com/')
# g2 = gevent.spawn(get_page, 'https://www.yahoo.com/')
# g3 = gevent.spawn(get_page, 'https://www.baidu.com/')
# gevent.joinall([g1, g2, g3])
# end = time.time()
# print('爬取网页时间为：%s' %(end-start))


# gevent实现单线程下的socket并发








