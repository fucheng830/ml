#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import urllib2
import htmllib
import formatter
import StringIO
import os
from formatter import AbstractFormatter
import chardet


class TrackingParser(htmllib.HTMLParser):
    def __init__(self,writer,*args):
        #formatter, verbose=0 =*arges
        htmllib.HTMLParser.__init__(self, *args)
        self.writer = writer
    def parse_starttag(self, i):
        index =htmllib.HTMLParser.parse_starttag(self, i)
        self.writer.index = index
        return index
    def parse_endtag(self, i):
        self.writer.index = i
        return htmllib.HTMLParser.parse_endtag(self, i) 

class Paragraph:
    def __init__(self):
        self.text = ''
        self.bytes = 0
        self.text_len = 0
        self.density = 0.0

class LineWriter(formatter.AbstractWriter):
    def __init__(self,*args):
        self.last_index = 0
        self.lines =[Paragraph()]
        formatter.AbstractWriter.__init__(self)
    def send_flowing_data(self, data):
       
        t= len(data)
        self.index += t
        b = self.index - self.last_index
        self.last_index = self.index
        l =self.lines[-1]
        l.text += data
        l.bytes += b
        l.text_len += t
        #l.density =  t/ float(b)
    
    def send_paragraph(self, blankline):
        
        if self.lines[-1].text =='':
            return
        self.lines[-1].text += '\n' * (blankline+1)
        self.lines[-1].bytes += 2 * (blankline+1)
        self.lines.append(Paragraph())
    
    def send_literal_data(self, data):
        self.send_flowing_data(data)
    
    def send_line_break(self):
        self.send_paragraph(0)
    
    
    def line_density(self):
        #self.density = len(l.text) / float(l.bytes)
           # total += l.density
       
        #self.average = total / float(len(self.lines))
        pass
  
    
    def compute_density(self):
   
        total =0.0
        for l in self.lines:
            l.density = len(l.text) / float(l.bytes)
            total += l.density
       
        self.average = total / float(len(self.lines))
     
  
    def output(self):
      
        self.compute_density()
        output = StringIO.StringIO()
        for l in self.lines:
           
            if l.density > 0.5:
                output.write(l.text)
        return output.getvalue()
        
'''
def extract_text(html):
    writer = LineWriter() 
    formatter = AbstractFormatter(writer)
    parser = TrackingParser(writer,formatter) 
    parser.feed(html)
    parser.close()
    
    return writer.output()  
''' 
def extract_text(html):
    writer = LineWriter() 
    formatter = AbstractFormatter(writer) 
    parser = TrackingParser(writer,formatter) 
    parser.feed(html)
    parser.close()
    writer.compute_density()
    
    return writer.lines

url='http://ent.hunantv.com/d/x/20091128/503722.html'
html=urllib2.urlopen(url)
reponse=html.read()
print chardet.detect(reponse)

'''
def write_train_data(a):
    f = open("save_file","w+")
    for index,x in enumerate(a):
        label=select_txt(x.text)
        if index == 0 :
            f.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (index,label,x.density,x.bytes,x.text_len,x.density,x.bytes,x.text_len,a[index+1].density,a[index+1].bytes,a[index+1].text_len))
        elif index ==len(a)-1 :
            f.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (index,label,x.density,x.bytes,x.text_len,a[index-1].density,a[index-1].bytes,a[index-1].text_len,x.density,x.bytes,x.text_len))
        else :
            f.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (index,label,x.density,x.bytes,x.text_len,a[index-1].density,a[index-1].bytes,a[index-1].text_len,a[index+1].density,a[index+1].bytes,a[index+1].text_len))
    
    f.close()

def save_file(s=1):
    if os.path.exists('d:/Workspace/ml/train_data/%s'%(make_file_name(s))):
       s+=1
       save_file(s)
    else:
        return make_file_name(s)
    
def make_file_name(s):
    return 'train%s'%s
    

def select_txt(train_data):
    print '%s' % train_data
    a=raw_input('是否选取')
    return a

def select_site():
    a=raw_input('请输入网址')
    htmls = urllib2.urlopen(a)
    a=extract_text(htmls.read())
    b=write_train_data(a)

select_site()


#b=write_train_data(a)
#q = open("e.csv","w+").writelines('\n'.join(["%s,%s"%(x.text,x.density) for x in a]))


#for x in b:
#   print x[:]
#write_to_txt(write_train_data(a))
#权向量（当前行的密度、当前行的HTML字节数、当前行的输出文本长度、前一行的这三个值、后一行的这三个值）

@var line_density: 当前行文本密度
@var line_bytes: 当前行的HTML字节数
@var line_len: 当前行文本长度
@var previous_density: 上一行文本密度
@var previous_bytes: 上一行的HTML字节数
@var previous_len: 上一行行文本长度
@var next_density: 下一行文本密度
@var next_bytes: 下一行的HTML字节数
@var next_len: 下一行文本长度

#def print_data(a):
#print len(a)


    
    
#q = open("e.csv","w+").writelines('\n'.join(["%s,%s"%(x.text,x.density) for x in a]))

#print_data
        
#

# 






       
#with open('C:/Users/Administrator/Desktop/text.txt','w') as f:    
    #print extract_text(html)
   
#s=map(lambda x:[x.bytes,len(x.text)], extract_text(html))
#q = open("e.csv","w+").writelines('\n'.join(["%s,%s"%(x[0],x[1]) for x in s]))
  
  



'''       