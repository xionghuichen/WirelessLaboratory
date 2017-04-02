
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

from config.globalVal import AP
from Handler import Project, Index

define("host", default="139.196.207.155", help="community database host")
define("mysql_database", default="cloudeye",
       help="community database name")
define("mysql_user", default="root", help="community mysql user")
define("mysql_password", default="",
       help="community database password")
define("mongo_user",default="burningbear", help="community mongodb  user")
define("mongo_password",default='',help="commuity mongodb password")
logging.basicConfig(level=logging.INFO)
                    #filename='log.log',
                    #filemode='w')


class Application(tornado.web.Application):
    def __init__(self, *argc, **argkw):
        config = ConfigParser.ConfigParser()
        config.readfp(open(AP + "config/config.ini"))
        ALIYUN_KEY = config.get("app","ALIYUN_KEY")
        ALIYUN_SECRET = config.get("app","ALIYUN_SECRET")
        template_path = os.path.join(AP + "templates")
        static_path = os.path.join(AP + "static")
        logging.info("start server.")
        version=config.get("app","RESOURCE_VERSION")
        service = config.get("app","RESOURCE_NAME")
        prefix = version+service
        settings = dict(
            xsrf_cookies=False,
        )

        handlers = [
            # test

            (r''+prefix+'/',Index.IndexHandler),
            (r''+prefix+'/project/post',Project.UploadHandler),
            (r''+prefix+'/project/get',Project.GetUrlHandler),

        ]

        tornado.web.Application.__init__(self, handlers, **settings)
        # bind ali cloud service
        self.auth = oss2.Auth(ALIYUN_KEY,ALIYUN_SECRET)
        logging.info('connecting to oss in ali yun...')
        self.endpoint = r'http://oss-cn-shanghai.aliyuncs.com'
        bucket_name = 'imgcuphololens'
        self.ali_service = oss2.Service(self.auth, self.endpoint)
        logging.info("start completed..")
        
def main():
    config = ConfigParser.ConfigParser()
    config.readfp(open(AP + "config/config.ini"))
    port = config.get("app","RESOURCE_PORT")
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
