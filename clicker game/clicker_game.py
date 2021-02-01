from tkinter import *
from random import *

c=0
n=0
mult=1

def count():
    global c
    global n
    c += 1+n 
    entry.delete(0, 'end')
    entry.insert(0,c)

def clickpurschase_1(n):
    global c
    global mult
    if c >= 100:
        n += 1
        c=c-100
        print('you have purschased +1 points per click')
    else:
        print('you haven´t got enough points to buy this upgrade, click more!!!')
        
root=Tk()
root.geometry('500x700')
M=Menu(root)
root.config(menu=M)

m1=Menu(M,tearoff=0)
M.add_cascade(label='Click Upgrader', menu=m1)
m1.add_command(label='+1 points per click',command=lambda:clickpurschase_1(2),)
button = Button(text="CLICK",command = count,)
label = Label(text="SCORE",font = 'arial 20',bg = 'red')
entry = Entry(root)
label.pack(side = TOP , pady = 5)
entry.pack(side = TOP , pady = 5)
button.pack(side=TOP , pady = 5)
root.mainloop()