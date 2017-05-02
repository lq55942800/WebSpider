#coding=utf-8

import urllib
from urllib import request,parse
#get方式

values = {}
values["loginName"]="12345"
values["passWord"]="54321"
data = parse.urlencode(values)
url = "https://www.hao123.com/"
getUrl = url+"?"+data
print(getUrl)
response = request.urlopen(url)
#print(response.read())