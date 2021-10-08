# coding:utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
import datetime

df=pd.read_csv(r'D:\xinjianqq\B题\附件1.csv',encoding='gbk')
# for x in df.index:
#     df.loc[x,'支付时间']=datetime.datetime.strptime(df.loc[x,'支付时间'],'%Y/%m/%d %H:%M')

# df['支付时间']=datetime.datetime.strptime(df['支付时间'],'%Y/%m/%d %H:%M:%S')
# df['月']=df['支付时间'].apply(lambda x : x.dt.month)


df['num']=1
data=df.loc[df['支付时间'].str.contains("2017/4")]
data=pd.pivot_table(data,index=['地点'],values=['实际金额','num'],aggfunc=np.sum)
print(data)
x=list(data.index)
y=data['实际金额']

size=data['num'].rank()
n=200
plt.scatter(x,y,s=size*n,alpha=0.6)
plt.show()