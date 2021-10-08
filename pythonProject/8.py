import pandas as pd
import numpy as np
from pyecharts.charts import Bar
from pyecharts import options as opts
from datetime import datetime

df=pd.read_csv(r'D:\xinjianqq\2019赛题\A题\task1_1.csv',encoding='gbk')
df['销售日期']=list(map(str,df['销售日期']))
df['销售日期']=pd.to_datetime(df['销售日期'],format='%Y-%m-%d',errors='coerce')
df['周']=df['销售日期'].apply(lambda x:x.weekofyear)

#df.to_csv(r'D:\xinjianqq\2019赛题\A题\result\pd1.csv') 符合要求了，周次正常返回了

data_1=df[df['是否促销']=='是'] #获取促销的数据
data_2=df[df['是否促销']=='否']
data_1_new=pd.DataFrame(data_1) #促销的数据
data_2_new=pd.DataFrame(data_2)
#data_1_new.to_csv(r'D:\xinjianqq\2019赛题\A题\result\2-3.csv')

'''data_1_new['周']=df['销售日期'].apply(lambda x:x.weekofyear)
data_2_new['周']=df['销售日期'].apply(lambda x:x.weekofyear)'''

data_1_new_0=pd.pivot_table(data=data_1_new,index='周',values='销售金额',fill_value=0,aggfunc=[np.sum])
data_2_new_0=pd.pivot_table(data=data_2_new,index='周',values='销售金额',fill_value=0,aggfunc=[np.sum])

data_new_sum=pd.DataFrame({'促销':data_1_new_0.iloc[:,0],'不促销':data_2_new_0.iloc[:,0]})

data_new_sum.to_csv(r'D:\xinjianqq\2019赛题\A题\result\2-33.csv')

new_data1=list(data_new_sum['促销'])
new_data2=list(data_new_sum['不促销'])

new_data1_0=[]
new_data2_0=[]
for i in range(17):
    new_data1_0.append((new_data1[i+1]-new_data1[i])/new_data1[i])
    new_data2_0.append((new_data2[i+1]-new_data2[i])/new_data2[i])
bar=(
     Bar()
         .add_xaxis([ i for i in range(2,19)])
         .add_yaxis("促销",new_data1_0,label_opts=False )
         .add_yaxis("不促销",new_data2_0,label_opts=False )
         .set_global_opts(title_opts=opts.TitleOpts(title="基本示例", subtitle="环比增长率图"))
     )

bar.render(r'D:\xinjianqq\2019赛题\A题\result\柱状图.html')
#data_1_1=pd.pivot_table(data=data_1,index='是否促销',values='销售金额',fill_value=0)

#new_data=pd.DataFrame({'促销':data_1_1.query('是否促销==["是"]'),'不促销':data_1_1.query('是否促销==["是"]')})

