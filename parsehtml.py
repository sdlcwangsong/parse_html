# -*- encoding:utf8 -*-

import json
import dbs
from bs4 import BeautifulSoup
import time
import tldextract
import re
from urllib.parse import urljoin

class Extract(object):
    def __init__(self):
        self.redis = dbs.Dbs()
        self.domain_extract = tldextract.TLDExtract()
        self.templates = json.loads(open("template.json",'r').read())
        self.LIST_NAME = "links"
    
    
    def get_domain(self, url):
        try:
            ext = self.domain_extract(url)
            return ext.domain + "." + ext.suffix
        except:
            return None
            
    def soup_select(self, soup, name, css_selector, html):
        sels = css_selector.split(';')
        rets = []
        #if name == "regex":
        #    return re.findall(css_selector, html[2])
            
        for sel in sels:
            tmps = sel.split(',')
            #print('-'*10,len(tmps), tmps)
            if len(tmps) == 2:
                print("selector:", tmps[0])
                if tmps[1] == "regex":
                    match = re.findall(tmps[0], html[2])
                    if match:
                        return match
                    else:
                        return ""
                for elem in soup.select(sel):
                    rets.append(urljoin(html[1], elem.get(tmps[1])))
            else:
                for elem in soup.select(sel):
                    rets.append(elem.get_text())
        return rets 
               
    def extractor(self):
        filename = "/Users/ws/GoCode/bin/pages/" + str(time.strftime('%Y%m%d%H'))
        for html in open(filename,'r').readlines():
            html = html.split('\t')
            template = self.templates[self.get_domain(html[1])]
            for temp in template:
                if not re.search(temp["patt"], html[1]):
                    print(temp["patt"], html[1])
                    print("no match")
                    continue
                soup = BeautifulSoup(html[2],"html.parser")
                if temp["type"] == 1:
                    
                    for k, v in temp["field"].items():
                       rets = self.soup_select(soup, k, v, html) 
                       print (rets) 
                elif temp["type"] == 2:
                    p = self.redis.redis.pipeline()
                    for k, v in temp["field"].items():
                        rets = self.soup_select(soup, k, v, html)
                        print (rets)
                        for ret in rets:
                            if "http" not in ret:
                                print("not real link")
                                continue
                            p.sadd(self.LIST_NAME, ret)
                    p.execute()
                        
                        
                        
                        
                       
                           
                
            
if __name__=='__main__':
    et = Extract()
    et.extractor()
