#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import chardet
'''
url=raw_input('网址')
htmls = urllib2.urlopen(url)
print htmls.read()
print chardet.detect(htmls.read())

import pylab as pl
pl.seed(1)
data = pl.randn(100)
pl.plot(data)
pl.show()
'''


'''
def c(p,last=5,g=1):
    last=g*5
    if p>last:
        g=g+1
        last=g*5
        c(p,last,g)
        return c(p,last,g)
    else:
        return p,last,g

print c(18) 
'''

import urllib   
import urllib2   
     
request_url = 'http://www.sina.com.cn' 

user_headers = {
    'x-requestted-with': 'XMLHttpRequest',
    'Cache-Control': 'no-cache',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1',  
    'Connection' : 'Keep-Alive',
}
   


req = urllib2.Request(url=request_url,headers=user_headers)   
response = urllib2.urlopen(req)   
the_page = response.read()

#the_page.decode('gbk')  
'''
def unzip(data):
        import gzip
        import StringIO
        data = StringIO.StringIO(data)
        gz = gzip.GzipFile(fileobj=data)
        data = gz.read()
        gz.close()
        return data
'''
print the_page

