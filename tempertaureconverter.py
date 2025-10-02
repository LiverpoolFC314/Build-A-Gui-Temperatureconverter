from tkinter import *
import tempertaureconverter
guiscreen=Tk()
guiscreen.title("temperatureconverter")
guiscreen.geometry("600x600")
guiscreen.config(background="ghost white")
title = Label(guiscreen,text="temperature converter",bg="gray89",fg="black",font=("Arial",25,"italic",))
title.place(x=200,y=100)
title2 = Label(guiscreen,text="Enter Temperature in celsius",bg="gray89",fg="black",font=("Arial",25,"italic"))
title2.place(x=100,y=200)
temperatureconverter = Entry()
temperatureconverter.place(x=600,y=200)
title3 = Label(guiscreen,text="Temperature in farenheit",bg="green2",fg="black",font=("Arial",25,"italic"))
title3.place(x=100,y=300)
convert=Button(guiscreen,text="Convert" )
convert.place(x=100,y=400)
guiscreen.mainloop()


             