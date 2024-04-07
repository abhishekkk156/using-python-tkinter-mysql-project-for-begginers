from tkinter import *
from time import strftime
root = Tk()
root.title("digital watch")
root.resizable(False, False)
def time():
    string = strftime('%H:%M:%S:%p')
    label.config(text=string)
    label.after(1000, time)
label = Label(root , font=("ds-digital", 30), background="black", foreground="red")
label.pack(anchor='center')
time()
mainloop()