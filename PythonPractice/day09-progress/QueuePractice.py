#!/usr/bin/env python
#-*- coding:utf-8 -*-

from multiprocessing import Process,Queue

# q = Queue(3)
# q.put({"a":"text1"})
# q.put({"b":"text2"})
# q.put("c")
# print(q.full())
# q.put_nowait("d") # 抛异常：queue.Full
# # q.put("d") # 超出maxsize,卡住
# # q.put("d",block=False) # 超出maxsize，抛异常：queue.Full。等同于q.put_nowait("d")
# # q.put("d", timeout=2) # 等待2秒，抛异常：queue.Full
# print(q.qsize())
#
#
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.empty())
# # print(q.get_nowait()) # 抛异常：queue.Empty
# # print(q.get()) # 取时超出maxsize,卡住
# # print(q.get(block=False)) # 取时超出maxsize,抛异常：queue.Empty
# # print(q.get(timeout=2)) # 等待2秒,如果超出maxsize抛异常：queue.Empty



# 基于队列实现生产者-消费者模型
def customer():
    pass

def producer():
    pass

if __name__ == '__main__': # windows系统下有用
    pass

# 共享数据实现进程间通信

# 进程同步 模拟抢票（注意文件中，字典的字符串要用双引号""，json识别不了单引号）
# 保证每个人来拿，其他人都不能读



