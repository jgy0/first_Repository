# coding:utf-8
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression    # 线性回归
from sklearn.model_selection import train_test_split   # 留出法
from sklearn.metrics import classification_report      # 模型评估

data = pd.read_csv('LogisticRegression.csv')
X_train, X_test, y_train, y_test = train_test_split(data.iloc[:, 1:], data['admit'], test_size=0.2)
clf = LogisticRegression()
clf.fit(X_train, y_train)                              # 训练模型
pre = clf.predict(X_test)
# np.mean(pre == y_test)
res = classification_report(y_test, pre)
print(res)

