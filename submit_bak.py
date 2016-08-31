# -*- coding:utf-8 -*-
import sys, json
import urllib.parse
import urllib.request
import os,time

#name, key, value = sys.argv[1:]

#task = [{"name": name, "data": {key: value}, "retry": 3}]
f = open(sys.argv[1])
for line in f:
    task = [{"name": "dayin","data": {"link" : line.strip()},"retry":3,"savefile":"true"}]

    data = {"tasks": json.dumps(task)}

    tmpData=urllib.parse.urlencode(data)


    print (data)
    f = urllib.request.urlopen(
            url = 'http://127.0.0.1:8097/submit' ,
            #url = 'http://taskfetcher.bdp.svc/fetch' ,
            data = tmpData.encode(encoding='utf-8',errors='ignore')
            )
    print ("---2:",f.read())
    time.sleep(1)
