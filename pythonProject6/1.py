# coding:utf-8
import numpy as np
import pandas as pd

# arr3=np.arange(1,13).reshape(3,4)
# print(arr3)
#
#
# arr=np.arange(10)
# print(arr)
# print(arr3[arr3[:,0]>4])
# print(arr3[:,0]>4)
# print(arr3[arr3[:,0]>4,:])
arr1=np.arange(12)
arr2=np.arange(12,24)
a1=arr1.reshape(3,4)
a2=arr2.reshape(3,4)
print(a1)
print(a2)
print(arr1.ravel())
print(np.hstack((a1,a2)))         #数据横向组合
print(np.vstack((a1,a2)))         #数组纵向组合
n=np.concatenate((a1,a2),axis=0)    #axis=1横向组合，axis=0纵向组合
# print(n)
# print(np.hsplit(a1,2))        #数组纵向分割
# print(np.vsplit(a1,3))        #数组横向分割



# print(np.mat("1 2 3 ;4 5 6;7 8 9"))
print(np.matrix([[1,2,3],[4,5,6],[7,8,9]]))
# print(np.bmat("arr1 arr2;arr1,arr2"))       #矩阵拼接

arr3=np.array([0.2,0.6,0.68])
arr4=np.array([0.2,0.3,0.76])

print(np.all(arr3==0.2))   #np.all逻辑与
print(np.any(arr3==0.2))   #np.any逻辑或

c=np.array([1,2,3,4])
d=c**2
print(d)