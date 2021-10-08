# # coding:utf-8
# import datetime
# import time
#
# import pandas as pd
# import numpy as np
#
# a = time.time()
# # 1569642653，得到 10位时间戳，int
# b = int(a)
# # 1569642653104，得到 13位时间戳，int
# c = int(a * 1000)
# # 1569642653104173，得到 16位时间戳，int
# d = int(a * 1000000)
#
# # print(a)
# # print(b)
# # print(c)
# # print(d)
# e = time.localtime(a)
# f = time.localtime(b)
# g = time.localtime(c//1000)
# h = time.localtime(d//1000000)
#
# print(type(e))
# i = time.mktime(e)
# j = time.mktime(f)
# k = time.mktime(g)
# l = time.mktime(h)
# good = time.strftime("%Y-%m-%d %H:%M:%S %A", e)
# print(good)
# nice = time.strptime(good,"%Y-%m-%d %H:%M:%S %A")
# print(nice)

import pandas as pd
import time
import datetime
import random
import numpy as np

# df = pd.DataFrame({
#     'some_data' : [random.randint(100,999) for i in range(1,10)],
#     'a_col' : '2019-07-12',
#     'b_col' : datetime.datetime.now().date(),
#     'c_col' : time.time()},
#     index=range(1,10))
# df.to_csv(r'D:\xinjianqq\赛题a：教育平台的线上课程智能推荐策略\0.csv')
# df.info()
# print(type(df))

# print(datetime.datetime.now().date())  #2021-07-27
# print(type(datetime.datetime.now().date()))  #<class 'datetime.date'>

#df.groupby(df['c_col'].dt.date).some_data.agg('sum')

# data = {'玩具':['车','飞机','轮船'], '数量':[3,2,5], '价格':[100,90,80]}
# df = pd.DataFrame(data)
#
# print(df)
# print(df.to_dict())
# print('-'*30)
# print(df.to_dict(orient='records'))

arr = np.arange(6)
print(arr.dtype)
str_arr = arr.astype('string_')
print(str_arr)
print(type(str_arr[0]))

n=r'D:\xinjianqq\赛题a：教育平台的线上课程智能推荐策略\project\task3.2.txt'