import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.DataFrame(pd.read_csv(r'D:\xinjianqq\赛题a：教育平台的线上课程智能推荐策略\login.csv',encoding='gbk'))
df.info()        #主要介绍数据集各列的数据类型，是否为空值，内存占用情况；