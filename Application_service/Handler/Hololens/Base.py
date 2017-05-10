#!/usr/bin/env python
# coding=utf-8
# base.py

import os
import ConfigParser
import functools
import logging
import json
import urllib
import requests
from functools import partial
from uuid import uuid4
import mimetypes

import tornado.web
import tornado.gen
import tornado.httpclient
from tornado.concurrent import run_on_executor
from concurrent.futures import ThreadPoolExecutor

from Models.KeyInfo import KeyInfoModel
# from config.globalVal import MAX_WORKERS

@tornado.gen.coroutine
def _multipart_producer(boundary, content, filename, write):
    boundary_bytes = boundary.encode()
    filename_bytes = filename.encode()
    write(b'--%s\r\n' % (boundary_bytes,))
    write(b'Content-Disposition: form-data; name="%s"; filename="%s"\r\n' %
          (filename_bytes, filename_bytes))

    mtype = mimetypes.guess_type(filename)[0] or 'application/octet-stream'
    write(b'Content-Type: %s\r\n' % (mtype.encode(),))
    write(b'\r\n')
    # with open(filename, 'rb') as f:
    #     while True:
    #         # 16k at a time.
    #         chunk = f.read(16 * 1024)
    #         if not chunk:
    #             break
    #         write(chunk)

    #         # Let the IOLoop process its event queue.
    #         yield gen.moment
    write(content)
    write(b'\r\n')
    yield tornado.gen.moment
    write(b'--%s--\r\n' % (boundary_bytes,))

def throw_base_exception(method):
    """This is a decorator to handler all of common exception in this App

    Should be add in all of post or get method in xxxHandler.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        try:
            return method(self, *args, **kwargs)
        except tornado.web.MissingArgumentError, e:
            raise MyMissingArgumentError(e.arg_name)
    return wrapper
    

class BaseHandler(tornado.web.RequestHandler):
    # executor = ThreadPoolExecutor(max_workers=MAX_WORKERS)

    def __init__(self, *argc, **argkw):
        super(BaseHandler, self).__init__(*argc, **argkw)
        para = {} 
        self.barcode_service = self.application.barcode_service_url
        self.resource_service = self.application.resource_service_url
        para['mongodb'] = self.application.mongodb 
        self.key_info_model = KeyInfoModel(**para)
    # @run_on_executor
    # def background_task(self,function,*argc):
    #     return function(*argc)

    def change_custom_string_to_json(self, dic):
        pass
        # logging.info("in change custom string to json")
        # if isinstance(dic, dict):
        #     for key, value in dic.items():
        #         # print "in dictory : ",key, value
        #         # logging.info(" print key %s and value %s"%(key,value))
        #         if type(value) == bool:
        #             # logging.info("in bool value ,key is%s"%key)
        #             dic[key] = str(value)
        #         elif key == '_id' or key == 'person_id' or key == 'message_id':
        #             dic[key] = str(dic[key])
        #         elif key == 'missing_person_list':
        #             for index,item in enumerate(dic[key]):
        #                 dic[key][index]= str(item)
        #         elif key == 'std_pic_key' or key == 'std_photo_key' or key == 'picture_key' or key == 'pic_key' or key =='picture_key_list':
        #             if dic[key] =='empty':
        #                 continue
        #             if type(dic[key]) == list:
        #                 for index,item in enumerate(dic[key]):
        #                     dic[key][index]= self.picture_model.get_url(item)
        #             else:
        #                 dic[key] = self.picture_model.get_url(value)
        #         if isinstance(value, dict):
        #             self.change_custom_string_to_json(value)
        #         elif isinstance(value, list):
        #             for list_value in value:
        #                 self.change_custom_string_to_json(list_value)

    def return_to_client(self,return_struct):
        # self.change_custom_string_to_json(return_struct.data)
        # return_struct.print_info("after change")
        temp_json = json.dumps({'code':return_struct.code,
            'message':return_struct.message_mapping[return_struct.code],
            'data':return_struct.data},ensure_ascii=False)
        temp_json.replace("null", "\'empty\'")
        self.write(temp_json)

    @tornado.gen.coroutine
    def requester(self,url,data):
        body = urllib.urlencode(data)
        request = tornado.httpclient.HTTPRequest(
            url=url,
            method='POST',
            body=body
        )
        # logging.info("requester body is %s"%request.body)
        # logging.info("requester url is %s"%request.url)
        client = tornado.httpclient.AsyncHTTPClient()
        response = yield tornado.gen.Task(client.fetch,request)
        logging.info("[Base.response]body is %s"%response.body)
        body = json.loads(response.body)
        raise tornado.gen.Return(body)

    @tornado.gen.coroutine
    def file_requester(self,url,data,content, name):
        client = tornado.httpclient.AsyncHTTPClient()
        boundary = uuid4().hex
        headers = {'Content-Type': 'multipart/form-data; boundary=%s' % boundary}
        producer = partial(_multipart_producer, boundary, content, name)
        parameters = urllib.urlencode(data)
        response = yield client.fetch(url+'?'+str(parameters),
                                      method='POST',
                                      headers=headers,
                                      body_producer=producer,
                                      )
        logging.info("[Base.file_response] body is %s"%response.body)
        body = json.loads(response.body)
        raise tornado.gen.Return(body)

    # def big_requester(self,url,data):
    #     """
    #         instead by file_requester.
    #     """
    #     logging.info("[baseHandler.big_requester] before request")
    #     res = requests.post(url, params=data)
    #     logging.info("[baseHandler.big_requester] before request")
    #     logging.info(res.text)
    #     logging.info("res type %s"%type(res.text))
    #     j = json.loads(res.text)
    #     logging.info(j['data']['key'])
    #     return  j
