from tkinter import *
from tkinter import messagebox
guiscreen = Tk()
guiscreen.geometry("600x600")
guiscreen.title("Login Me")
guiscreen.config(background ="gray57")
def submit():
    messagebox.showinfo("Success","Login Succesfully")
#text 
user_name = Label(guiscreen,text = "Username",bg="ghost white",fg="gray7",font =("Arial",45,"italic"))
password_name =Label(guiscreen,text = "Password",bg ="ghost white",fg="gray7",font =("Arial",45,"italic"))
user_entry=Entry(guiscreen)
user_name.place(x= 100,y=100 )
password_name.place(x=100,y=200)
user_entry.place(x=400,y=100)
password_entry=Entry(guiscreen)
password_entry.place(x=400,y=200)
login=Button(guiscreen,text="Log In",bg="green2",font=("Arial",45,"italic"),command=submit)
login.place(x=300,y=300,)
guiscreen.mainloop()