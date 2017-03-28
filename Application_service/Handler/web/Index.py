#!/usr/bin/env python
# coding=utf-8

# Author      :   Xionghui Chen
# Created     :   2017.3.27
# Modified    :   2017.3.27
# Version     :   1.0

import tornado.web
import logging


class IndexPageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')