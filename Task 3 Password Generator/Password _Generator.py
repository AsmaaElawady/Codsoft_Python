from tkinter import *
import tkinter as tk
import string
import random
import pyperclip

def generator():
    passwordField.delete(0,END)
    smallAlphabets = string.ascii_lowercase
    capitalAlphabets = string.ascii_uppercase
    numbers = string.digits
    specialChar = string.punctuation

    all_chars = smallAlphabets + capitalAlphabets + numbers + specialChar
    password_length = int(lengthBox.get())
    if choice.get()==1:
        passwordField.insert(0,random.sample(all_chars,password_length))

    if choice.get() == 2:
        passwordField.insert(0, random.sample(capitalAlphabets, password_length))

    if choice.get()==3:
        passwordField.insert(0,random.sample(smallAlphabets,password_length))


def copy():
    randomPassword=passwordField.get()
    pyperclip.copy(randomPassword)



root = tk.Tk()
root.config(bg="#004953")
root.geometry("600x450")
root.title("Password Generator")
choice=IntVar()
Font="arial 13 bold"

Password = tk.Label(root, text="Password Generator", font="arial 20 bold", bg="#004953", fg="white")
Password.pack(side="top", fill=tk.BOTH)

Length = tk.Label(root, text="Length", font="arial 20 bold", bg="#004953", fg="white")
Length.place(x=150, y=80)

lengthBox = tk.Entry(root, font=('calibre', 16, 'normal'))
lengthBox.place(x=260, y=88)

Length = tk.Label(root, text="Complexity", font="arial 20 bold", bg="#004953", fg="white")
Length.place(x=150, y=150)

strongComplexity = tk.Radiobutton(root, text="strong", value=1, variable=choice, font=Font)
strongComplexity.place(x=320, y=130)

mediumComplexity = tk.Radiobutton(root, text="Medium", value=2, variable=choice, font=Font)
mediumComplexity.place(x=320, y=170)

weakComplexity = tk.Radiobutton(root, text="Weak", value=3, variable=choice, font=Font)
weakComplexity.place(x=320, y=210)

generateButton = tk.Button(root, text="Generate",width=8, height=1,font="arial 18 bold", command=generator)
generateButton.place(x=280, y=250)

passwordField = tk.Entry(root, width=20 , bd=2, font=('calibre', 16, 'normal'))
passwordField.place(x=220, y=310)

copyButton = tk.Button(root, text="Copy" ,width=5, font="arial 18 bold" ,command=copy)
copyButton.place(x=300, y=360)

root.mainloop()