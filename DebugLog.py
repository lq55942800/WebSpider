#coding=utf-8

import urllib
from urllib import request,parse

httpHandler = request.HTTPHandler(debuglevel=1)
httpsHandler = request.HTTPSHandler(debuglevel=1)
opener = request.build_opener(httpHandler, httpsHandler)
request.install_opener(opener)
request.urlopen("http://www.baidu.com")