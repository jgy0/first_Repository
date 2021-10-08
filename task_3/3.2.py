from pyecharts.charts import Line
import pandas as pd
import numpy as np
df=pd.DataFrame(pd.read_csv(r'D:\xinjianqq\2019赛题\A题\task1_1.csv',encoding='gbk'))
data_0=pd.pivot_table(data=df,index=['大类名称','销售月份'],values='销售金额',aggfunc=[np.sum],fill_value=0)
data_1=pd.DataFrame({'销售金额':data_0.iloc[:,0]})
#data_1.to_csv(r'D:\xinjianqq\2019赛题\A题\3-2.csv')
x_num=data_1.index
x_num_0=list(set(x_num))
l=len(x_num_0)
x=[]
for i in range(l):
    x1=x_num_0[i][0]
    x.append(x1)
y_0=list(data_1.iloc[0:4,0])
y_1=list(data_1.iloc[4:8,0])
y_2=list(data_1.iloc[8:12,0])
y_3=list(data_1.iloc[12:16,0])
y_4=list(data_1.iloc[16:20,0])
y_5=list(data_1.iloc[20:24,0])
y_6=list(data_1.iloc[24:28,0])
y_7=list(data_1.iloc[28:32,0])
y_8=list(data_1.iloc[32:36,0])
y_9=list(data_1.iloc[36:40,0])
y_10=list(data_1.iloc[40:44,0])
y_11=list(data_1.iloc[44:48,0])
y_12=list(data_1.iloc[48:52,0])
y_13=list(data_1.iloc[52:56,0])
y_14=list(data_1.iloc[56:60,0])
line1=(
    Line() # 生成line类型图表
    .add_xaxis(xaxis_data=['201501','201502','201503','201504'])  # 添加x轴，x_data数据生成x轴标签(注意xaxis_data的对象必须是列表，且列表元素是str)
    .add_yaxis(series_name=x[0],y_axis=y_0,is_smooth=True,is_symbol_show=False)  # 添加y轴，
    .add_yaxis(series_name=x[1],y_axis=y_1,is_smooth=True,is_symbol_show=False)
    .add_yaxis(series_name=x[2],y_axis=y_2,is_smooth=True,is_symbol_show=False)
    .add_yaxis(series_name=x[3],y_axis=y_3,is_smooth=True,is_symbol_show=False)
    .add_yaxis(series_name=x[4],y_axis=y_4,is_smooth=True,is_symbol_show=False)
    .add_yaxis(series_name=x[5],y_axis=y_5,is_smooth=True,is_symbol_show=False)
    .add_yaxis(series_name=x[6],y_axis=y_6,is_smooth=True,is_symbol_show=False)
    .add_yaxis(series_name=x[7],y_axis=y_7,is_smooth=True,is_symbol_show=False)
    .add_yaxis(series_name=x[8],y_axis=y_8,is_smooth=True,is_symbol_show=False)
    .add_yaxis(series_name=x[9],y_axis=y_9,is_smooth=True,is_symbol_show=False)
    .add_yaxis(series_name=x[10],y_axis=y_10,is_smooth=True,is_symbol_show=False)
    .add_yaxis(series_name=x[11],y_axis=y_11,is_smooth=True,is_symbol_show=False)
    .add_yaxis(series_name=x[12],y_axis=y_12,is_smooth=True,is_symbol_show=False)
    .add_yaxis(series_name=x[13],y_axis=y_13,is_smooth=True,is_symbol_show=False)
    .add_yaxis(series_name=x[14],y_axis=y_14,is_smooth=True,is_symbol_show=False)

)
line1.render(r'D:\xinjianqq\2019赛题\A题\result\折线图3-22.html') # 生成一个名为.html的网页文件