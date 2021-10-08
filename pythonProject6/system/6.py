# coding:utf-8
# 对初代程序进行改进，先总体的布局，使用pack， 成绩管理系统2.0
import random
import numpy as np
import pandas as pd
import tkinter
from tkinter import *
from random import randint
from tkinter import messagebox

top = Tk()
top.title("学生成绩管理系统")
top.geometry("1300x800")
canvas = Canvas(top, bg='green', height=200, width=500)
photo = PhotoImage(file='tk.gif')
image = canvas.create_image(50, 50, anchor=NW, image=photo)
canvas.pack()
# L2 = Label(top, image=photo)
# L2.grid(row=0, column=3, columnspan=3, rowspan=3, sticky=W+E+N+S, padx=15, pady=15)
L1 = Label(top, text="welcome to our system",  font=("Arial Bold", 15))
L1.grid(column=6, row=0)
frame1 = Frame(top, height=60, width=80)
frame1.grid(row=0, column=8)
Information = Label(top, text='用户手册'
                              '教程，进行成绩输入的时候采用入关键字输入，如高等数学=98'
                              '............................................'
                              '.............................................'
                              '..............................................'
                              '...............................................'
                              '..............................................'
                              '.............................................',
                    font=("隶书", 20, 'italic'),
                    foreground=f'#{randint(0,16777215):06x}',
                    background='#cccccc',
                    cursor='circle',
                    anchor='center',
                    wraplength=800,
                    justify='left'
                    )
Information.grid(column=8, row=0, columnspan=5, rowspan=3)

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
        return self.data

    def find_sore(self, name):
        """ 成绩查找"""
        score = self.data.loc[self.data['name']==name, :]
        print(score)

    def out_sore(self):
        """ 成绩打印输出"""
        return (self.data)


student_0 = StudentS1()


def begin():
    L1.configure(text="初始化成功")
    messagebox.showinfo("Message title", "successful")
    print(student_0.data)


def code1():
    messagebox.askyesno("Message title", "输入成绩")
    s = txt.get()
    L1.configure(text=s)
    # student_0.input_core(s)


def code2():
    messagebox.askyesno("Message title", "文件导入成绩")
    student_0.input_file(txt.get())

def code3():
    messagebox.askyesno("Message title", "修改成绩")
    student_0.change_sore(txt.get())

def code4():
    messagebox.askyesno("Message title", "删除成绩")
    student_0.rm_sore(txt.get())


def code5():
    messagebox.askyesno("Message title", "成绩排序'")
    n = student_0.sort_sore()
    L1.configure(text=f"{n}")


def code6():
    messagebox.askyesno("Message title", "成绩查找")
    student_0.find_sore(txt.get())


def code7():
    messagebox.askyesno("Message title", "成绩打印输出")
    n = student_0.out_sore()
    L1.configure(text=f'{n}')


btn = Button(top, text="初始化", bg="#F0F8FF", fg="red", width=10, height=3, command=begin)
btn.grid(column=0, row=0)
text_0 = ['输入成绩', '文件导入成绩', '修改成绩', '删除成绩', '成绩排序', '成绩查找', '成绩打印输出']
n1 = code1
n2 = code2
n3 = code3
n4 = code4
n5 = code5
n6 = code6
n7 = code7
instructions = [n1, n2, n3, n4, n5, n6, n7]
for i in range(7):
    txt = Entry(top, width=10)
    txt.grid(column=1, row=i + 1)
    btn = Button(top, text=text_0[i], bg="#F0F8FF", fg="black", width=10, height=3, command=instructions[i])
    btn.grid(column=0, row=i+1)

# txt = Entry(top, width=10)
# txt.grid()
top.mainloop()
