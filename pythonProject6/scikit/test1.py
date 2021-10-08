# coding:utf-8
from sklearn.metrics import precision_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_iris
from sklearn.svm import SVC
iris=load_iris()
clf=SVC(kernel='linear', C=1)
score=cross_val_score(clf, iris.data, iris.target, cv=5)

print(score)

y_true = [1, 0, 1, 1, 0]  #样本实际值
y_pred = [1, 0, 1, 0, 0]  #模型预测值
# res = precision_score(y_true,y_pred,average=None) #准确率
res1 = confusion_matrix(y_true,y_pred)   #混淆矩阵
res2 = classification_report(y_true,y_pred)


# print(res)
# print(res2)
