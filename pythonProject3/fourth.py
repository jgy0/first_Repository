import matplotlib.pyplot as plt
x=[i for i in range(1,13)]
y=[5.2,2.7,5.8,5.7,7.3,9.2,18.7,15.6,20.5,18.0,7.8,6.9]
plt.rcParams['font.sans-serif'] = 'simhei'
plt.rcParams['axes.unicode_minus'] = False
plt.plot(x,y,'bv:',)
plt.xlabel('月份',fontsize=18)
plt.ylabel('营业额（万元）',fontsize=18)
plt.show()