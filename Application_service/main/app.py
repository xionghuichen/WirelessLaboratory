#!/usr/bin/env python
# coding=utf-8

# Author      :   Xionghui Chen
# Created     :   2017.3.27
# Modified    :   2017.5.10
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

import tornado.web
import tornado.httpserver
import tornado.ioloop
from tornado.options import define, options

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymongo

from config.globalVal import AP
service_path = AP+'Application_service/'

from Handler.web import Index, MainPage
from Handler.Hololens import Recognize, IndexTest


define("port", default=10001, help="run on the given port", type=int)
define("host", default="139.196.207.155", help="community database host")
define("mysql_database", default="cloudeye",
       help="community database name")
define("mysql_user", default="root", help="community mysql user")
define("mysql_password", default="zp19950310",
       help="community database password")
define("mongo_host", help="community mongodb  host")
define("mongo_user", help="community mongodb  user")
define("mongo_password",help="commuity mongodb password")
logging.basicConfig(level=logging.INFO)
                    #filename='log.log',
                    #filemode='w')


class Application(tornado.web.Application):
    def __init__(self, *argc, **argkw):
        config = ConfigParser.ConfigParser()
        config.readfp(open(AP + "config/config.ini"))
        COOKIE_SECRET = config.get("app", "COOKIE_SECRET")
        logging.info("ap is %s"%service_path)
        template_path = os.path.join(service_path + "templates")
        static_path = os.path.join(service_path + "static")

        logging.info("start server.")
        version= config.get("app", "APPLICATION_VERSION")
        service = config.get("app", "APPLICATION_NAME")
        self.prefix = version+service
        settings = dict(
            cookie_secret=COOKIE_SECRET,
            xsrf_cookies=False,
            template_path=template_path,
            static_path=static_path
        )

        handlers = [
            # test
            (r''+self.prefix+'/',IndexTest.IndexHandler),
            (r''+self.prefix+'/web/index', Index.IndexPageHandler),
            (r''+self.prefix+'/web/main',MainPage.IndexHandler),
            (r''+self.prefix+'/hololens/upload',Recognize.UploadHandler),
            (r''+self.prefix+'/hololens/detect',Recognize.DetectHandler)
        ]

        tornado.web.Application.__init__(self, handlers, **settings)
        # use SQLachemy to connection to mysql.
        logging.info("connect mysql ..")
        # DB_CONNECT_STRING = 'mysql+mysqldb://%s:%s@%s/%s?charset=utf8'%(options.mysql_user, options.mysql_password, options.host, options.mysql_database)
        # engine = create_engine(DB_CONNECT_STRING, echo=False,pool_size=1000)
        # self.sqldb = sessionmaker(
        #         bind=engine,
        #         autocommit=False, 
        #         autoflush=True,
        #         expire_on_commit=False)
        # base_model = declarative_base()
        # # create all of model inherit from BaseModel 
        # base_model.metadata.create_all(engine) 
        # use pymongo to connectino to mongodb
        logging.info("connect mongodb ..")
        client = pymongo.MongoClient(options.mongo_host,27017)
        client.hololens.authenticate(options.mongo_user,options.mongo_password)
        self.mongodb = client.hololens
        # bind face++ cloud service
        logging.info("connect mongodb successfully..")
        # bind micro service
        self.barcode_service_url = 'http://127.0.0.1:'+config.get("app","BARCODE_PORT")+config.get("app","BARCODE_VERSION")+config.get("app","BARCODE_NAME")
        self.resource_service_url = 'http://127.0.0.1:'+config.get("app","RESOURCE_PORT")+config.get("app","RESOURCE_VERSION")+config.get("app","RESOURCE_NAME")
        logging.info("varcode url is %s"%self.barcode_service_url)
        logging.info("resource url is %s"%self.resource_service_url)
        # bind ali cloud service
        logging.info("start completed..")
        
def main():
    config = ConfigParser.ConfigParser()
    config.readfp(open(AP + "config/config.ini"))
    port = config.get("app", "APPLICATION_PORT")
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application(),chunk_size=65536000, max_header_size=65536000)
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
