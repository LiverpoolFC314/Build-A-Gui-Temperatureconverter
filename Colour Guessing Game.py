from tkinter import*
import random
from tkinter import messagebox
guiscreen=Tk()
guiscreen.geometry("400x400")
guiscreen.config(background="gray57")
guiscreen.title("Colour Guessing Game")
colours=("Red","Yellow","Blue","Green","White","Black",)
c=random.choice(colours)
def greet():
    name=Entrybox.get()
    messagebox.showinfo("Hi",f"Hi {name} Guess a Colour using these options Red,Yellow,Blue,White,Green and Black")
def check_colur():
    user_options=Entrybox2.get()
    global c
    name=Entrybox.get()
    if c==user_options:
        messagebox.showinfo("You Won",f"Hi {name} Congratulations you have won the game")
    elif c !=user_options:
        messagebox.showinfo("You Lose",f"Hi {name} You Lose but better luck next time")
   


title1=Label(text="Colour Guessing Game",bg="gray57", font=("Arial",25,"italic"))
title1.place(x=200,y=100)
title2=Label(text="What's Your Name",bg="gray57",font=("Arial",25,"italic"))
title2.place(x=100,y=200)
Entrybox=Entry()
Entrybox.place(x=150,y=250)
title3=Label(text="Have a guess",bg="gray57",font=("Arial",25,"italic"))
title3.place(x=100,y=300)
Entrybox2=Entry()
Entrybox2.place(x=150,y=350)
B1=Button(text="Ok",command=greet)
B1.place(x=300,y=250,)
B2=Button(text="Guess",command=check_colur)
B2.place(x=300,y=350)
guiscreen.mainloop()
