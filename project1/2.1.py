import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

n=r'D:\qq聊天记录\1赛题A：教育平台的线上课程智能推荐策略\login.csv'
path=r''
df=pd.DataFrame(pd.read_csv(n,encoding='gbk'))


def save(data,path):         #保存csv
    data.to_csv(path,encoding='gbk')
def draw(data):
    prince1=[]               #广东
    for x in data.index:
        if data.loc[x,'login_place'].str.contains("中国黑龙江"):
            prince1.append(data.loc[x,'login_place'])
        elif data.loc[x,'login_place'].str.contains("中国"):
            pass
    print(prince1)

def main():
    draw(df)
main()