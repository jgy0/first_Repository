# coding:utf-8
import pandas as pd
import numpy as np
from pyecharts.charts import Bar
from pyecharts import options as opts

df=pd.read_csv(r'D:\xinjianqq\2019赛题\A题\task1_1.csv',encoding='gbk')
data_0=pd.pivot_table(data=df,index='顾客编号',values='销售金额',aggfunc=[np.sum]) #每个用户的总消费额
data_1=pd.DataFrame({'总消费金额':data_0.iloc[:,0]})
#data_1.to_csv(r'D:\xinjianqq\2019赛题\A题\result\3-1.csv')
data_2=data_1.sort_values(by='总消费金额',ascending=False)   #按照消费排名
data_2_0=pd.DataFrame( {'总消费金额':data_2.iloc[0:10,0] })         #筛选出排名前十
#data_2_0.to_csv(r'D:\xinjianqq\2019赛题\A题\result\3.csv')
num=list(data_2_0.index)
num=list(map(str,num))
values=list(data_2_0['总消费金额'])
bar=(
     Bar()
         .add_xaxis(num)
         .add_yaxis("消费金额",values,label_opts=False )
         .set_global_opts(title_opts=opts.TitleOpts(title="基本示例", subtitle=""))
     )

bar.render(r'D:\xinjianqq\2019赛题\A题\result\柱状图3.1.html')
#print(num)
#for i in num:
#   s_information = df.loc[(df["顾客编号"] == i)]

