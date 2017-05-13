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
        upload_type = self.get_argument('type')
        # user_id = self.get_argument('user_id')
        # pro_id = self.get_argument('pro_id')
        data = {
            'user_id':'1',
            'pro_id':'1',
        }
        logging.info("[UPLOADHANDLER.uploadtype] %s, type %s"%(upload_type,type(upload_type)))
        if upload_type == '4':
            logging.info("in type == 4")
            info = '4' + self.get_argument('special_effect_method')
            res2 = yield self.requester(self.barcode_service+'/encode',{'information':info,'user_id':'1','pro_id':'1'})
            res = yield self.requester(self.resource_service+'/project/get',{'key':res2['data']['key']})
            self.write(res)
            self.finish()
        else:
            file_metas=self.request.files['main_model']   #提取表单中‘name’为‘file’的文件元数据
            logging.info("in recognize, upload is %s"%self.request)

            for meta in file_metas:
                binary = meta['body']
                name = meta['filename']
            logging.info("in get b64 encode")

            logging.info("in get oss key")
            # get oss key from object
            res =yield self.file_requester(self.resource_service+'/project/post', data, binary, name)
            key = res['data']['key']
            
            if upload_type == '3':
                para = {
                    'method':self.get_argument('method')
                }
                self.key_info_model.insert_new_key(key,upload_type,para)
            else:
                self.key_info_model.insert_new_key(key,upload_type)
            # get oss key from barcode picture
            logging.info("in bracode pic")
            res2 = yield self.requester(self.barcode_service+'/encode',{'information':key,'user_id':'1','pro_id':'1'})
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
        if key[0] == '4':
            self.write(key)
            self.finish()
        else:
            info = self.key_info_model.find_key(key)
            logging.info("[hololens.detect] info is %s"%info)
            # get url from key.
            prefix = info['type']

            res = yield self.requester(self.resource_service+'/project/get',{'key':key})

            if prefix == '3':
                prefix = prefix + info['method'] 
            self.write(prefix+res['data']['url'])
            self.finish()

# class RedirectHandler(BaseHandler):
#     def __init__(self, *argc, **argkw):
#         super(RedirectHandler, self).__init__(*argc, **argkw)    

#     @tornado.web.asynchronous
#     @tornado.gen.engine
#     def post(self):
#         self.get_argument('file')
