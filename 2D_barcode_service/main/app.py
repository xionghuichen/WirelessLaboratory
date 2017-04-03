
#!/usr/bin/env python
# coding=utf-8

# Author      :   Xionghui Chen
# Created     :   2017.3.27
# Modified    :   2017.3.27
# Version     :   1.0

# app.py
import sys
import os
reload(sys)
sys.setdefaultencoding('utf8')
location = str(os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.pardir))) + '/'
sys.path.append(location)
location = str(os.path.abspath(os.path.join(os.path.join(
    os.path.dirname(__file__), os.pardir), os.pardir))) + '/'
sys.path.append(location)


import ConfigParser
import logging
import oss2
import redis

import tornado.web
import tornado.httpserver
import tornado.ioloop
from tornado.options import define, options

from Handler import CoderHandler,Index
from config.globalVal import AP

define("host", default="139.196.207.155", help="community database host")
logging.basicConfig(level=logging.INFO)
                    #filename='log.log',
                    #filemode='w')


class Application(tornado.web.Application):
    def __init__(self, *argc, **argkw):
        config = ConfigParser.ConfigParser()
        config.readfp(open(AP + "config/config.ini"))
        logging.info("start server...")
        version = config.get('app','BARCODE_VERSION')
        service = config.get('app','BARCODE_NAME')
        prefix = version+service
        template_path = os.path.join(AP + "templates")
        static_path = os.path.join(AP + "static")
        settings = dict(
            xsrf_cookies=False,
            template_path=template_path,
            static_path=static_path
        )
        handlers = [
            # test
            (r''+prefix+'/',Index.IndexHandler),
            (r''+prefix+'/encode',CoderHandler.EncoderHandler),
            (r''+prefix+'/decode',CoderHandler.DecoderHandler),
        ]
        tornado.web.Application.__init__(self, handlers, **settings)
        self.resource_service_url = 'http://127.0.0.1:'+config.get("app","RESOURCE_PORT")+config.get("app","RESOURCE_VERSION")+config.get("app","RESOURCE_NAME")

        logging.info("start completed.")
        
def main():
    config = ConfigParser.ConfigParser()
    config.readfp(open(AP + "config/config.ini"))
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(config.get('app','BARCODE_PORT'))
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
