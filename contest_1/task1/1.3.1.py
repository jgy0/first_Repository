# coding:utf-8
import pandas as pd
import numpy as np
import datetime
import time
df=pd.read_csv(r'D:\xinjianqq\B题\附件1.csv',encoding='gbk')

df['支付时间'] = df['支付时间'].apply(lambda x: time.strptime(x, '%Y/%m/%d %H:%M'))
df['月份']=df['支付时间'].dt.month
data=pd.pivot_table(df,index=['地点','支付时间'])
data.to_csv(r'D:\xinjianqq\B题\task1\1_3_1.csv')