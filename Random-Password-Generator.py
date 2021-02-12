import random, string
from tkinter import *
import tkinter as tk

import pyperclip

root = Tk()
root.title("Random Password")
root.geometry("300x400")
root.resizable(0, 0)
#
Label(root, text="PLEASE CHOOSE", fg="blue", relief=tk.GROOVE, font=("arial", 18, "bold")).place(x=45, y=0)
Label(root, text="Password Length:").place(x=50, y=60)
pass_len = IntVar()
length = Spinbox(root, from_=8, to_=32, textvariable=pass_len, width=10, borderwidth=2).place(x=165, y=60)
Label(root, text="Password Included:").place(x=50, y=90)
ascii_uppercase = IntVar()
Checkbutton(root, text="ascii_uppercase", variable=ascii_uppercase, onvalue=1, offvalue=0).place(x=160, y=100)
ascii_lowercase = IntVar()
Checkbutton(root, text="ascii_lowercase", variable=ascii_lowercase, onvalue=1, offvalue=0).place(x=160, y=120)
digits = IntVar()
Checkbutton(root, text="digits", variable=digits, onvalue=1, offvalue=0).place(x=160, y=140)
punctuation = IntVar()
Checkbutton(root, text="punctuation", variable=punctuation, onvalue=1, offvalue=0).place(x=160, y=160)

pass_str = StringVar()


def generator():
    password = ''
    included = ""
    if ascii_uppercase.get() == 1:
        password += random.choice(string.ascii_uppercase)
        included += string.ascii_uppercase
    if ascii_lowercase.get() == 1:
        password += random.choice(string.ascii_lowercase)
        included += string.ascii_lowercase
    if digits.get() == 1:
        password += random.choice(string.digits)
        included += string.digits
    if punctuation.get() == 1:
        password += random.choice(string.punctuation)
        included += string.punctuation
    a = len(password)
    if included != "":
        for i in range(pass_len.get() - a):
            password += random.choice(included)
    else:
        password += random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(
            string.digits) + random.choice(string.punctuation)
        for i in range(pass_len.get() - 4):
            password += random.choice(
                string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)


Button(root, text="Generator", command=generator).place(x=160, y=200)
Entry(root, textvariable=pass_str, font=("arial", 10, "bold"), width=35, borderwidth=4, justify=tk.CENTER, bg="#747474",
      fg="#FFFFFF").place(x=25, y=250)


def copy_password():
    pyperclip.copy(pass_str.get())


Button(root, text='COPY TO CLIPBOARD', command=copy_password).place(x=85, y=290)
root.mainloop()
