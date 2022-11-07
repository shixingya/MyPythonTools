#!/usr/bin/evn python
# coding:utf-8

# discover_available_domain.py 用来发现未注册的域名
# 主要用到的接口 http://panda.www.net.cn/cgi-bin/check.cgi?area_domain= XXX.com
# 关注返回值参数
# 
# original=210 : Domain name is available 表示域名可以注册
# original=211 : Domain name is not available 表示域名已经注册
# original=212 : Domain name is invalid 表示查询的域名无效
# original=213 : Time out 查询超时
                
import xylog
from xylog import Logger
import exrex
import random
import string
import urllib
import json
import requests
import sys
from xml.dom.minidom import parse
import xml.etree.ElementTree as ET
import os
import logging

xylog = Logger('result2.log',level='debug')
#已经查询的域名列表
#The domain name has been queried
queried_domain_list = []  

#可以注册的域名列表
can_register_list = []

def func_get(domain_address):
   request = "http://panda.www.net.cn/cgi-bin/check.cgi?area_domain=" + domain_address
   #print(request)
   ResponseStr = requests.get(request)
   #print(ResponseStr.text)
   return ResponseStr.text


def random_string_generator(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x
                   in range(str_size))


def parsexml(str,domain,index):
       try:
          root = ET.fromstring(str)
          #print(str)
          #print (root.tag, "---", root.attrib)
          
          for child in root:
            if child.tag == "original":
                # original=210 : Domain name is available 表示域名可以注册
                # original=211 : Domain name is not available 表示域名已经注册
                # original=212 : Domain name is invalid 表示查询的域名无效
                # original=213 : Time out 查询超时
                if child.text.find("211") > -1:
                    queried_domain_list.append(domain)
                if child.text.find("210") > -1:                    
                    queried_domain_list.append(domain)
                    res = child.tag + "---"+ child.text + " domain:",domain
                    print (res , " index:",index)
                    xylog.logger.info(res)
    
            
       except Exception as e:
           abc = 3 + 0
           #print("failed to get : ",domain,"  index:",index)
           #print('cannot parse str ,error code:%s', e)
       
def task(size, frontFix, backFix):
    chars = string.ascii_lowercase + string.digits 
    range_count = 36
    for index in range(size):
        range_count *= 36  
        
    for index in range(range_count):
     domain = frontFix + random_string_generator(size, chars) + backFix + ".com"
     if( queried_domain_list.count(domain) > 0 ):
        continue
    #  if(len(queried_domain_list) %10 == 0 ):
    #      print("current index",index)
         
     content = func_get(domain)
     #print('Random String of length 3 =',domain)
     parsexml(content,domain,index)
    
    print("task end =====",range_count)


def make_task(args):
    #print(args)
    #加1位置
    for u in args:
     print("hi::",u)
     task(1,u,"")
     task(1,"",u)
    
    print("done =================================================================")
    #加两位
    for u in args:
     print("hi::",u)
     task(2,u,"")
     task(2,"",u)


if __name__ == '__main__': 
    xylog.logger.debug('debug')
    xylog.logger.info('info')
    xylog.logger.warning('警告')
    xylog.logger.error('报错')
    xylog.logger.critical('严重')

    #Create a list of 5 elements
    # a1 = ["shixingya","1"]
    # make_task(a1)
    # exlog.logger.info(can_register_list)
    # exlog.logger.info("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    
    a = ["ai","hi","by","xi","fu","du","xr","vr","ar","la","91","mi","51","la","oh","job","shi","good","xiaomi","jd",]
    make_task(a)

    #exlog.logger.warning("task end ==----------------------------------------------------------------",queried_domain_list)
    xylog.logger.info(can_register_list)
    
    #print("task end ==----------------------------------------------------------------",queried_domain_list)
    print("task end ==----------------------------------------------------------------",can_register_list)