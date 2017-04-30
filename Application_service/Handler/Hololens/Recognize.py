#!/usr/bin/env python
# coding=utf-8

# Author      :   Xionghui Chen
# Created     :   2017.3.27
# Modified    :   2017.3.27
# Version     :   1.0


from Base import BaseHandler
from tornado import httputil, stack_context
from tornado.httpclient import HTTPResponse, HTTPError
import tornado.httpclient
import json
import tornado.gen
import tornado.web
import time
import logging
import urllib
import base64


class UploadHandler(BaseHandler):
    def __init__(self, *argc, **argkw):
        super(UploadHandler, self).__init__(*argc, **argkw)

    @tornado.web.asynchronous
    @tornado.gen.engine
    def post(self):
        #usernmae = self.get_argument("username")
        file_metas=self.request.files['image']   #提取表单中‘name’为‘file’的文件元数据
        logging.info("in recognize, upload is %s"%self.request)
        # user_id = self.get_argument('user_id')
        # pro_id = self.get_argument('pro_id')
        # file = self.get_argument('file')
        for meta in file_metas:
            binary = meta['body']
            name = meta['filename']
        logging.info("in get b64 encode")
        data = {
            'user_id':'1',
            'pro_id':'1',
        }
        logging.info("in get oss key")
        # get oss key from object
        res =yield self.file_requester(self.resource_service+'/project/post', data, binary, name)
        # res = yield self.requester(self.resource_service+'/project/post',data)
        # get oss key from barcode picture
        logging.info("in bracode pic")
        res2 = yield self.requester(self.barcode_service+'/encode',{'information':res['data']['key'],'user_id':'1','pro_id':'1','filename':name})
        # get url from key.
        logging.info("in get url")
        res = yield self.requester(self.resource_service+'/project/get',{'key':res2['data']['key']})
        # logging.info("response")
        self.write(res)
        self.finish()

class DetectHandler(BaseHandler):
    """docstring for DetectHandler"""
    def __init__(self, *argc, **argkw):
        super(DetectHandler, self).__init__(*argc, **argkw)
    
    @tornado.web.asynchronous
    @tornado.gen.engine
    def post(self):
        b64_pic = self.get_argument('b64_pic')
        if b64_pic == '':
            raise ArgumentTypeError("empty picture_base64")
        try:
            binary_picture = base64.b64decode(b64_pic)
        except TypeError as e:
            raise ArgumentTypeError('error change type : picture_base64')

        res2 = yield self.requester(self.barcode_service+'/decode',{'picture_base64':b64_pic})
        key = res2['data']['info']
        # get url from key.
        res = yield self.requester(self.resource_service+'/project/get',{'key':key})
        self.write(res['data']['url'])
	# self.write(res)
        self.finish()

# class RedirectHandler(BaseHandler):
#     def __init__(self, *argc, **argkw):
#         super(RedirectHandler, self).__init__(*argc, **argkw)    

#     @tornado.web.asynchronous
#     @tornado.gen.engine
#     def post(self):
#         self.get_argument('file')
