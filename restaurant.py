import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import font
import random

root = tk.Tk()
root.geometry("1400x788")

background_image = Image.open("content/restaurant.jpg")
background_photo = ImageTk.PhotoImage(background_image)

background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

overlay_image1 = Image.open("restaurant/golden apple.png")
overlay_photo1 = ImageTk.PhotoImage(overlay_image1)

overlay_image2 = Image.open("restaurant/pizza.png")
overlay_photo2 = ImageTk.PhotoImage(overlay_image2)

overlay_image3 = Image.open("restaurant/dog.jpg")
overlay_photo3 = ImageTk.PhotoImage(overlay_image3)

overlay_image4 = Image.open("restaurant/cat.jpg")
overlay_photo4 = ImageTk.PhotoImage(overlay_image4)

overlay_image5 = Image.open("restaurant/horse.png")
overlay_photo5 = ImageTk.PhotoImage(overlay_image4)

overlay_image6 = Image.open("restaurant/nutella.png")
overlay_photo6 = ImageTk.PhotoImage(overlay_image4)

# Create labels for overlay images and position them
overlay_label1 = tk.Label(root, image=overlay_photo1)
overlay_label2 = tk.Label(root, image=overlay_photo2)
overlay_label3 = tk.Label(root, image=overlay_photo3)
overlay_label4 = tk.Label(root, image=overlay_photo4)
overlay_image5 = tk.Label(root, image=overlay_photo5)
overlay_image6 = tk.Label(root, image=overlay_photo6)

overlay_label1.place(x=50, y=5)
overlay_label2.place(x=50, y=200)
overlay_label3.place(x=50, y=400)
overlay_label4.place(x=1200, y=50)
overlay_image5.place(x=1200,y=400)
overlay_image6.place(x=1200,y=200)

food = ["Golden apple","Pizza","dawgs","cat","horse","nutella"]

def add0():
    pass
def add1():
    pass
def add2():
    pass
def add3():
    pass
def add4():
    pass
def add5():
    pass
def add6():
    pass

def remove0():
    pass
def remove1():
    pass
def remove2():
    pass
def remove3():
    pass
def remove4():
    pass
def remove5():
    pass
def remove6():
    pass

def prices():
    pass


Plus0 =  Button(text = "+",command=add0)
Plus1 =  Button(text = "+",command=add1)
Plus2 =  Button(text = "+",command=add2)
Plus3 =  Button(text = "+",command=add3)
Plus4 =  Button(text = "+",command=add4)
Plus5 =  Button(text = "+",command=add5)
Plus6 =  Button(text = "+",command=add6)


minus0 =  Button(text = "-",command=remove0)
minus1 =  Button(text = "-",command=remove1)
minus2 =  Button(text = "-",command=remove2)
minus3 =  Button(text = "-",command=remove3)
minus4 =  Button(text = "-",command=remove4)
minus5 =  Button(text = "-",command=remove5)
minus6 =  Button(text = "-",command=remove6)

prices = Button(text="prices",command=prices)

Plus0.grid(row=24, column=2)
minus0.grid(row=34, column=2)

Plus1.place(x=0,y=200)
minus1.place(x=0,y=240)

Plus2.place(x=0,y=400)
minus2.place(x=0,y=440)


Plus6.place(x=1380,y=400)
minus6.place(x=1380,y=440)



root.mainloop()