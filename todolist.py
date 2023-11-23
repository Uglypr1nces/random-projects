from tkinter import *
from tkinter.font import Font
import datetime

root = Tk()
root.geometry("500x300")
root.title("to do list")

my_font = Font(
    family="Terminal",
    size=20,
    weight="bold")

my_frame = Frame(root)
my_frame.pack(pady=10)

my_list = Listbox(my_frame,
    font=my_font,
    width=25,
    height=5,
    bg="systemButtonFace",
    bd=0,
    fg="#464646",
    highlightthickness=0,
    selectbackground = "#a6a6a6",
    activestyle = "none"
    )
my_list.pack(side=LEFT,fill=BOTH)

class thingstodo:
    def __init__(self, date, end, importance):
        self.date = date
        self.end = end
        self. importance = importance
        
stuff = ["example"]

for item in stuff:
    my_list.insert(END, item)

myscrollbar = Scrollbar(my_frame)
myscrollbar.pack(side=RIGHT,fill=BOTH)

my_list.config(yscrollcommand=myscrollbar.set)
myscrollbar.config(command=my_list.yview)

my_entry = Entry(root, font=("Helvetica",24))
my_entry.pack(pady=20)

button_frame = Frame(root)
button_frame.pack(pady=20)


def delete_item():
    my_list.delete(ANCHOR)


def details():
    selecteditem = my_list.get(ANCHOR)
    detailswindow = Toplevel(root)
    detailswindow.title("Details")
    detailswindow.geometry("400x200")

    date = datetime.datetime.now()
    details_frame = LabelFrame(detailswindow, text=f"Details for {selecteditem}")
    details_frame.pack(pady=10)

    question1 = "wann wollen sie es machen?"
    question2 = "wie wichtig ist es?"

    mylabel = Label(details_frame, text=f"{question1}")
    mylabel.pack()

    my_entry1 = Entry(details_frame, font=("Helvetica", 24))
    my_entry1.pack(pady=20)
    endline = "nothing"
    importance = "nothing"
    
    def next():
        endline = my_entry1.get()
        my_entry1.clipboard_clear()
        my_entry1.clipboard_append(endline)
        my_entry1.delete(0, 'end')
        my_entry1.update()  
        mylabel.config(text=question2)  
        importance = my_entry1.get()
        my_entry1.clipboard_clear()
        my_entry1.clipboard_append(endline)

    selecteditem = thingstodo(date,endline,importance)
    print(selecteditem.date)
    print(selecteditem.end)
    print(selecteditem.importance)
    Okbutton = Button(detailswindow,text="ok",command=next)
    Okbutton.pack()

def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)
    date = datetime.datetime.now()

def cross_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg="#dedede")
    my_list.selection_clear(0,END)

def uncross_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg="#464646")

delete_button = Button(button_frame,text="Delete smth",command=delete_item)
add_button = Button(button_frame,text="add smth",command=add_item)
cross_button = Button(button_frame,text="cross smth",command=cross_item)
uncross_button = Button(button_frame,text="uncross smth",command=uncross_item)
details_button = Button(button_frame,text="details",command=details)

delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1,padx=20)
cross_button.grid(row=0, column=2)
uncross_button.grid(row=0, column=3,padx=20)
details_button.grid(row=0, column=33,padx=20)

root.mainloop()