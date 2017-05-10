#!/usr/bin/env python
# coding=utf-8

# Author      :   Xionghui Chen
# Created     :   2015.5.10
# Modified    :   2015.5.10
# Version     :   1.0

class BaseModel(object):
    def __init__(self, *argc, **argkw):
        self.mongodb = argkw['mongodb']