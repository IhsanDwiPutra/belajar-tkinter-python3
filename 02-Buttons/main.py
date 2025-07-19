from tkinter import *

root = Tk()

def myClick():
	myLabel = Label(root, text="Wah Anda mengklik saya")
	myLabel.pack()

myButton = Button(root, text="Klik saya dong", padx=50, pady=20, command=myClick, fg="green", bg="#fffffa")
myButton.pack()

root.mainloop()