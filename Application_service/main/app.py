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

import ConfigParser
import logging
import oss2
import redis

import tornado.web
import tornado.httpserver
import tornado.ioloop
from tornado.options import define, options

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymongo

from config.globalVal import AP
from Handler import Index

define("port", default=10001, help="run on the given port", type=int)
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
        COOKIE_SECRET = config.get("app", "COOKIE_SECRET")
        template_path = os.path.join(AP + "templates")
        static_path = os.path.join(AP + "static")
        logging.info("start server.")
        version='/v1.0'

        settings = dict(
            cookie_secret=COOKIE_SECRET,
            xsrf_cookies=False,
            template_path=template_path,
            static_path=static_pathd
        )

        handlers = [
            # test
            (r''+version+'/index', Index.IndexPageHandler),
        ]

        tornado.web.Application.__init__(self, handlers, **settings)
        # use SQLachemy to connection to mysql.
        DB_CONNECT_STRING = 'mysql+mysqldb://%s:%s@%s/%s?charset=utf8'%(options.mysql_user, options.mysql_password, options.host, options.mysql_database)
        engine = create_engine(DB_CONNECT_STRING, echo=False,pool_size=1000)
        self.sqldb = sessionmaker(
                bind=engine,
                autocommit=False, 
                autoflush=True,
                expire_on_commit=False)
        base_model = declarative_base()
        # create all of model inherit from BaseModel 
        base_model.metadata.create_all(engine) 
        # use pymongo to connectino to mongodb
        logging.info("connect mongodb ..")
        client = pymongo.MongoClient(options.host,27017)
        client.cloudeye.authenticate(options.mongo_user,options.mongo_password)
        self.mongodb = client.cloudeye
        # bind face++ cloud service
        logging.info("connect mongodb successfully..")
        # bind ali cloud service
        logging.info("start completed..")
        
def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
