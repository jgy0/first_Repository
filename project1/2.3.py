# coding:utf-8
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar

df=pd.DataFrame(pd.read_csv(r'D:\xinjianqq\赛题a：教育平台的线上课程智能推荐策略\login.csv',encoding='gbk'))
df['login_time']=pd.to_datetime(df['login_time'])
df['daynameofweek']=df['login_time'].dt.day_name()

#df.to_csv(r'D:\xinjianqq\赛题a：教育平台的线上课程智能推荐策略\project\2.2.csv')
# data0=pd.pivot_table(df,index=['daynameofweek'],values=[''])

data=df.loc[df['daynameofweek'].isin(['Monday','Tuesday','Wednesday','Thursday','Friday'])]
data_yes=pd.DataFrame(data)   #工作日的数据
data_no=pd.DataFrame(df.loc[df['daynameofweek'].isin(['Saturday','Sunday'])])
# data_0.to_csv(r'D:\xinjianqq\赛题a：教育平台的线上课程智能推荐策略\project\2.2_2.csv')

data_yes['login_time']=data_yes['login_time'].dt.hour
data_no['login_time']=data_no['login_time'].dt.hour
# data_yes.to_csv(r'D:\xinjianqq\赛题a：教育平台的线上课程智能推荐策略\project\222.csv')


data_yes_1=pd.DataFrame(data_yes.loc[data_yes['login_time'].isin([0,1])])
data_yes_2=data_yes.loc[data_yes['login_time'].isin([2,3])]
data_yes_3=data_yes.loc[data_yes['login_time'].isin([4,5])]
data_yes_4=data_yes.loc[data_yes['login_time'].isin([6,7])]
data_yes_5=data_yes.loc[data_yes['login_time'].isin([8,9])]
data_yes_6=data_yes.loc[data_yes['login_time'].isin([10,11])]
data_yes_7=data_yes.loc[data_yes['login_time'].isin([12,13])]
data_yes_8=data_yes.loc[data_yes['login_time'].isin([14,15])]
data_yes_9=data_yes.loc[data_yes['login_time'].isin([16,17])]
data_yes_10=data_yes.loc[data_yes['login_time'].isin([18,19])]
data_yes_11=data_yes.loc[data_yes['login_time'].isin([20,21])]
data_yes_12=data_yes.loc[data_yes['login_time'].isin([22,23])]

#data_yes_1.to_csv(r'D:\xinjianqq\赛题a：教育平台的线上课程智能推荐策略\project\2222.csv')

data_0_0=[]
n1=len(data_yes_1.index)
n2=len(data_yes_2.index)
n3=len(data_yes_3.index)
n4=len(data_yes_4.index)
n5=len(data_yes_5.index)
n6=len(data_yes_6.index)
n7=len(data_yes_7.index)
n8=len(data_yes_8.index)
n9=len(data_yes_9.index)
n10=len(data_yes_10.index)
n11=len(data_yes_11.index)
n12=len(data_yes_12.index)

data_0_0.append(n1)
data_0_0.append(n2)
data_0_0.append(n3)
data_0_0.append(n4)
data_0_0.append(n5)
data_0_0.append(n6)
data_0_0.append(n7)
data_0_0.append(n8)
data_0_0.append(n9)
data_0_0.append(n10)
data_0_0.append(n11)
data_0_0.append(n12)
print(data_0_0)

data_no_1=pd.DataFrame(data_no.loc[data_no['login_time'].isin([0,1])])
data_no_2=data_no.loc[data_no['login_time'].isin([2,3])]
data_no_3=data_no.loc[data_no['login_time'].isin([4,5])]
data_no_4=data_no.loc[data_no['login_time'].isin([6,7])]
data_no_5=data_no.loc[data_no['login_time'].isin([8,9])]
data_no_6=data_no.loc[data_no['login_time'].isin([10,11])]
data_no_7=data_no.loc[data_no['login_time'].isin([12,13])]
data_no_8=data_no.loc[data_no['login_time'].isin([14,15])]
data_no_9=data_no.loc[data_no['login_time'].isin([16,17])]
data_no_10=data_no.loc[data_no['login_time'].isin([18,19])]
data_no_11=data_no.loc[data_no['login_time'].isin([20,21])]
data_yes_12=data_no.loc[data_no['login_time'].isin([22,23])]

#data_yes_1.to_csv(r'D:\xinjianqq\赛题a：教育平台的线上课程智能推荐策略\project\2222.csv')

data_0_0_no=[]
n1=len(data_yes_1.index)
n2=len(data_yes_2.index)
n3=len(data_yes_3.index)
n4=len(data_yes_4.index)
n5=len(data_yes_5.index)
n6=len(data_yes_6.index)
n7=len(data_yes_7.index)
n8=len(data_yes_8.index)
n9=len(data_yes_9.index)
n10=len(data_yes_10.index)
n11=len(data_yes_11.index)
n12=len(data_yes_12.index)

data_0_0_no.append(n1)
data_0_0_no.append(n2)
data_0_0_no.append(n3)
data_0_0_no.append(n4)
data_0_0_no.append(n5)
data_0_0_no.append(n6)
data_0_0_no.append(n7)
data_0_0_no.append(n8)
data_0_0_no.append(n9)
data_0_0_no.append(n10)
data_0_0_no.append(n11)
data_0_0_no.append(n12)
x=[
            "0-1点",
            "2-3点",
            "4-5点",
            "6-7点",
            "8-9点",
            "10-11点",
            "11-12点",
            "12-13点",
            "14-15点",
            "16-17点",
            "18-19点",
            "20-21点",
            "22-23点",
        ]
c = (
    Bar()
    .add_xaxis(x)
    .add_yaxis("工作日", data_0_0)
    .set_global_opts(title_opts=opts.TitleOpts(title="工作日", subtitle=""))
    .render(r"D:\xinjianqq\赛题a：教育平台的线上课程智能推荐策略\project\work.html")
)
d = (
    Bar()
    .add_xaxis(x)
    .add_yaxis("非工作日", data_0_0_no)
    .set_global_opts(title_opts=opts.TitleOpts(title="非工作日", subtitle=""))
    .render(r"D:\xinjianqq\赛题a：教育平台的线上课程智能推荐策略\project\no_work.html")
)
# c = (
#     Bar()
#     .add_xaxis(
#         [
#             "0-1点",
#             "2-3点",
#             "4-5点",
#             "6-7点",
#             "8-9点",
#             "10-11点",
#             "11-12点",
#             "12-13点",
#             "14-15点",
#             "16-17点",
#             "18-19点",
#             "20-21点",
#             "22-23点",
#         ]
#     )
#     .add_yaxis("工作日", data_0_0)
#
#     .set_global_opts(
#         xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
#         title_opts=opts.TitleOpts(title="Bar工作日", subtitle=""),
#     )
#     .render(r"D:\xinjianqq\赛题a：教育平台的线上课程智能推荐策略\bar_work.html")
# )
#
# c = (
#     Bar()
#     .add_xaxis(
#         [
#             "0-1点",
#             "2-3点",
#             "4-5点",
#             "6-7点",
#             "8-9点",
#             "10-11点",
#             "11-12点",
#             "12-13点",
#             "14-15点",
#             "16-17点",
#             "18-19点",
#             "20-21点",
#             "22-23点",
#         ]
#     )
#     .add_yaxis("非工作日", data_0_0_no)
#
#     .set_global_opts(
#         xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
#         title_opts=opts.TitleOpts(title="Bar非工作日", subtitle=""),
#     )
#     .render(r"D:\xinjianqq\赛题a：教育平台的线上课程智能推荐策略\bar_notwork.html")
# )