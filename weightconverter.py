from tkinter import* 
import weightconverter
guiscreen=Tk()
guiscreen.title("Weightconverter")
guiscreen.geometry("600x600")
guiscreen.config(background="gray57")
def converter():
  g=Weightconverter.get()
  g=float(g)
  kg=(g/1000)  
  title3.config(text=f"Weight in kilograms:{kg}")
title = Label(guiscreen,text="Grams to kg converter",fg="gray6",bg="gray57",font=("Arial",45,"italic"))
title.place(x=300,y=100)
title2 = Label(guiscreen,text="Enter Weight in grams",fg="gray6",bg="gray88",font=("Arial",45,"italic"))
Weightconverter = Entry()
Weightconverter.place(x=900,y=300)
title2.place(x=300,y=250)
title3= Label(guiscreen,text="Weight in kilograms",fg="gray6",bg="gray88",font=("Arial",45,"italic"))
title3.place(x=300,y=450)

convert=Button(guiscreen,text="Convert",command=converter)
convert.place(x=300,y=350)
guiscreen.mainloop()
