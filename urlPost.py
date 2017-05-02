#coding=utf-8
import urllib
from urllib import request,parse
#访问URL取得回应response对象
'''
response = request.urlopen("https://www.hao123.com/")
#urlopen(url, data, timeout)
#data入参，timeout延时
response.encoding='utf-8'
print (response.read())

'''
#post
values = {"loginName":"123456","passWord":"654321"}
#urlencode编码转换
data = parse.urlencode(values).encode(encoding="utf-8")
url= "https://www.hao123.com/"
response = request.urlopen(url, data)
print(response.read())
