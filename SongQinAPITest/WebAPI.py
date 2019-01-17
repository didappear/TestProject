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
    print(retDict)

    return retDict,res.cookies


# 添加课程，sessionid 哪里来的？
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



# 列出课程
def list_course(sessionid):
    params = {
        'action':'list_course',
        'pagenum':'1',
        'pagesize':20
    }
    res = requests.get('http://localhost/api/mgr/sq_mgr/',
                       params = params,
                       cookies = {'sessionid':sessionid})
    # 获取结果，返回给调用者
    retList = res.json()
    pprint.pprint(retList)
    print(retList)

    return retList

# 修改课程
# python3.5不支持 'F' prefix
def modify_course(courseid,name,desc,displayidx,sessionid):
    pl = {
        'action':'modify_course',
        'id':courseid, # 为什么这里的courseid直接使用，delete中的需要用字符串格式？？？
        'newdata': ''' 
        {{
            'name':'{name}',
            'desc':'{desc}',
            'display_idx':'{displayidx}'
        }}
        '''
    }
    res = requests.put('http://localhost/api/mgr/sq_mgr/',
                        data=pl,
                        cookies = {'sessionid':sessionid})
    retDict = res.json()
    print(retDict)

    return retDict


# 删除课程
def delete_course(courseid,sessionid):
    pl = {
        'action':'delete_course',
        'id':'{courseid}' #为什么这里要用字符串格式？
    }

    res = requests.delete('http://localhost/api/mgr/sq_mgr/',
                          data = pl,
                          cookies = {'sessionid':sessionid})
    r = res.json()
    pprint.pprint(r)

    return r