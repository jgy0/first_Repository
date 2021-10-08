import urllib.request
import requests
import re
import random
import xlwt
import sqlite3
from bs4 import BeautifulSoup


url=r"https://movie.douban.com/top250"
useragent1="Netscape 3.01 gold (Win 95): Mozilla/3.01Gold (Win95; I)"
useragent2="Googlebot 2.1 (New version): Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
useragent3="Internet Explorer 6: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"
useragent4="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0"
useragent5="MQQBrowser/38 (iOS 4; U; CPU like Mac OS X; zh-cn)"
useragent=[useragent1,useragent2,useragent3,useragent4,useragent5]

agent=random.choice(useragent)
print(agent)

header={"User-Agent":agent}
req=requests.Request(url,headers=header)
respond=urllib.request.urlopen(url).read().decode()

pat=r"<title>(.*?)</title>"
data=re.findall(pat,respond)
print(data[0])