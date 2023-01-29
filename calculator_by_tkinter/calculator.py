from tkinter import *

window = Tk()
window.title("Calculator")
window.geometry("270x250")
window.resizable(FALSE,FALSE)

storage = ""

def hesapla(tus):
    global storage
    if tus in "0123456789":
        illustration.insert(END,tus)
        storage = storage+tus

    if tus in "+-*/":
        illustration.insert(END,tus)
        storage = storage +tus
    
    if tus == "=":
        illustration.delete(0,END)
        hesap = eval(storage,{"__builtins__":None},{})
        storage = str(hesap)
        illustration.insert(END,storage)

        
    if tus == "C":
        illustration.delete(0,END)
        storage=""

illustration = Entry(width=44,justify=RIGHT,)
illustration.grid(row=0,column=0,columnspan=3,ipady=4)


liste = ["1","2","3","4","5","6","7","8","9","0"]
liste2 = ["+","-","*","/","=","C"]
_row = 1
_column = 0

_row2 = 6
_column2=0


for i in liste:
    komut = lambda x=i : hesapla(x)
    Button(text=i,font="verdana 8",width=10,height=2,relief=GROOVE,command=komut).grid(row=_row,column=_column)
    _column +=1
    if _column > 2:
        _column = 0
        _row +=1

for i in liste2:
    komut = lambda x=i : hesapla(x)
    Button(text=i,font="verdana 8",bg="gray",width=10,height=2,relief=GROOVE,command=komut).grid(row=_row2,column=_column2)
    _column2 +=1
    if _column2 > 2:
        _column2 = 0
        _row2 +=1



mainloop()