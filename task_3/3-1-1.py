# coding:utf-8
# coding:utf-8
import pandas as pd
import numpy as np
import pyecharts.options as opts
from pyecharts.charts import WordCloud
import collections

df=pd.read_csv(r'D:\xinjianqq\2019赛题\A题\task1_1.csv',encoding='gbk')
data_0=pd.pivot_table(data=df,index='顾客编号',values='销售金额',aggfunc=[np.sum]) #每个用户的总消费额
data_1=pd.DataFrame({'总消费金额':data_0.iloc[:,0]})
#data_1.to_csv(r'D:\xinjianqq\2019赛题\A题\result\3-1.csv')
data_2=data_1.sort_values(by='总消费金额',ascending=False)   #按照消费排名
data_2_0=pd.DataFrame( {'总消费金额':data_2.iloc[0:10,0] })         #筛选出排名前十
x=list(data_2_0.index)
sum=[]
for i in x:
    n=df[df['顾客编号']==i]
    n_0=df.iloc[:,5]
    n_1=list(n_0)
    sum.extend(n_1)
#sum=list(map(str,sum))
d=collections.Counter(sum)
d=dict(d)                       #必须dict转换一下
d=dict([(x,str(y)) for x,y in d.items()])
new_list=[(x,y) for x,y in d.items()]

#d=list(zip(data_2_0.index,list(data_2_0.iloc[:,0])))
(
    WordCloud()
    .add(series_name="用户画像", data_pair=new_list, word_size_range=[10, 100])
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="用户画像", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
        ),
        tooltip_opts=opts.TooltipOpts(is_show=True),
    )
    .render(r"D:\xinjianqq\2019赛题\A题\result\wordcloud.html")
)
