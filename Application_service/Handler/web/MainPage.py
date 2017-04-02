
import tornado.web
import logging


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('mainpage.html')