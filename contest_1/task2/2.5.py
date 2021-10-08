# coding:utf-8
import numpy as np
import datetime
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import HeatMap


df=pd.read_csv(r'D:\xinjianqq\B题\附件1.csv',encoding='gbk')

data=df.loc[df['地点']=='C']
data['支付时间']=pd.to_datetime(data['支付时间'],format='%Y/%m/%d %H:%M:%S', errors='coerce')
data['月份']=data['支付时间'].dt.month
data['小时']=data['支付时间'].dt.hour
data['天']=data['支付时间'].dt.day
# for x in data.index:
#     data.loc[x,'支付时间']=datetime.datetime.strptime(df.loc[x,'支付时间'],'%Y/%m/%d %H:%M')
# df.info()
# df['月']=df['支付时间'].apply(lambda x : x.dt.month)

data_f=data.loc[data['月份'].isin([6])]

data_x=pd.pivot_table(data_f,index=['天','小时'],values='实际金额',aggfunc=np.sum)
data_x=pd.DataFrame(data_x)
v=[]
# print(data_x.index)
# ( 1,  0),
# ( 1,  2),
# ( 1,  4),
value=value1=value0=[]
# print(data_x.index[0])
# (1, 0)

n=list(data_x['实际金额'])
i=0
for x in data_x.index:
    value.append([x[0], x[1],n[i]])
    i=i+1


#----------------
data_3=data.loc[data['月份'].isin([7])]

data_3=pd.pivot_table(data_3,index=['天','小时'],values='实际金额',aggfunc=np.sum)
data_3=pd.DataFrame(data_3)


n1=list(data_3['实际金额'])
i=0
for x in data_3.index:
    value0.append([x[0], x[1],n1[i]])
    i=i+1


#--------------

# data_x.to_csv(r'D:\xinjianqq\B题\2.5.csv')
data_8=data.loc[data['月份'].isin([8])]

data_8=pd.pivot_table(data_8,index=['天','小时'],values='实际金额',aggfunc=np.sum)
data_8=pd.DataFrame(data_8)


n2=list(data_8['实际金额'])
i=0
for x in data_8.index:
    value1.append([x[0], x[1],n2[i]])
    i=i+1


c = (
    HeatMap()
    .add_xaxis([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])
    .add_yaxis("series0",[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23] , value)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="6月订单量的热力图，"),
        visualmap_opts=opts.VisualMapOpts(),
    )
    .render(r"D:\xinjianqq\B题\sss.html")
)

c = (
    HeatMap()
    .add_xaxis([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])
    .add_yaxis("series1",[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23] , value0)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="7月订单量的热力图，"),
        visualmap_opts=opts.VisualMapOpts(),
    )
    .render(r"D:\xinjianqq\B题\7月.html")
)

c = (
    HeatMap()
    .add_xaxis([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])
    .add_yaxis("series2",[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23] , value1)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="8月订单量的热力图，"),
        visualmap_opts=opts.VisualMapOpts(),
    )
    .render(r"D:\xinjianqq\B题\八月.html")
)