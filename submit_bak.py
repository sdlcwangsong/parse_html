# -*- coding:utf-8 -*-
import sys, json
import urllib.parse
import urllib.request
import os,time
#name, key, value = sys.argv[1:]

#task = [{"name": name, "data": {key: value}, "retry": 3}]


task = [{"name": "tinkercad","data": {"link" : "https://www.tinkercad.com/things/jKdHxIbCgv8-because-no-one-likes-cats/"},"retry":3,"savefile":"true"}]

data = {"tasks": json.dumps(task)}

tmpData=urllib.parse.urlencode(data)


print (data)
f = urllib.request.urlopen(
        url = 'http://127.0.0.1:8097/submit' ,
        #url = 'http://taskfetcher.bdp.svc/fetch' ,
        data = tmpData.encode(encoding='utf-8',errors='ignore')
        )
print ("---2:",f.read())
