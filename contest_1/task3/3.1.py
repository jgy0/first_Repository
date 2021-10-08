# coding:utf-8
import pandas as pd
from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn import preprocessing
def task9(data,data_1):
    data1=pd.read_csv('D:/桌面/B题//'+data,encoding='utf-8')

    data2=pd.read_csv("附件2.csv",encoding='gbk')
    data2 = data2.loc[data2['大类'] == ['饮料']]
    y_shop = list(data2['商品'])

    dalei=data1['商品'].unique().tolist()#提取出商品总列表，方便之后进行分类
    datasum=[]
    datasem=[]
    for i in dalei:
        data_x=data1[data1['商品']==i]['实际金额'].sum()
        data_t=data1[data1['商品']==i]['商品'].size
        datasum.append(data_x)#插入列表中
        datasem.append(data_t)
    task1_2 = pd.DataFrame({'商品':dalei,'总实际金额':datasum,'销售量':datasem})#对列表进行整理，制作成表单
    X = preprocessing.minmax_scale(task1_2['销售量'])
    X = pd.DataFrame(X, columns=['销售量'])
    kmeans=KMeans(n_clusters=3)
    kmeans.fit(X)
    #将标签插入players表格中
    task1_2['cluster']=kmeans.labels_
    task1=list(task1_2['cluster'])
    for i in range(len(task1)):
        if(task1[i] == 2):
            task1[i] = '热销'
        elif(task1[i]==1):
            task1[i]='正常'
        elif(task1[i]==0):
            task1[i]='滞销'
    task1_2['cluster']=task1
    task1=task1_2['商品']
    task2=task1_2['cluster']
    task=pd.DataFrame({'商品':task1,'标签':task2})
    #return task
    task.to_csv('D:/桌面/B题//'+data_1,encoding='utf-8')
task9('task1-1A.csv','task3-A.csv')
task9('task1-1B.csv','task3-B.csv')
task9('task1-1C.csv','task3-C.csv')
task9('task1-1D.csv','task3-D.csv')
task9('task1-1E.csv','task3-E.csv')