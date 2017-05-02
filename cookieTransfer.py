#coding=utf-8

from urllib import request,parse
import http.cookiejar

filename = 'cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = request.HTTPCookieProcessor(cookie)
#模拟登录，并把cookie保存到变量
opener = request.build_opener(handler)
url1 = 'https://www.baidu.com'
#req = request.Request(url)
res1 = opener.open(url1)
#保存cookie到cookie.txt中
cookie.save(ignore_discard=True,ignore_expires=True)
#利用cookie请求访问另一个网址
url2 = 'https://tieba.baidu.com/index.html'
res2 =opener.open(url2)
print(res1.read().decode('utf-8'))
print(res2.read().decode('utf-8'))
