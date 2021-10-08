# coding:utf-8
import pandas as pd
import numpy as np
df=pd.read_csv(r'D:\xinjianqq\B题\附件1.csv',encoding='gbk')

df['num']=1
data=df.loc[df['支付时间'].str.contains("2017/4")]


data_0=pd.pivot_table(data,index='地点',aggfunc=np.sum)

data_0.to_csv(r'D:\xinjianqq\B题\task1\1_2.csv')