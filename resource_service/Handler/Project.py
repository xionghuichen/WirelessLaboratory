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
import os
from Base import BaseHandler
from _exceptions.http_error import ArgumentTypeError
from config.globalVal import ReturnStruct,AP

class ProjectHandler(BaseHandler):
    def __init__(self,*argc, **argkw):
        super(ProjectHandler, self).__init__(*argc, **argkw)
        self.buckname = 'imgcuphololens'
        self._picture_model.register_bucket(self.buckname)
        self.temp_file_dir = self.application.static_path+'/temp_file/'

class UploadHandler(ProjectHandler):
    def __init__(self,*argc, **argkw):
        super(UploadHandler, self).__init__(*argc, **argkw)

    def _gen_key(self, user_id,pro_id,filename):
        return str(user_id)+':'+str(pro_id) + str(datetime.datetime.now())+str(filename)

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):
	logging.info("in post upload")
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
        for field_name, files in self.request.files.items():
            for meta in files:
                filename, content_type = meta['filename'], meta['content_type']
                body = meta['body']
                logging.info('POST "%s" "%s" %d m',filename, content_type, len(body)/1024.0/1024.0)

        user_id = self.get_argument('user_id')
        pro_id = self.get_argument('pro_id')
        logging.info("get user id %s"%user_id)
        # file = self.get_argument('file')
        # name = self.get_argument('filename')
        # try:
        #     binary_picture = base64.b64decode(body)
        #     del file
        # except TypeError as e:
        #     raise ArgumentTypeError('upload project picture')
        logging.info("in uploading resource...")
        key = self._gen_key(user_id,pro_id,filename)
        file_dir =self.temp_file_dir + str(key)
        with open(file_dir,'wb') as f:
            f.write(body)
            f.close()
        result.code = 0
        result.data = {'key':key}
        self.return_to_client(result)
        self.finish()
        up_result =yield self.background_task(self._picture_model.upload_resource,key,body)
        if up_result:
            del body
            logging.info("after upload file %s. result code is %s "%(key,result.code))
            os.remove(file_dir)


class GetUrlHandler(ProjectHandler):
    def __init__(self,*argc, **argkw):
        super(GetUrlHandler, self).__init__(*argc, **argkw)

    def post(self):
        message_mapping = [
            'success in oss',
            'success in resource server',
            'failed , not exist'
        ]
        result = ReturnStruct(message_mapping)
        key = self.get_argument('key')
        exist = self._picture_model.check_exist(key)
        if exist:
            url = self._picture_model.get_url(key)
            result.data = {'url':url}
        else:

            file_dir = self.temp_file_dir +str(key)
            if os.path.exists(file_dir):
                result.code = 1                                
                url = 'http://'+self.application.host+':'+self.application.port + self.application.prefix + '/project/redirect?key='+str(key)
                result.data = {'url':url}
            else:
                result.code = 2
        self.return_to_client(result)
        self.finish()

class RedirectHandler(ProjectHandler):
    def __init__(self,*argc, **argkw):
        super(RedirectHandler, self).__init__(*argc, **argkw)

    def get(self):
        key = self.get_argument('key')
        file_dir = self.temp_file_dir +str(key)
        exist = os.path.exists(file_dir)
        if exist:
            url = 'http://'+self.application.host+':'+self.application.port + '/static/temp_file/'+str(key)
            self.redirect(url)
        else:
            url = self._picture_model.get_url(key)
            self.redirect(url)