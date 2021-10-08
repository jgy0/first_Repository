import pandas as pd
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Page, Pie

df=pd.DataFrame(pd.read_csv(r'D:\xinjianqq\2019赛题\A题\task1_1.csv',encoding='gbk'))
data_1=df.loc[df['销售月份'].isin([201501])] #提取一月份的销售情况(注意201501数据类型是int，不是str)
data_2=df.loc[df['销售月份'].isin([201502])] #提取二月份的销售情况
data_3=df.loc[df['销售月份'].isin([201503])]
data_4=df.loc[df['销售月份'].isin([201504])]

data_1_sum=pd.pivot_table(data=data_1,index='大类名称',values='销售金额',aggfunc=[np.sum],fill_value=0) #一月的透视表
data_2_sum=pd.pivot_table(data=data_2,index='大类名称',values='销售金额',aggfunc=[np.sum],fill_value=0)
data_3_sum=pd.pivot_table(data=data_3,index='大类名称',values='销售金额',aggfunc=[np.sum],fill_value=0)
data_4_sum=pd.pivot_table(data=data_4,index='大类名称',values='销售金额',aggfunc=[np.sum],fill_value=0)

data_1_sum_new=pd.DataFrame({'一月销售额':data_1_sum.iloc[:,0]})
data_2_sum_new=pd.DataFrame({'二月销售额':data_2_sum.iloc[:,0]})
data_3_sum_new=pd.DataFrame({'三月销售额':data_3_sum.iloc[:,0]})
data_4_sum_new=pd.DataFrame({'四月销售额':data_4_sum.iloc[:,0]})
pie1=(
         Pie() #
         .add(series_name='销售金额占比', data_pair=[list(z) for z in zip(list(data_1_sum_new.index), list(data_1_sum_new['一月销售额']))],radius="55%",label_opts=opts.LabelOpts(is_show=False, position="center"),)
         .set_global_opts(title_opts=opts.TitleOpts(title="一月"))
         .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))

        )

pie1.render(r'D:\xinjianqq\2019赛题\A题\result\一月销售额222.html')
pie2=(
         Pie() #
         .add(series_name='销售金额占比', data_pair=[list(z) for z in zip(list(data_2_sum_new.index), list(data_2_sum_new['二月销售额']))],radius="55%",label_opts=opts.LabelOpts(is_show=False, position="center"),)
         .set_global_opts(title_opts=opts.TitleOpts(title="二月"))
         .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        )

pie2.render(r'D:\xinjianqq\2019赛题\A题\result\二月月销售额222.html')