# WebSpider
第一周，学习了Urllib库的基本操作（Python3）urllib.request,urllib.parse,urllib.error

1.请求URL,get,post方法。

2.设置header，proxy和timeout。

3.异常处理

4.cookie的使用




#-------------------------------------------------------------------------------------------------------------------------
踩过的坑：
1.urllib.request.Request(url,data,header),如果只传header,而没有data时，定义data=None
2.使用read()方法时，输出乱码，可以常识 .encoding('utf-8')解码
