# coding:utf-8
from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("First Window")
window.geometry("350x200")
combo = Combobox(window)
combo['values'] = (1,2,3,4,5,"Text")
combo.current(0)
combo.grid(column=0, row=0)
window.mainloop()