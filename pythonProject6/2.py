# coding:utf-8
import numpy as np
arr=np.arange(1,13).reshape(3,4)
arr1=np.arange(13,25).reshape(3,4)


np.save('test.npy',arr)
arr_laod=np.load('test.npy')
print(arr_laod)

np.savez('arr&arr1',arr,arr1)

arr_arr_1=np.load('arr&arr1.npz')
print(arr_arr_1)
print(arr_arr_1.files)    #查看文件中有哪些数组对象
print(arr_arr_1['arr_0'])  #访问数据文件中的具体数据对象
#
np.savetxt("1.txt",arr1)
print(np.loadtxt('1.txt'))

