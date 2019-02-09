#!/usr/bin/env python
#-*- coding:utf-8 -*-
from multiprocessing import Process,Pool
import os
import time
import random

# # print(os.cpu_count()) #4
# # 进程池之回调函数
# def work(num):
#     time.sleep(0.5)
#     return num**2
#
#
# if __name__ == '__main__':
#     p = Pool(processes=6)
#     res_l = []
#     for i in range(6):
#        res = p.apply_async(work,args=(i,)) #收集进程池中创建的对象。\
#        # 进程池中有6个进程，并发运行。每创建一个进程就append到res_l中，\
#        # 所以res_l中存放的对象的顺序是一定的，从第一个开始到最后一个。但是，这个存放顺序和进程并发执行的顺序无关。
#        res_l.append(res) # 只是拿到进程对象，放到列表中有序排开，和并发执行顺序无关。
#
#     # print(res_l) # 打印进程池中创建的所有对象的列表
#     for res in res_l:
#         print(res.get()) # 进程池中所有对象的返回值。为什么结果是有序的？res_l.append(res)是有序的。


# def work(num):
#     print("%s is working" %os.getppid())
#     time.sleep(0.5)
#     return num**2
#
#
# if __name__ == '__main__':
#     p = Pool()
#     obj_l = []
#     for i in range(10):
#        # res = p.apply(work,args=(i,)) # 按顺序一个一个执行，而且规定进程池中有几个进程，就固定用这几个进程。
#        # print(res)
#        obj = p.apply_async(work,args=(i,)) # 一直在异步向操作系统提交任务，提交完整个程序就结束了。\
# # 进程还没来得及创建出来，主进程就结束了。一旦创建，才会执行work中的打印操作。主进程想要拿到结果，就要等进程创建出来并执行
#        obj_l.append(obj)
#     p.close() # 关掉进程池，不能再往里面提交新的任务
#     p.join() # 主进程等待进程池中的任务都执行完。一定要先close()，再join
#     for obj in obj_l:
#         print(obj.get())

# def get_page(url):
#     print('(进程 %s) 获取网页：%s' %(os.getppid(),url))
#     time.sleep(random.randint(1,2))
#     return url # 用url充当下载后的网页
#
# def parse_page(content):
#     print('<进程 %s> 正在解析网页：%s' %(os.getppid(),content))
#     time.sleep(random.randint(1,2))
#     return '%s 回调函数处理结果：%s' %(os.getppid(),content)
#
# if __name__ == '__main__':
#     urls = [
#         'http://maoyan.com/board/1',
#         'http://maoyan.com/board/2',
#         'http://maoyan.com/board/3',
#         'http://maoyan.com/board/4',
#         'http://maoyan.com/board/5',
#         'http://maoyan.com/board/6',
#         'http://maoyan.com/board/7',
#         'http://maoyan.com/board/8'
#     ]
#     p = Pool()
#     obj_l = []
#     # 异步的方式提交任务，任务的返回结果交给callback作为参数进行处理
#     # 主进程处理callback指定的任务
#     for url in urls:
#         obj = p.apply_async(get_page,args=(url,),callback=parse_page)
#         obj_l.append(obj)
#     # 异步任务提交完，主进程先关闭p,然后用p.join()等待所有任务结束（包括callback）
#     p.close()
#     p.join()
#     print('{主进程 %s}' %os.getppid())
#
#     # 本例中，下面这段代码是多余的。
#     # 获取的是异步任务get_page的返回值。所以需要注意：
#     # 1.如果想要将get_page的结果传给parse_page处理，就不需要obj.get()。直接指定callback即可
#     # 2.如果想要在主进程中处理get_page的结果，就需要obj.get()进行获取，再进一步处理。
#     for obj in obj_l:
#         print(obj.get())