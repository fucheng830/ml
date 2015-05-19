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