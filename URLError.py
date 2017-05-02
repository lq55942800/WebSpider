#coding=utf-8

import urllib
from urllib import request,error
'''
url = "http://www.iloveyou.com"
req = request.Request(url)

try:
    request.urlopen(req)
except error.URLError as e:
    print (e.reason)
'''
url1 = "http://blog.csdn.net/cqcre"
try:
    request.urlopen(url1)
except error.HTTPError as e:
    print (e.code, e.reason)
except error.URLError as e:
    print (e.reason)
else:
    print ("OK")
