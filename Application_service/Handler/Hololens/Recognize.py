#!/usr/bin/env python
# coding=utf-8

# Author      :   Xionghui Chen
# Created     :   2017.3.27
# Modified    :   2017.3.27
# Version     :   1.0


from Base import BaseHandler
from tornado import httputil, stack_context
from tornado.httpclient import HTTPResponse, HTTPError
import json
import tornado.gen
import tornado.web
import time
import logging

class UploadHandler(BaseHandler):
    """
     Client will access IndexHandler when he open his app.
     Server will set a _xsrf as cookie to client.
     All of access after it, client should post _xsrf as a parameter to server,
     tornado will check it automatic.
    """
    def post(self):
        #usernmae = self.get_argument("username")
        file_metas=self.request.files['image']   #提取表单中‘name’为‘file’的文件元数据
        logging.info(self.request)
        # for meta in file_metas:
        #     filename=meta['filename']
        #     filepath=os.path.join(upload_path,filename)
        #     with open(filepath,'wb') as up:      #有些文件需要已二进制的形式存储，实际中可以更改
        #         up.write(meta['body'])
        self.write('finished!')