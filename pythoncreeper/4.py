# coding:utf-8
import urllib.request
import requests
import re
import random
import xlwt
import sqlite3
from bs4 import BeautifulSoup
def main():
    baseurl=r"https://movie.douban.com/top250?start="
    #1.爬取网页
    datalist=getData(baseurl)
    savepath="豆瓣电影Top250.xls"
    #3.保存数据
    saveData(datalist,savepath)
    # response=urllib.request.urlopen(url).read().decode('utf-8')
    # print(response)
    #askURL("https://movie.douban.com/top250?start=")

findLink=re.compile(r'<a href="(.*?)">')  #创建正则表达式对象，表示规则
#影片图片的规则
findImgSrc=re.compile(r'<img alt=.*src="(.*?)"',re.S)  #点任意匹配模式，改变'.'的行为,让换行符包含在字符中
#影片的片名
findTitle=re.compile(r'<span class="title">(.*)</span>')
#影片的评分
findRemark=re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#影片的评价人数
findPeople=re.compile(r'<span>(\d*)人评价</span>')
#影片的概况
findView=re.compile(r'<span class="inq">(.*)</span>')
#找到影片的相关内容
findBd=re.compile(r'<p class="">(.*?)</p>',re.S)
def getData(baseurl):
    datalist=[]
    for i in range(0,25):
        url=baseurl+str(i*25)
        html=askURL(url)
        #逐一进行解析
        soup=BeautifulSoup(html,"html.parser")   #获得树形对象
        for item in soup.find_all("div",class_="item"):
            #print(item)
            data=[]    #保存一部电影的全部信息
            item=str(item)
            #获取影片详情的超链接
            #print(item)

            link=re.findall(findLink,item)[0]   #re库用正则表达式查找指定的字符串
            data.append(link)

            imgSrc=re.findall(findImgSrc,item)[0]
            data.append(imgSrc)

            title = re.findall(findTitle, item)
            if len(title)==2:
                ctitle=title[0]
                data.append(ctitle)     #添加中国名
                otitle=title[1].replace("/","")   #去掉title前的无关符号/
                data.append(otitle)     #添加外国名
            else:
                data.append(title[0])
                data.append(" ")      #若没有外国名，留空

            reMark=re.findall(findRemark,item)[0]
            data.append(reMark)     #添加评价

            people=re.findall(findPeople,item)[0]
            data.append(people)      #添加评价人数

            view=re.findall(findView,item)
            if len(view) !=0:
                view=view[0].replace("。","")
                data.append(view)  # 添加概述
            else:
                data.append(" ")     #留空

            bd=re.findall(findBd,item)[0]
            bd=re.sub('<br(\s+)?/>(\s+)?',' ',bd)  #去掉br
            bd=re.sub('/',' ',bd)   #替换/
            data.append(bd.strip())   #去掉前后的空格


            datalist.append(data)   #把处理好的一部分电源信息放进去

    return datalist

def askURL(url):
    head={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0"}
    req=urllib.request.Request(url,headers=head)
    html=""
    try:
        response=urllib.request.urlopen(req)
        html=response.read().decode()
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):   #用于判断对象是否包含对应的属性
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html
def saveData(datalist,savepath):
    workbook = xlwt.Workbook(encoding='utf-8',style_compression=0)  # 创建workbook对象
    worksheet = workbook.add_sheet('豆瓣Top250',cell_overwrite_ok=True)  # 创建工作表 ,cell_每个单元是否可以覆盖
    col=("电影详情链接","图片链接","影片中国名","外国名","评分","评价数","概述","相关信息")
    for i in range(0,8):
        worksheet.write(0,i,col[i]) #写入列名
    for i in range(0,250):
        print("第%d条" %(i+1))
        data=datalist[i]
        for j in range(0,8):
            worksheet.write(i+1,j,data[j])

    workbook.save(savepath)  #保存
if __name__=='__main__':
    main()
    print("爬取完毕")