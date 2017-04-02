#!/usr/bin/env python
# coding=utf-8
# base.py

import os
import ConfigParser
import functools
import logging
import json
import urllib
import tornado.web
import tornado.gen
import tornado.httpclient
from tornado.concurrent import run_on_executor
from concurrent.futures import ThreadPoolExecutor
# from config.globalVal import MAX_WORKERS

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
        logging.info(response.body)
        body = json.loads(response.body)
        raise tornado.gen.Return(body)