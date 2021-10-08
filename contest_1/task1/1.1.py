# coding:utf-8
import pandas as pd
import numpy as np
df = pd.read_csv(r'D:\xinjianqq\B题\附件1.csv',encoding='gbk')
data_a =pd.DataFrame( df.loc[df['地点']=='A'])
data_b = pd.DataFrame(df.loc[df['地点']=='B'])
data_c =pd.DataFrame( df.loc[df['地点']=='C'])
data_d =pd.DataFrame( df.loc[df['地点']=='D'])
data_e = pd.DataFrame(df.loc[df['地点']=='E'])
data_a.to_csv(r"D:\xinjianqq\B题\task1\task1-1A.csv" , index=None)
data_b.to_csv(r"D:\xinjianqq\B题\task1\task1-1B.csv", index=None)
data_c.to_csv(r"D:\xinjianqq\B题\task1\task1-1C.csv", index=None)
data_d.to_csv(r"D:\xinjianqq\B题\task1\task1-1D.csv",index=None)
data_e.to_csv(r"D:\xinjianqq\B题\task1\task1-1E.csv",index=None)