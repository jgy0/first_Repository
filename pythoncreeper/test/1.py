# coding:utf-8
import urllib.request
import urllib.parse     #解析data键值对
#post请求，模拟用户登陆
#url=r"http://httpbin.org/post"

# data=bytes(urllib.parse.urlencode({"hello":"world"}),encoding='utf-8') #封装二进制bytes数组
# response=urllib.request.urlopen(url,data=data).read().decode() #post方式访问就必须有data参数
# print(response)

#超时处理
# try:
#     response=urllib.request.urlopen("http://httpbin.org/get",timeout=0.01).read().decode() #timeout响应时间，超出直接结束
#     print(response)
# except urllib.error.URLError as f:
#     print('timeout')

# response=urllib.request.urlopen("http://www.baidu.com")
# print(response.status)     #状态码,418代表别发现是爬虫了

# response=urllib.request.urlopen("http://www.baidu.com")
# print(response.getheaders())   #注意getheaders,getheader不一样
# print(response.getheader("Server"))

url="https://www.douban.com"
agent="MQQBrowser/38 (iOS 4; U; CPU like Mac OS X; zh-cn)"
header={"User-Agent":agent}
data=bytes(urllib.parse.urlencode({'name':'eric'}),encoding='utf-8')
req=urllib.request.Request(url=url,headers=header,data=data,method="POST")
response=urllib.request.urlopen(req)
print(response.read().decode())