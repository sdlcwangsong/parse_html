 # -*- coding:utf-8 -*-

import redis

class Dbs(object):
    def __init__(self):
        self.redis = redis.Redis(host = '127.0.0.1', port = 6379)

if __name__=='__main__':
    #pass
    dbs = Dbs()
    dbs.redis.delete("links")