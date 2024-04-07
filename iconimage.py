from tkinter import *
from tkinter import ttk
root=Tk()
root.title("CCIT")
root.geometry("500x400")

main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

my_canvas=Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

second_frame = Frame(my_canvas)

my_canvas.create_window((0,0), window=second_frame, anchor="nw")



for c in range (20):
    Button(second_frame, text=f'Button {c} cc!').grid(row=c, column=0, pady=10, padx=10)

root.mainloop()
