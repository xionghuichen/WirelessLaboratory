#!/usr/bin/env python
# coding=utf-8

# Author      :   Xionghui Chen
# Created     :   2017.3.27
# Modified    :   2017.3.27
# Version     :   1.0
import datetime
import logging
import tornado.web
import tornado.gen
import base64
from Base import BaseHandler
from _exceptions.http_error import ArgumentTypeError
from config.globalVal import ReturnStruct

class ProjectHandler(BaseHandler):
    def __init__(self,*argc, **argkw):
        super(ProjectHandler, self).__init__(*argc, **argkw)
        self.buckname = 'imgcuphololens'
        self._picture_model.register_bucket(self.buckname)

class UploadHandler(ProjectHandler):
    def __init__(self,*argc, **argkw):
        super(UploadHandler, self).__init__(*argc, **argkw)

    def _gen_key(self, user_id,pro_id,filename):
        return str(user_id)+':'+str(pro_id) + str(datetime.datetime.now())+str(filename)

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):
        """
            user_id:
            pro_id:
            file:
        """
        message_mapping = [
            'success',
            'failed'
        ]
        result = ReturnStruct(message_mapping)
        user_id = self.get_argument('user_id')
        pro_id = self.get_argument('pro_id')
        file = self.get_argument('file')
        name = self.get_argument('filename')
        try:
            binary_picture = base64.b64decode(file)
        except TypeError as e:
            raise ArgumentTypeError('upload project picture')
        logging.info("in uploading resource...")
        key = self._gen_key(user_id,pro_id,name)
        if self._picture_model.upload_resrouce(key,binary_picture):
            result.code = 0
            result.data = {'key':key}
        else:
            result.code = 1
        logging.info("after upload. result code is %s "%result.code)
        self.return_to_client(result)
        self.finish()

class GetUrlHandler(ProjectHandler):
    def __init__(self,*argc, **argkw):
        super(GetUrlHandler, self).__init__(*argc, **argkw)

    def post(self):
        key = self.get_argument('key')
        url = self._picture_model.get_url(key)
        result = ReturnStruct()
        result.data = {'url':url}
        self.return_to_client(result)
        self.finish()
