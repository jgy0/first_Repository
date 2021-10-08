import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.DataFrame(pd.read_csv(r'D:\qq聊天记录\1赛题A：教育平台的线上课程智能推荐策略\study_information.csv',encoding='gbk'))
# data=df[df.isnull().T.any()]          #筛选有空值的行
# data.to_csv(r'E:\tmp\project\rm_null.csv',encoding='gbk')
# print(data[data['user_id']=='用户44241'].dtypes)     #判断DataFrame中的数据类型
df2=pd.DataFrame(pd.read_csv(r'D:\qq聊天记录\1赛题A：教育平台的线上课程智能推荐策略\users.csv',encoding='gbk'))


# data=pd.DataFrame(df2['recently_logged']=='--')
# data.to_csv(r'E:\tmp\project\1.csv',encoding='gbk')


# def rm_miss_value(n):  #缺失值处理
#     pass
# def error_deal(n):        #异常值处理
#     data_1=n
#     if data_1[data_1['recently_logged']=='--'] and data_1[data_1['learn_time']==0]:   #学习时常为零的异常值用注册时间填充最后登录时间
#         data_1['recently_logged']=data_1['register_time']
#     elif data_1[data_1['recently_logged']=='--']:
#         id=data_1['user_id']
#         if df2[id]!=None:
#             data_1['recently_logged']=df[]



def main(n):
    pass
