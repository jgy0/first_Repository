import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# import os
# print(os.getcwd())

# df=pd.DataFrame(pd.read_csv(r'D:\xinjianqq\赛题a：教育平台的线上课程智能推荐策略\study_information.csv',encoding='gbk'))
# data=pd.DataFrame(df.dropna())
# data_1=pd.DataFrame(data.drop_duplicates())
# data_1.to_csv(r'E:\tmp\project\task1_1_2.csv',encoding='gbk')         #删除空值

n=r'D:\xinjianqq\赛题a：教育平台的线上课程智能推荐策略\study_information.csv'
n1=r'D:\xinjianqq\赛题a：教育平台的线上课程智能推荐策略\users.csv'
path=r'D:\xinjianqq\赛题a：教育平台的线上课程智能推荐策略\project\task1_1__2.csv'
path1=r'D:\xinjianqq\赛题a：教育平台的线上课程智能推荐策略\project\task1_1_3.csv'

def rm_null(n):              #去除空值
    df = pd.DataFrame(pd.read_csv(n,encoding='gbk'))
    data = pd.DataFrame(df.dropna())
    return data
def save(data,path):         #保存csv
    data.to_csv(path,encoding='gbk')
def rm_same(data):           #去重
    data=pd.DataFrame(data.drop_duplicates())
    return data
def del_error(n):
    n=pd.DataFrame(n)
    for x in n.index:
        if n.loc[x,'recently_logged'] == '--':
            n.loc[x, 'recently_logged'] = n.loc[x, 'register_time']
    return n

def main():                  #程序入口
    data_0 = rm_null(n)         #study表去空
    data_1 = rm_same(data_0)    #study去重
    save(data_1, path)

    data2_1=pd.read_csv(n1,encoding='gbk')
    data2_2=del_error(data2_1)
    save(data2_2,path1)
main()