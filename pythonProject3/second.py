import matplotlib.pyplot as plt
import pandas
plt.rcParams['font.sans-serif'] = 'simhei'
plt.rcParams['axes.unicode_minus'] = False
num=[i for i in range(1,31)]
price=[]
profit=[]
save=[]
for n in range(1,31):
    price.append( 75 * n * (1-(0.01 * n)))
    profit.append(75 * n * (1-(0.01 * n))-49*n)
    save.append(75*n-75 * n * (1-(0.01 * n)))
plt.plot(num,price,'-',label='顾客消费',color='b') #顾客消费
plt.plot(num,profit,'-',label='商家收益',color='g') #商家收益
plt.plot(num,save,'-',label='省钱',color='y') #省钱
plt.xlabel('购买件数',fontsize=18)
plt.ylabel('金额',fontsize=18)
plt.legend()
plt.show()

