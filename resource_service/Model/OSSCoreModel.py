#!/usr/bin/env python
# coding=utf-8

# Author      :   Xionghui Chen
# Created     :   2017.3.27
# Modified    :   2017.3.27
# Version     :   1.0


# OSSCoreModel.py
import logging
import oss2
import time
class OSSCoreModel(object):
    def __init__(self, *argc, **argkw):
        self._sign_time = 3600
        self.ali_service = argkw['ali_service']
        self.auth = argkw['auth']
        self.endpoint = argkw['endpoint']

    def register_bucket(self,bucket_name):
        self.ali_bucket = oss2.Bucket(self.auth, self.endpoint, bucket_name)


    def upload_resource(self,key,binary_picture):
        """Upload single picture to OSS databases.

        Args:
            imageBytes: a bianry stream file
        
        Returns:
            true for success, false for failed.
        """
        logging.info("uploading resrouce key is %s..."%key)
        result = self.ali_bucket.put_object(key, binary_picture)
        if result.status != 200:
            return False
        return True

    def delete_picture_by_key(self,key):
        """Delete picture which key is parameter 'key'

        Args:

        Returns:
        """
        result = self.ali_bucket.delete_object(key)
        if result.status != 200:
            return False
        return True

    def get_url(self,key):
        return self.ali_bucket.sign_url('GET', key, self._sign_time)

    def check_exist(self,key):
        """return bool
        """
        return self.ali_bucket.object_exists(key)