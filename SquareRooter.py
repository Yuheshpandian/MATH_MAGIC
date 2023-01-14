from tkinter import *

root = Tk()
root.geometry("500x500")
root.title('SquareRooter')
root.config(bg='Teal')

def find_root(num):
    e.delete(0,END)
    e.insert(0,"root of the number is: " +str(num**0.5))



lbl = Label(root,text = 'enter a square number')
lbl.place(relx=0.38,rely=0.4)
lbl.config(bg="sky blue")

e = Entry(root,width=50)
e.place(relx=0.2,rely=0.5)

btn = Button(root, text = "FIND ROOT",padx=10,pady=10, command=lambda : find_root(int(e.get())))
btn.place(relx=0.42,rely=0.7)
btn.config(bg="sky blue")

root.mainloop()