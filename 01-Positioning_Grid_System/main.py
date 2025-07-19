from tkinter import *

root = Tk()

myLabel1 = Label(root, text="Hai Duniaaa") # .grid(row=0, column=0)
myLabel2 = Label(root, text="Nama saya Agus siTompul") # .grid(row=1, column=1)
myLabel3 = Label(root, text="Ini contoh ya guysss") # .grid(row=0, column=3)

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)
myLabel3.grid(row=0, column=3)


root.mainloop()