import tkinter
from tkinter import *
import string
import random
import pyperclip
def generator():
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    number=string.digits
    special_character=string.punctuation



    all=small_alphabets+capital_alphabets+number+special_character
    password_length=int(length_Box.get())

    if choice.get()==1:
        passwordField.insert(0,random.sample(small_alphabets,password_length))
    if choice.get()==2:
        passwordField.insert(0,random.sample(small_alphabets+capital_alphabets,password_length))
    if choice.get()==3:
        passwordField.insert(0,random.sample(all,password_length))
#password=random.sample(all,password_length)
#passwordField.insert(0,password)
def copy():
    random_password=passwordField.get()
    pyperclip.copy(random_password)
    
root =Tk()
root.title("PASSWORD GENERATOR")
root.geometry("560x550")
choice=IntVar()
Font=("arial",20,"bold")
root.configure(bg="#17161b")
passwordlabel=Label(root,text="PASSWORD GENERATOR",font=("times new roman",15,"bold"),bg="snow")
passwordlabel.pack()
weakradiobutton=Radiobutton(root,text="WEAK",value=1,variable=choice)
weakradiobutton.pack(padx=10,pady=5)

mediumradiobutton=Radiobutton(root,text="medium",value=2,variable=choice)
mediumradiobutton.pack(padx=10,pady=5)

strongradiobutton=Radiobutton(root,text="strong",value=3,variable=choice)
strongradiobutton.pack(padx=10,pady=5)

lengthlabel=Label(root,text="PASSWORD LENGTH",font=("times new roman",15,"bold"),bg="snow")
lengthlabel.pack()

length_Box=Spinbox(root,from_=5,to_=18,width=5,font=Font)
length_Box.pack()

generateButton=Button(root,text="GENERATE",font=Font,command=generator)
generateButton.pack(padx=2,pady=6)

passwordField=Entry(root,width=30,bd=6,font=Font)
passwordField.pack()


copyButton=Button(root,text="COPY",font=Font,command=copy)
copyButton.pack(padx=2,pady=6)


root.mainloop()