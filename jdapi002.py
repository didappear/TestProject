#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "LJ"
# Date: 2019/1/17

import requests

r = requests.get('https://www.baidu.com/s?ie=UTF-8&wd=requests')
payload = {
    '':'',
}

print(r.text)