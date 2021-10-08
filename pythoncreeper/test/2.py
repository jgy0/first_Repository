# coding:utf-8
from bs4 import BeautifulSoup
import re

file=open("./baidu.html","rb")
html=file.read().decode()
bs=BeautifulSoup(html,"html.parser") #是指定Beautiful的解析器为“html.parser”还有BeautifulSoup(markup,“lxml”)BeautifulSoup(markup, “lxml-xml”) BeautifulSoup(markup,“xml”)等等很多种
'''
# #1.Tag     标签及其内容
# print(bs.title)    #第一个出现的标签及其内容
# #2.NavigableString    标签里的内容（字符串）
# print(bs.title.string)  #只要标签里面的东西
# print(bs.a)
# print(type(bs.head))
print(bs.a.attrs)    #快速获得标签里所有的属性
#3.BeautifulSoup  表示整个文档
# print(type(bs))
# print(bs.name)
# print(bs.attrs)
# print(bs)
#4.NavigableString    注释
print(bs.a.string)
print(type(bs.a.string))'''
#print(bs.head.contents[1])

#文档的搜索
#(1)find_all()   字符串过滤：会查找与字符串完全匹配的
# t_list=bs.find_all("a")
# print(t_list)


#(2)正则表达式搜索
# t_list=bs.find_all(re.compile("a"))

#(3) 自定义函数操作
# def name_is_exists(tag):
#     return tag.has_attr("name")
# t_list=bs.find_all(name_is_exists)
# print(t_list)

#2 参数信息
# t_list=bs.find_all(class_=True)
# for i in t_list:
#     print(i)
# t_list=bs.find_all(href="http://www.baidu.com/more/")
# print(t_list)

#3.text 参数
# t_list=bs.find_all(text=["hao123","地图","贴吧"])
# t_list=bs.find_all(text=re.compile("\d"))
# print(t_list)
#4 limit参数
# t_list=bs.find_all("a",limit=3)    #可以限定一下获取多少个
# print(t_list)

#css 选择器
# print(bs.select('title'))   #通过标签进行查找
# print(bs.select(".mnav",limit=3))   #按照类名来查找
# print(bs.select("#u1"))       #按照id查找
# print(bs.select("div[class='bdpfmenu']")) #通过属性来查找
# t_list = bs.select("head > title")	   #通过子标签查找
t_list=bs.select(".mnav ~ .bri")
print(t_list[0].get_text())
# for i in t_list:
#     print(i)