#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "LJ"
# Date: 2019/1/16

import requests,pprint
'''

'''
request_url = 'api.m.jd.com'

cookies = 'abtest=20171112132916936_40; shshshfpa=d2d66407-afd2-bc74-d1c4-b38fc566ae65-1528783597; shshshfpb=2b18de2272ae34917bd0806352de6fc3a5b2767d781c8306017fc0edc4; __jdu=1526114150885499639638; pinId=rZj5v8dLtuLR8YKtwflTDbV9-x-f3wj7; pin=jd_54397e682436b; unick=jd_130522759; _tp=cakA%2Bu6VpcS3vX5rBe7ukhOnk5sC77jFk%2F7M0ngoAaE%3D; _pst=jd_54397e682436b; user-key=47ce9435-dfaf-4c09-a4b6-96bd23397a3c; PCSYCityID=1; ipLocation=%u5c71%u4e1c; cn=62; jcap_dvzw_fp=41f83b9a1a056118808a424fcf314d6615476334359942051506482; whwswswws=; __jdv=122270672|kong|t_1000000936_0|tuiguang|1fd96477eb864f5c82b23f255a2157f4|1547633621684; _contrast=100002100080.100000109473.100000109455.4939815; areaId=1; ipLoc-djd=1-2901-4135-0.137923460; __jdc=122270672; autoOpenApp_downCloseDate_auto=1547696889895_21600000; downloadAppPlugIn_downCloseDate=1547696917370_86400000; _contrast_status=show; 3AB9D23F7A4B3C9B=CYAIYHMV2QZ5FKG6OIJZF2EFKHYPXITMRC73DTHJOTOYUI3ZWBRLJAGHMCELXJKIRMGXMTDEWGTSISE4XHJK4DOBM4; wlfstk_smdl=6bxwq1cpnbfjw3cwc8ajdm7ocvtyzqq6; TrackID=12nxvzBXPqrlBw-JqL0K5mCd4JqmIUMsJNZQp-DoXL-quv_Df_AOXWnjnz9eqcX070VIrxzMIm6dEVNrpLZtRv9IOHC55gr8uex9zylgss2w; ceshi3.com=201; unpl=V2_ZzNtbRIDQRYiDEYBfRtdAWJRFg1KVRYTIg0WBCwRDABjUEJaclRCFX0UR1RnGVoUZwsZXUtcRhdFCEdkexhdBGYCE1VAUHMURQl2V3spXARXAxZeRVdDEHUMR11yHVkNbwQQVUVVSiVFD3ZkK1ECXjkzEFpHUkQVcwFFZHopXTUsbRMQQlNAEnUIQ1R%2fGFUMYwYaVUVVSxJ3AXZVSxo%3d; CCC_SE=ADC_wHgst6dyQf2KbCTxRy%2f4eZfz6rL%2f1M0dcFsxpDXmyFLNNUnW4FzIjDAjq%2bUXf2iQ%2fKyALodlA2v1Vk%2fxU4lqLny2%2fSTFu9Dd%2bB49pqtc0ZN9e3BE7lAu3dHPfaze140jaX0%2b3sk%2fQlHd%2bpk86Ao54J5drl51tKwZfWNfK32q3HQvcU6a7uKG72ssU0HI6aXa7VGztPh49LCI0%2btcgKjeRuS2tzp2ZCyxJvK9nzl6KksxmmOmTttn3xcqxnZUFNAqgOmcpLTJ%2bbBZ37UwBBIjeC0eVQnwWDSY%2bmyHpdObdN7azZeIY8%2bRWsK2apcm3kKHnmV%2fyWZTQZq1P2laFibv0v2GWwcPiooTOooKRVTABvWEilOv8oKFo0JqTltAaJPyNJSMpezAxP1ossJfC2ZujzMizMunqa%2bVm%2b26W03sjLr9KIPT24CggqSwcCUJTnKf1vCLxmh6vadq5%2bWzc6xiroZmgvV4RtRkYyLcUMSZVmvveeuiJxGUQV%2bqfqWgeknt; mobilev=html5; sid=a7f73f92ebb3e1d8053375898d2356a7; USER_FLAG_CHECK=83d3a534c14bdd37ad3163a67a64bc60; TrackerID=bCJf7Sp3sZmISDM2GiEimINvu2lxMuFod3BAkAxyInqBCcSrprzLEdFsdzpReezEdB-lH47oR22ze7t8X-XFplHo7rKYTGsw9AquKt7WTlA; pt_key=AAFcQGSzADD4D08OUyBVkkiF-x8V6vo3J6T2N35Ypc5cB-u3lv87Oh-RbwC8TFHEaVUzkcRtlSY; pt_pin=jd_54397e682436b; pt_token=slz4grl9; pwdt_id=jd_54397e682436b; wxa_level=1; retina=0; cid=9; webp=1; visitkey=36737167522817205; wq_ufc=83d3a534c14bdd37ad3163a67a64bc60; __wga=1547723958411.1547723958411.1547723958411.1547723958411.1.1; PPRD_P=UUID.1526114150885499639638; sc_width=1920; wq_area=13_1112_0%7C2; shshshfp=903cac5b5554d91e9e698ad5cb9d520b; __jda=122270672.1526114150885499639638.1526114151.1547712588.1547723998.21; __jdb=122270672.1.1526114150885499639638|21.1547723998; shshshsID=4b52ff156a70a6db91fc4ca7fe7c78d0_3_1547724000889; thor=56401E19FB0AD7CDBE28BCDF98857F748C7579004B9AC1F9EE3953156081DE96759AD2CD612B7F4B09508DCEBC2AFF4B666D244F7F0EF28E28C57C8259D3C818E40683DDF250E98E3B6D9489402F816A38EE3955076DD71344B0DF0DC4240B4225D5A82A65A22CD7B7A21AB02CFCDD91DE5346885BE67AF7560B004616953978A6525E9EC5579E32E93EE51C5871428E8F6D0C1B243D0D542687703D3D2D7BE3'

path = '/client.action?functionId=newBabelAwardCollection&body=%7B%22activityId%22%3A%22gLmT9mwp1wCyKvL58hvpRHC3kMP%22%2C%22scene%22%3A%221%22%2C%22args%22%3A%22key%3Dd807fdd0f2774d3290b3c84b55a4fbef%2CroleId%3D17254396%22%2C%22eid%22%3A%22CYAIYHMV2QZ5FKG6OIJZF2EFKHYPXITMRC73DTHJOTOYUI3ZWBRLJAGHMCELXJKIRMGXMTDEWGTSISE4XHJK4DOBM4%22%2C%22fp%22%3A%2221a873dabf9f64ec63a8ec770ce5bedc%22%2C%22pageClick%22%3A%22Babel_Coupon%22%2C%22mitemAddrId%22%3A%22%22%2C%22geo%22%3A%7B%22lng%22%3A%22%22%2C%22lat%22%3A%22%22%7D%7D&screen=750*1334&client=wh5&clientVersion=1.0.0&sid=a7f73f92ebb3e1d8053375898d2356a7&uuid=&area=&loginType=3&callback=jsonp4'

functionId = 'newBabelAwardCollection'
body = '''
        {"activityId":"gLmT9mwp1wCyKvL58hvpRHC3kMP","scene":"1","args":"key=d807fdd0f2774d3290b3c84b55a4fbef,roleId=17254396","eid":"CYAIYHMV2QZ5FKG6OIJZF2EFKHYPXITMRC73DTHJOTOYUI3ZWBRLJAGHMCELXJKIRMGXMTDEWGTSISE4XHJK4DOBM4","fp":"21a873dabf9f64ec63a8ec770ce5bedc","pageClick":"Babel_Coupon","mitemAddrId":"","geo":{"lng":"","lat":""}}
'''

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
params = {
    'screen': '750*1334',
    'client': 'wh5',
    'clientVersion':'1.0.0',
    'sid':'a7f73f92ebb3e1d8053375898d2356a7',
    'loginType':'3',
    'callback':'jsonp4',
    'functionId' : 'newBabelAwardCollection',
    'body' : '''
{"activityId":"gLmT9mwp1wCyKvL58hvpRHC3kMP","scene":"1","args":"key=d807fdd0f2774d3290b3c84b55a4fbef,roleId=17254396","eid":"CYAIYHMV2QZ5FKG6OIJZF2EFKHYPXITMRC73DTHJOTOYUI3ZWBRLJAGHMCELXJKIRMGXMTDEWGTSISE4XHJK4DOBM4","fp":"21a873dabf9f64ec63a8ec770ce5bedc","pageClick":"Babel_Coupon","mitemAddrId":"","geo":{"lng":"","lat":""}}'
'''
}

req = requests.get(request_url,params=params,cookies={'cookies':cookies})

# retjson = req.json()

print(req)