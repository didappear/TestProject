#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "LJ"
# Date: 2019/1/17

import requests,pprint

#登录
def login(username,password):
    payload = {
        'username':username,
        'password':password
    }
    # 构造请求
    res = requests.post('http://localhost/api/mgr/loginReq',data=payload)
    # 获取请求结果
    retDict = res.json()
    # 打印结果
    pprint(retDict)

    return retDict,res.cookies


# 添加课程，sessionid哪里来的？
def add_course(name,desc,displayidx,sessionid):
    pl = {
        'action':'add_course',
        'data':'''
        {
            'name':'%s',
            'desc':'%s',
            'displayidx':'%s',
        }
        '''  %(name,desc,displayidx)
    }

    res = requests.post('http://localhost/api/mgr/sq_mgr/',
                        data=pl,
                        cookies = {'sessionid':sessionid}
                        )
    retDict = res.json()

    print(retDict)
    return retDict

