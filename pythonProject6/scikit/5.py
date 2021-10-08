# coding:utf-8

from sklearn.datasets import load_iris
import numpy as np

iris = load_iris()
data = iris.data
# 1. 选中心
n = len(data)
k = 3
knn = data[:k, :]
dist = np.zeros((n, k+1))
knn_new = np.zeros((k,data.shape[1]))
# 2. 求距离
while True:
    for i in range(n):
        for j in range(k):
            # dist[i][j] = np.sqrt((data[i, :] - knn[j, :])**2) # (data[i, :] - knn[j, :])**2 是个向量
            dist[i][j] = np.sqrt(sum((data[i, :] - knn[j, :]) ** 2))
        # 3. 归类
        dist[i][k] = np.argmin(dist[i, :k])        # np.argmin获得最小值的索引
    dist
    # 4. 求新类中心
    for i in range(k):
        index = dist[:, k] == i
        knn_new[i] = data[index, :].mean(axis=0)
    # index_0 = dist[:, k] == 0
    # index_1 = dist[:, k] == 1
    # index_2 = dist[:, k] == 2
    #
    # knn_new[0] = data[index_0, :].mean(axis=0)
    # knn_new[1] = data[index_1, :].mean(axis=0)
    # knn_new[2] = data[index_2, :].mean(axis=0)

    knn_new
    if np.all(knn == knn_new):
        break
    else:
        knn = knn_new
        # for i in range(k):
        #     knn[i] = knn_new[i]
        #
    # 5. 判定结束


