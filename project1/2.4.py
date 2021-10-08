# coding:utf-8
import pandas as pd
import numpy as np
import datetime

time=datetime.datetime.strptime("2020-06-18 00:00:00", "%Y-%m-%d %H:%M:%S")
df=pd.DataFrame(pd.read_csv(r'D:\xinjianqq\赛题a：教育平台的线上课程智能推荐策略\project\task1_1_3.csv',encoding='gbk'))
lost_sum=0

df['recently_logged'] = pd.to_datetime(df['recently_logged'],format='%Y-%m-%d %H:%M:%S') #object类型转化为datetime64

# for x in df.index:    #这种方式不行，类型转化不成功
#     df.loc[x,'recently_logged']=datetime.datetime(df.loc[x,'recently_logged'])

for x in df.index:
    if (time - df.loc[x, 'recently_logged']).days > 90:
        lost_sum+=1
loss_percent=lost_sum/43982
print(loss_percent)
