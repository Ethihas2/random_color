from tkinter import *
import random

root = Tk()
root.geometry("700x800")
root.title("Random Color")

list = ["maroon1","lawn green","magenta2","purple1","springgreen2","chocolate1", "deep pink","cyan"]

def random_color():
    random_num = random.randint(0,7)
    random_color = list[random_num]
    root.configure(background = random_color)

button1 = Button(root,text="Click me", command=random_color)
button1.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()