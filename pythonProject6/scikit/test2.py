# coding:utf-8
from sklearn.linear_model import LinearRegression

clf = LinearRegression()
clf.fit([[0, 0], [1, 1], [2, 2]],[0,1,2])   # 模型训练
# 得到的模型应该就是  y=0.5 * x1 + 0.5 * x2 + 0
pre=clf.predict([[3, 3]])      # 模型预测
clf.coef_            # 系数属性
clf.intercept_          # 截距项


from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


boston = load_boston()
x = boston.data[:, 5:6]
clf = LinearRegression()
clf.fit(x,boston.target)  # 模型训练
clf.coef_                 # 回归系数
y_pre = clf.predict(x)    # 模型输出

plt.scatter(x,boston.target)
plt.plot(x,y_pre)
plt.show()



