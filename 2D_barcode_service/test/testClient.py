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
prefix ="http://127.0.0.1:10000/v1.0/barcode"
# prefix ="http://139.196.207.155:10000/v1.0/barcode"
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

def encode(data):
    # data = {
    #     "information":"15195861111",
    # }
    req = set_resquest("/encode",data,"POST")
    response = urllib2.urlopen(req)
    the_page = response.read()
    return the_page

def decode(data):
    # data = {
    #     'picture_base64':''
    # }
    req = set_resquest("/decode",data,"POST")
    response = urllib2.urlopen(req)
    the_page = response.read()
    return the_page

def test_encode():
    data = {
        'information':"2",
        'user_id':'',
        'pro_id':''
    }
    data = encode(data)
    data =  eval(data)
    print data['data']['key']
    # bin_pic = base64.b64decode(data['data']['key'])
    # print bin_pic
    # file = open('encoder.png','wb')
    # file.write(bin_pic)


def test_decode():
    with open('encoder3.jpg','rb') as f:
        content = f.read()
        b64 = base64.b64encode(content)
        data = {
            'picture_base64':b64,
            'just_info':1
        }
        result = decode(data)
        print result

if __name__ == '__main__':
    # test_encode()
    test_decode()
    # with open('encoder4.png','rb') as f:
    #     content = f.read()
    #     b64 = base64.b64encode(content)
    #     print b64
    # string ='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'
    # string = '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'
    # b64 = base64.b64decode(string)
    # data = {
    # 'picture_base64':string,
    # }
    # result = decode(data)
    # print result
    # # print b64
    # with open('encoder22.png','wb') as f:
    #     f.write(b64)
    # print test_encode()