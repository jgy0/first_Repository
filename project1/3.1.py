# coding:utf-8
import pandas as pd
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Bar

df=pd.DataFrame(pd.read_csv(r'D:\xinjianqq\赛题a：教育平台的线上课程智能推荐策略\project\task1_1__2.csv',encoding='gbk'))
df['number']=1
data=pd.pivot_table(df,index=['course_id'],values=['number'],aggfunc=np.sum)
data=pd.DataFrame(data)
n=data.loc[:,'number']
n_min=min(n)
n_max=max(n)
for x in data.index:
    data.loc[x,'we']=(data.loc[x,'number']-n_min)/(n_max-n_min)

data_0 = data.sort_values(by="we")

data_1=data_0.tail(10)

# y=data_1.loc[:,'we'].values
y=list(data_1['we'])

x=list(map(str,data_1.index))
y_1=[]
for i in y:
    d=round(i,3)
    y_1.append(d)
print(y_1)
c = (
    Bar()
    .add_xaxis(x)
    .add_yaxis("课程", y_1)
    .set_global_opts(title_opts=opts.TitleOpts(title="Bar-最受欢迎的十们课程", subtitle=""))
    .render(r"D:\xinjianqq\赛题a：教育平台的线上课程智能推荐策略\3.1.html")
)