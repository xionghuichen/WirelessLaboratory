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
prefix ="http://127.0.0.1:10001/v1.0/service"
# prefix = "http://139.196.207.155:10001/v1.0/service"
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

def detect(data):
    req = set_resquest("/hololens/detect",data,"POST")
    response = urllib2.urlopen(req)
    the_page = response.read()
    return the_page

def test_detect():
    with open('add_method.png','rb') as f:
        content = f.read()
        b64 = base64.b64encode(content)
        data = {
            'b64_pic':b64,
        }
        result = detect(data)
        print result

if __name__ == '__main__':
    test_detect()