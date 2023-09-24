import tkinter
from tkinter import *


root = Tk()
root.title("Calcualtor")
root.geometry("320x500")
root.config(bg="#000000")

equation = ""

def clear():
    global equation
    equation = ""
    labelRes.config(text = equation)


def show(value):
    global equation
    equation += value
    labelRes.config(text = equation)


def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "Error!"
            equation = ""

    labelRes.config(text = result)






labelRes = Label(root, width=25, height=2, bg="#000000", text="", font="arial 30", fg="#fff", bd=1, relief=SOLID, anchor='w')
labelRes.pack(pady=10)

Button(root, text="C", width = 7, height=1, font="arial 25 bold", bd=1, fg="#fff", bg="#722F37" , command=lambda:clear()).place(x=5, y=110)
Button(root, text="%", width = 3, height=1,  font="arial 25 bold", bd=1, fg="#fff", bg="#2a9a00" ,command=lambda:show("%")).place(x=165, y=110)
Button(root, text="/", width = 3, height=1,  font="arial 25 bold", bd=1, fg="#fff", bg="#2a9a00" , command=lambda:show("/")).place(x=245, y=110)



Button(root, text="7", width = 3, height=1,  font="arial 25 bold", bd=1, fg="#fff", bg="#041E42" ,command=lambda:show("7")).place(x=5, y=190)
Button(root, text="8", width = 3, height=1,  font="arial 25 bold", bd=1, fg="#fff", bg="#041E42" , command=lambda:show("8")).place(x=85, y=190)
Button(root, text="9", width = 3, height=1,  font="arial 25 bold", bd=1, fg="#fff", bg="#041E42" ,command=lambda:show("9")).place(x=165, y=190)
Button(root, text="X", width = 3, height=1,  font="arial 25 bold", bd=1, fg="#fff", bg="#2a9a00" , command=lambda:show("*")).place(x=245, y=190)

Button(root, text="4", width = 3, height=1,  font="arial 25 bold", bd=1, fg="#fff", bg="#041E42" ,command=lambda:show("4")).place(x=5, y=270)
Button(root, text="5", width = 3, height=1,  font="arial 25 bold", bd=1, fg="#fff", bg="#041E42" ,command=lambda:show("5")).place(x=85, y=270)
Button(root, text="6", width = 3, height=1,  font="arial 25 bold", bd=1, fg="#fff", bg="#041E42" ,command=lambda:show("6")).place(x=165, y=270)
Button(root, text="-", width = 3, height=1,  font="arial 25 bold", bd=1, fg="#fff", bg="#2a9a00" ,command=lambda:show("-")).place(x=245, y=270)


Button(root, text="1", width = 3, height=1,  font="arial 25 bold", bd=1, fg="#fff", bg="#041E42" ,command=lambda:show("1")).place(x=5, y=350)
Button(root, text="2", width = 3, height=1,  font="arial 25 bold", bd=1, fg="#fff", bg="#041E42" ,command=lambda:show("2")).place(x=85, y=350)
Button(root, text="3", width = 3, height=1,  font="arial 25 bold", bd=1, fg="#fff", bg="#041E42" ,command=lambda:show("3")).place(x=165, y=350)
Button(root, text="+", width = 3, height=1,  font="arial 25 bold", bd=1, fg="#fff", bg="#2a9a00" ,command=lambda:show("+")).place(x=245, y=350)


Button(root, text="0",width = 3, height=1,  font="arial 25 bold", bd=1, fg="#fff", bg="#041E42" ,command=lambda:show("0")).place(x=5, y=430)
Button(root, text=".", width = 3, height=1,  font="arial 25 bold", bd=1, fg="#fff", bg="#041E42" ,command=lambda:show(".")).place(x=85, y=430)
Button(root, text="=", width = 7, height=1,  font="arial 25 bold", bd=1, fg="#fff", bg="#7a5a07", command=lambda:calculate()).place(x=165, y=430)


root.mainloop()
