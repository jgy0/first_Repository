# coding:utf-8
import numpy as np
import pandas as pd

d = np.zeros((30, 6))
df = pd.DataFrame(d, columns=['高等数学', '大学英语', '大学物理', '大学体育', '程序设计技术', 'name'])
dict_0 = {"高等数学": 45, "大学英语": 67, "大学物理": 99, "name": 88, "大学体育": 77, "程序设计技术": "lisi"}
# df.iloc[0, :] = dict_0.values()
data = pd.read_csv(r'D:\xinjianqq\赛题a：教育平台的线上课程智能推荐策略\users.csv', encoding='gbk',header=None)
df.iloc[:, :] = data.iloc[:, :6]
print(df)