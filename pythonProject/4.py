import matplotlib.pyplot as plt#约定俗成的写法plt
import numpy as np
import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.faker import Faker

df=pd.DataFrame(pd.read_csv(r"D:\xinjianqq\2019赛题\A题\task1_1.csv",encoding='gbk'))
data_0_1=df.loc[df['商品类型'].isin(['生鲜'])]   #筛选出生鲜的数据
data_0_2=df.loc[df['商品类型'].isin(['一般商品'])]   #筛选出一般商品的数据
data_1=pd.pivot_table(data=data_0_1,index=['销售日期'],values=['销售金额'],aggfunc=[np.sum],fill_value=0)  #创建一个生鲜透视表
# data_1.to_csv(r'D:\xinjianqq\2019赛题\A题\result\2.csv')
data_2=pd.pivot_table(data=data_0_2,index=['销售日期'],values=['销售金额'],aggfunc=[np.sum],fill_value=0)  #创建一个一般商品的透视表
new_data=pd.DataFrame({'生鲜每日销售额':data_1.iloc[:,0],'一般商品每日销售额':data_2.iloc[:,0]})


x_data=list(new_data.index) #x的下表
y_list_1=list(new_data['生鲜每日销售额']) #y_1的值(生鲜)
y_list_2=list(new_data['一般商品每日销售额']) #y_2的值(一般商品)
x_data1=list(map(str,x_data))
line1=(
    Line() # 生成line类型图表
    .add_xaxis(xaxis_data=x_data1)  # 添加x轴，x_data数据生成x轴标签(注意xaxis_data的对象必须是列表，且列表元素是str)
    .add_yaxis(series_name='生鲜类',y_axis=y_list_1,is_smooth=True,is_symbol_show=False)  # 添加y轴，是使用生鲜数据生成y轴数值
    .add_yaxis(series_name='一般商品',y_axis=y_list_2,is_smooth=True,is_symbol_show=False)

)
line1.render(r'D:\xinjianqq\2019赛题\A题\result\折线图.html') # 生成一个名为.html的网页文件



