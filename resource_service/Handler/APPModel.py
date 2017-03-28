#!/usr/bin/env python
# coding=utf-8

# Author      :   Xionghui Chen
# Created     :   2017.3.27
# Modified    :   2017.3.27
# Version     :   1.0
import datetime

import tornado.web
import tornado.gen

from Base import BaseHandler

class UploadHandler(BaseHandler):
    def __init__(self,*argc, **argkw):
        super(UploadHandler, self).__init__(*argc, **argkw)
        self.buckname = ''
    def _gen_key(self, user_id,app_id):
        return str(user_id)+':'+str(app_id) + str(datetime.datetime.now())

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):
        """
            user_id:
            app_id:
            file:
        """
        user_id = self.get_argument('user_id')
        app_id = self.get_argument('app_id')
        file = self.get_argument('file')
        key = self._gen_key(user_id,app_id)
        self.register_bucket(self.buckname)
        if self._picture_model.upload_resrouce(key,file):
        else:
            raise 