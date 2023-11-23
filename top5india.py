import tkinter as tk
from tkinter import *
from PIL import ImageTk
from tkinter import font
from moviepy.editor import VideoFileClip
from moviepy.editor import TextClip


root = tk.Tk()
root.geometry("700x500")

goofyfont = font.Font(size=24)
smolgofyfont = font.Font(family="Fixedsys Regular",size=18)
img= PhotoImage(file='content/right.png', master= root)
img_label= Label(root,image=img)
img_label.place(x=0, y=0)

def india5():
    video_path = "content/top5india.mp4"
    video = VideoFileClip(video_path)
    video.preview()

def india4():
    video_path = "content/top4india.mp4"
    video = VideoFileClip(video_path)
    video.preview()
def india3():
    video_path = "content/top3india.mp4"
    video = VideoFileClip(video_path)
    video.preview()
def india2():
    video_path = "content/top2india.mp4"
    video = VideoFileClip(video_path)
    video.preview()
def india1():
    video_path = "content/top1india.mp4"
    video = VideoFileClip(video_path)
    video.preview()



button1 = Button(text="",font=smolgofyfont, fg="red",command=india5)
button1.pack()

button2 = Button(text="SUfSSSS",font=smolgofyfont,fg="blue",command=india4)
button2.pack()

button3 = Button(text="SUSSasdSS",font=smolgofyfont,fg="green",command=india3)
button3.pack()

button4 = Button(text="sussy black people",font=smolgofyfont,fg="pink",command=india2)
button4.pack()

button5 = Button(text="SUSSfdasSS",font=smolgofyfont,fg="gray",command=india1)
button5.pack()


Title = Label(text="TOP 5 INDA",font=goofyfont)
Title.pack()

root.mainloop()