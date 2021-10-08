# coding:utf-8
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

iris = load_iris()

model = KMeans(n_clusters=3).fit(iris.data)
# 类中心个数   n_clusters
model.labels_  # 就是聚类的结果

# metrics模块 可以进行模型的评估
