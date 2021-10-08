# coding:utf-8
import numpy as np
import pandas as pd


class StudentS1:
    i = 0

    def __init__(self):
        self.d = np.zeros((30, 7))
        self.data = pd.DataFrame(self.d, columns=['高等数学', '大学英语', '大学物理', '大学体育', '程序设计技术', 'name', 'mean'])

    # def input_core(self, name, n1, n2, n3, n4, n5):
    #
    #     """ 输入成绩"""
    #     self.name = name
    #     self.score['高等数学'] = n1
    #     self.score['大学英语'] = n2
    #     self.score['大学物理'] = n3
    #     self.score['大学体育'] = n4
    #     self.score['程序设计技术'] = n5
    def input_core(self,  **kwargs):
        """输入成绩"""
        kw = kwargs
        self.data.iloc[StudentS1.i, :] = kw.values()
        StudentS1.i = StudentS1.i + 1

    def input_file(self, path):
        """文件导入成绩"""
        df = pd.read_csv(path, encoding='gbk')
        n = len(df)
        # self.data.iloc[:, :] = df
        self.data = df
        # self.data = self.data.reindex(index=self.data['name'].values)

    def change_sore(self, name, **kwargs):
        """ 修改成绩"""
        self.data.loc[self.data['name']==name, :'程序设计技术'] = kwargs.values()

    def rm_sore(self, name):
        """ 删除成绩"""
        self.data.loc[self.data['name']==name, :]=0.0
        # self.data.drop(name, axis=0, inplace=True)

    def sort_sore(self):
        """ 成绩排序"""
        self.data.iloc[:, 6] = self.data.mean(1)
        self.data = self.data.sort_values(by="mean")

    def find_sore(self, name):
        """ 成绩查找"""
        score = self.data.loc[self.data['name']==name, :]
        print(score)

    def out_sore(self):
        """ 成绩打印输出"""
        print(self.data)


if __name__=='__main__':
    stu = StudentS1()
    stu.out_sore()
    stu.input_core(n1=66, n2=77, n3=88, n4=33, n5=88, name='lisi', ave=0)
    stu.out_sore()
    stu.input_core(n1=66, n2=77, n3=88, n4=33, n5=88, name='si', ave=0)
    stu.find_sore('si')
    stu.input_core(n1=66, n2=87, n3=88, n4=83, n5=88, name='zhangsan', ave=0)
    stu.input_core(n1=66, n2=77, n3=88, n4=33, n5=88, name='shi', ave=0)
    stu.input_core(n1=66, n2=77, n3=88, n4=33, n5=88, name='wang', ave=0)
    stu.change_sore('si', n1=61, n2=71, n3=81, n4=31, n5=81)
    stu.rm_sore('shi')
    stu.sort_sore()
    stu.out_sore()
