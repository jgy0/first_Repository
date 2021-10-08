# coding:utf-8
import pandas as pd
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Bar


df=pd.DataFrame(pd.read_csv(r'D:\xinjianqq\2019赛题\A题\task1_1.csv',encoding='gbk'))
data_1=df.loc[df['是否促销'].isin(['是'])]   #促销的数据
data_2=df.loc[df['是否促销'].isin(['否'])]    #非促销的数据

data_1_0=pd.pivot_table(data=data_1,index=['大类名称'],values=['销售金额'],aggfunc=[np.sum],fill_value=0)
data_2_0=pd.pivot_table(data=data_2,index='大类名称',values='销售金额',aggfunc=[np.sum],fill_value=0)
data_1_new=pd.DataFrame({'销售金额':data_1_0.iloc[:,0]})
data_2_new=pd.DataFrame({'销售金额':data_2_0.iloc[:,0]})
#data_1.to_csv(r'D:\xinjianqq\2019赛题\A题\result\3.3.csv')
'''
y_1=data_1[data_1['是否促销']=='否']
y_1_0=list(y_1.iloc[:,0])
y_2=data_1[data_1['是否促销']=='是']
y_2_0=list(y_2.iloc[:,0])
'''
x=list(data_1_0.index)
x=list(map(str,x))
y_1=list(data_1_new['销售金额'])
y_2=list(data_2_new['销售金额'])
c = (
    Bar()
    .add_xaxis(x)
    .add_yaxis("促销",y_1)
    .add_yaxis("不促销",y_2)
    .set_global_opts(title_opts=opts.TitleOpts(title="Bar", subtitle="促销的影响"))
    .render(r"D:\xinjianqq\2019赛题\A题\result\bar_base.html")
)