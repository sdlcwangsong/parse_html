# -*- coding:utf-8 -*-
import sys, json
import dbs
import urllib.parse
import urllib.request
import os,time
sys.path.append("logger_python")
import log

LIST_NAME = "links"

logger = log.Log("sWang", "logger_python/logger.conf").logger

def submit(name, link):
    task = [{"name": name,"data": {"link" : link},"retry":3,"savefile":"true"}]
    data = {"tasks": json.dumps(task)}
    tmpData=urllib.parse.urlencode(data)
    f = urllib.request.urlopen(
            url = 'http://127.0.0.1:8097/submit' ,
            data = tmpData.encode(encoding='utf-8',errors='ignore')
    )
    ret = f.read().decode('utf-8').strip()
    logger.info(ret)
    return ret
if __name__=='__main__':

    redis = dbs.Dbs().redis
    
    while True:
    
        link = redis.spop(LIST_NAME).decode('utf-8')
        logger.info(link)
        if "dayin" in link:
            ret = submit("dayin", link)
            if ret != "ok":
                redis.sadd(LIST_NAME, link)
            continue
        if "tinkercad" in link:
            ret = submit("tinkercad", link)
            if ret != "ok":
                redis.sadd(LIST_NAME, link)
            continue
        ret = submit("link", link)
        logger.info("%s ok" , ret)
        if ret != "ok":
            logger.debug("reput")
            redis.sadd(LIST_NAME, link)
            
        time.sleep(1)
