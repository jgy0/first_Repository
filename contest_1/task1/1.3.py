# coding:utf-8
import pandas as pd
import numpy as np
df=pd.read_csv(r'D:\xinjianqq\B题\附件1.csv',encoding='gbk')
df['num']=1
df.loc[df['支付时间'].str.contains("2017/4"),'支付时间']='四月'

df.loc[df['支付时间'].str.contains("2017/1",na=False),'支付时间']='一月'
df.loc[df['支付时间'].str.contains("2017/2",na=False),'支付时间']='二月'
df.loc[df['支付时间'].str.contains("2017/3",na=False),'支付时间']='三月'

df.loc[df['支付时间'].str.contains("2017/5",na=False),'支付时间']='五月'
df.loc[df['支付时间'].str.contains("2017/6",na=False),'支付时间']='六月'
df.loc[df['支付时间'].str.contains("2017/7",na=False),'支付时间']='七月'
df.loc[df['支付时间'].str.contains("2017/8",na=False),'支付时间']='八月'
df.loc[df['支付时间'].str.contains("2017/9",na=False),'支付时间']='九月'
df.loc[df['支付时间'].str.contains("2017/10", na=False),'支付时间']='十月'
df.loc[df['支付时间'].str.contains("2017/11", na=False),'支付时间']='十一'
df.loc[df['支付时间'].str.contains("2017/12", na=False),'支付时间']='十二'


data=pd.pivot_table(df,index=['地点','支付时间'],values=['实际金额','num'],aggfunc=np.sum)
for x in data.index:
    data.loc[x,'num']=data.loc[x,'num']/30
    data.loc[x,'实际金额']=data.loc[x,'实际金额']/30

data.to_csv(r'D:\xinjianqq\B题\task1\1_3_2.csv')
