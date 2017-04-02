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
    @tornado.web.asynchronous
    @tornado.gen.engine
    def post(self):
        #usernmae = self.get_argument("username")
        file_metas=self.request.files['image']   #提取表单中‘name’为‘file’的文件元数据
        binaty =''
        # user_id = self.get_argument('user_id')
        # pro_id = self.get_argument('pro_id')
        # file = self.get_argument('file')
        for meta in file_metas:
            binary = meta['body']

        data = {
            'user_id':'1',
            'pro_id':'1',
            'file':base64.b64encode(binary)
        }
        res =yield self.requester(self.resource_service+'/project/post',data)
        res = yield self.requester(self.resource_service+'/project/get',{'key':res['data']['key']})
        # logging.info("response")
        self.write(res)
        self.finish()