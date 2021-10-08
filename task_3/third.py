# coding:utf-8
import csv
with open('text.csv','w',newline='') as f:
    test=csv.writer(f,delimiter=' ',quotechar='"')
    test.writerow(['abc','bcd','cdf'])
    test.writerow(['hhh']*6)

with open('text.csv',newline='') as f:
    text=csv.reader(f,delimiter=' ',quotechar='"')
    for i in text:
        print(i)