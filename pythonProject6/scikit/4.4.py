# coding:utf-8
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report         # 混淆矩阵的分类报告
from sklearn.tree import export_graphviz
import graphviz


df = pd.read_csv(r'D:\应用\pycharm\PyCharm 2021.1.3\source\pythonProject6\scikit\titanic_data.csv', encoding='gbk')
x = df['Age'].mean()
df['Age'].fillna(x, inplace=True)
df.drop('PassengerId', axis=1, inplace=True)
# for x in df.index:
#     if df.loc[x, 'Sex'] == 'female':
#         df.loc[x,'Sex'] = 0
#     else:
#         df.loc[x,'Sex'] = 1
df.loc[df['Sex'] == 'female', 'Sex'] = 0
df.loc[df['Sex'] == 'male', 'Sex'] = 1
print(df)
Dtc = DecisionTreeClassifier(max_depth=5, random_state=8)  # 构建决策树模型
Dtc.fit(df.iloc[:, 1:],df['Survived'])          # 训练模型 fit(x,y)
pre = Dtc.predict(df.iloc[:, 1:])               # 模型预测
# pre == df['Survived']
classification_report(df['Survived'], pre)      # 分类报告

dot_data = export_graphviz(Dtc, feature_names=['Pclass', 'Sex', 'Age'], class_names='Survived')
# feature_names就是属性名称，class_names 类别的名称
graph = graphviz.Source(dot_data)
graph
