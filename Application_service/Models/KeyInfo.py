#!/usr/bin/env python
# coding=utf-8

# Author      :   Xionghui Chen
# Created     :   2017.5.10
# Modified    :   2017.5.10
# Version     :   1.0


from Base import BaseModel
from _exceptions.http_error import DBQueryError
class KeyInfoModel(BaseModel):
    def __init__(self, *argc, **argkw):
        super(KeyInfoModel, self).__init__(*argc, **argkw)

    def insert_new_key(self,key,type,other={}):
        info_data = {
            'key':key,
            'type':type
        }
        if type == '3':
            info_data['method']=other['method']
        return self.mongodb.key.info.insert_one(info_data).inserted_id

    def find_key(self,key):
        result = self.mongodb.key.info.find_one({'key':key})
        if result == []or result == None:
            raise DBQueryError('error when get person detail infomation by key: %s'%key)
        return result