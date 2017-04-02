#!/usr/bin/env python
# coding=utf-8

# Author      :   Xionghui Chen
# Created     :   2017.3.10
# Modified    :   2017.3.10
# Version     :   1.0


# urllibtest.py
import urllib2
import urllib
import cookielib
import json
import random
import hashlib
import base64
import time
import datetime
import Image
prefix ="http://127.0.0.1:10002/v1.0/resource"
# prefix = "http://127.0.0.1:9000"
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
# get _xsrff
resp = urllib2.urlopen(prefix+'/')
the_page = resp.read()
print resp.getcode() == 200
print the_page

_xsrf = json.loads(the_page)['data']['_xsrf']
print "_xsrf:",_xsrf
def set_resquest(api,data,method):
    # data is dictory.
    # method can be get put delete post ?
    # get _xsrf
    for item in cj:
        if item.name == '_xsrf':
            _xsrf = item.value
    if method != 'GET':
        data['_xsrf'] = _xsrf
    data = urllib.urlencode(data)
    url = prefix + api
    if method == 'GET': 
        url = url + "?"+ data
    request = urllib2.Request(url,data)
    request.get_method = lambda: method # or 'DELETE' 
    return request

def upload(data):
    # data = {
    #     "information":"15195861111",
    # }
    req = set_resquest("/project/post",data,"POST")
    response = urllib2.urlopen(req)
    the_page = response.read()
    return the_page

def geturl(data):
    req = set_resquest("/project/get",data,"POST")
    response = urllib2.urlopen(req)
    the_page = response.read()
    return the_page    

def test_upload():
    with open('encoder.png','rb') as f:
        content = f.read()
        b64 = base64.b64encode(content)
        print b64
        data = {
            'file':b64,
            'user_id':123,
            'pro_id':12,
        }
        data = upload(data)
        print data
        data = eval(data)
        key = data['data']['key']
        data = {
            'key':key
        }
        data = geturl(data)
        print data
    # data =  eval(data)
    # bin_pic = base64.b64decode(data['data']['pic'])
    # print bin_pic
    # file = open('encoder.png','wb')
    # file.write(bin_pic)


if __name__ == '__main__':
    test_upload()