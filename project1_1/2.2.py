# coding:utf-8
import datetime

import pandas as pd
import numpy as np

df=pd.DataFrame(pd.read_csv(r'D:\xinjianqq\赛题a：教育平台的线上课程智能推荐策略\login.csv',encoding='gbk'))
df['login_time']=str(df['login_time'][1])          #不加【1】print输出会多几列
df['login_time']=df['login_time'].str.split(' ')
# print(df['login_time'][0])   #['2018-09-07', '09:28:28']
# print(df['login_time'][0][0])  #2018-09-07

# for x in df.index:
#     df.loc[x,'login_time']=df.loc[x,'login_time'][0]

# for x in range(len(df.index)):             #运行时间过长
#     df['login_time'][x]=df['login_time'][x][0]
#print(df['login_time'])
#df['login_time']=df['login_time'].dt.weekday_name

for x in df.index:
    df.loc[x,'long_timeofday']=df.loc[x,'login_time'][1]
    time=df.loc[x,'long_timeofday']=datetime.datetime.strptime(df.loc[x,'long_timeofday'],'%H:%M:%S')

    # print(df.loc[x,'long_timeofday'])
    # break
df.to_csv(r'D:\xinjianqq\赛题a：教育平台的线上课程智能推荐策略\project\22222.csv')