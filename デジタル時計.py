from tkinter import *
from time import strftime

root = Tk()
root.title('デジタル時計')

def time():
    clock = strftime('%H:%M:%S %p')
    label.config(text=clock)
    label.after(1000,time)

label = Label(root,font=("impact",80,'bold'), bg ='cyan',fg="black")
label.pack(anchor='center')
time()

root.mainloop()
