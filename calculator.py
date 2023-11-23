import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry("300x100")
x = False
y = False
result = 3
def num1():
    x = 1
    result = 1
def num2():
    x = 2
    result = 2
def num3():
    x = 3
    result = 1
def num4():
    x = 4
    result = 1
def num5():
    x = 5
    result = 1
def num6():
    x = 6
    result = 1
def num7():
    x = 7
    result = 1
def num8():
    x = 8
    result = 1
def num9():
    x = 9
    result = 1
def num0():
    x = 0
    result = 1
def plus():
    x + y
def minus():
    x - y
def division():
    x / y
def multiply():
    x * y

num1 = Button(text = "1", command=num1)
num2 = Button(text = "2", command=num2)
num3 = Button(text = "3", command=num3)
num4 = Button(text = "4", command=num4)
num5 = Button(text = "5", command=num5)
num6 = Button(text = "6", command=num6)
num7 = Button(text = "7", command=num7)
num8 = Button(text = "8", command=num8)
num9 = Button(text = "9", command=num9)
num0 = Button(text = "0", command=num0)
plus = Button(text = "+", command=plus)
minus = Button(text = "-", command=minus)
division = Button(text = "%", command=division)
multiply = Button(text = "*", command=multiply)

num1.place(x=0, y=5)
num2.place(x=20, y=5)
num3.place(x=40, y=5)
num4.place(x=0, y=25)
num5.place(x=20, y=25)
num6.place(x=40, y=25)
num7.place(x=0, y=45)
num8.place(x=20, y=45)
num9.place(x=40, y=45)
num0.place(x=0, y=60)
plus.place(x=60, y=0)
minus.place(x=60, y=20)
division.place(x=60, y=40)
multiply.place(x=20, y=80)


root.mainloop()