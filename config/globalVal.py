import os
import logging
AP = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))+'/'
MAX_WORKERS =100
class ReturnStruct(object):
    def __init__(self, message_mapping = ['default message']):
        self.max_code = len(message_mapping)
        self.code = 0
        self.message_mapping = message_mapping
        self.data = {}

    def merge_info(self,new_struct):
        self.code = self.max_code + new_struct.code
        self.max_code = self.max_code + new_struct.max_code
        self.data = dict(self.data, **new_struct.data)
        self.message_mapping.extend(new_struct.message_mapping)

    def print_info(self,tag ='default'):
        logging.info("print return struct, tag = %s...."%tag)
        logging.info("max_code:%s"%self.max_code)
        logging.info("code: %s"%self.code)
        logging.info("message_mapping: %s"%self.message_mapping)
        logging.info("data: %s"%self.data)