#!/usr/bin/env python
# coding=utf-8

# Author      :   Xionghui Chen
# Created     :   2017.3.27
# Modified    :   2017.3.27
# Version     :   1.0


from Handler.Base import BaseHandler
from tornado import httputil, stack_context
from tornado.httpclient import HTTPResponse, HTTPError
import json
import tornado.gen
import tornado.web
import time

class IndexHandler(BaseHandler):
    """
     Client will access IndexHandler when he open his app.
     Server will set a _xsrf as cookie to client.
     All of access after it, client should post _xsrf as a parameter to server,
     tornado will check it automatic.
    """
    def get(self):
        try:
            data = {"_xsrf":self.xsrf_token}
            jquery = ''
            try:
                jquery = str(self.get_argument('jsoncallback'))
            except Exception as e:
                # do nothing.
                pass
            # Data = json.dumps(Data)
            result = json.dumps({"code": 100,"message":self.xsrf_token,"data":data})
            if jquery != '':
                result = jquery + '('+result+')'

            self.write(result)
        except Exception, e:
            result = json.dumps({"code": 99,"message":"fail set cookie","data":{}})
            self.write(result)
            raise
        self.finish()