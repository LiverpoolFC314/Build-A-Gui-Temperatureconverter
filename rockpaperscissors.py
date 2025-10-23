from tkinter import*
import random
guiscreen=Tk()
guiscreen.config(background="gray57")
guiscreen.geometry("800x800")
guiscreen.title("Rock Paper Scissors")
title=Label(text="Rock Paper Scissors",fg="gray2",bg="gray57",font=("Arial",25,"italic"))
player_score=0
computer_score=0
options=["Rock","Paper","Scissors"]
def game(user):
    global player_score,computer_score
    user_options=user
    computer_options= random.choice(options)
    title5.config(text=f"You Selected:{user_options}")
    title6.config(text=f"Computer Selected:{computer_options}")
    if user_options ==computer_options:
        title2.config(text=f"It a Draw Congrats to both sides!")
    elif user_options=="Rock" and computer_options=="Paper":

        title2.config(text=f"Computer Won!")
        computer_score+=1
    elif user_options=="Rock" and computer_options=="Scissors":
        title2.config(text=f"Player Won!")
        player_score+=1
    elif user_options=="Paper" and computer_options=="Rock":
        title2.config(text=f"Player Won!")
        player_score+=1
    elif user_options=="Scissors" and computer_options=="Rock":
        title2.config(text=f"Computer Won!")
        computer_score+=1
    elif user_options=="Paper" and computer_options=="Scissors":
         title2.config(text=f"Computer Won!")
         computer_score+=1
    elif user_options=="Scissors" and computer_options=="Paper":
        title2.config(text=f"Player Won!")
        player_score+=1
    title7.config(text=f"Player Score:{player_score}")
    title8.config(text=f"Computer Score {computer_score}")  
        
title.place(x=300,y=50)
title2=Label(text="Press Button to start",fg="gray2",bg="gray57",font=("Arial",25,"italic"))
title2.place(x=300,y=100)
title3=Label(text="Your Options:",fg="gray2",bg="gray57",font=("Arial",25,"italic"))
title3.place(x=150,y=200)
title4=Label(text="Score:",fg="gray2",bg="gray57",font=("Arial",25,"italic"))
title4.place(x=150,y=300)
B1=Button(guiscreen,text="Rock",command=lambda:game("Rock"))

B2=Button(guiscreen,text="Paper", command=lambda:game("Paper"))
B3=Button(guiscreen,text="Scissors",command=lambda:game("Scissors"))
B1.place(x=400,y=200)
B2.place(x=500,y=200)
B3.place(x=600,y=200)
title5=Label(text="You Selected",fg="gray2",bg="gray57",font=("Arial",25,"italic"))
title5.place(x=150,y=400)
title6=Label(text="Computer Selected",fg="gray2",bg="gray57",font=("Arial",25,"italic"))
title6.place(x=150,y=500)
title7=Label(text="Player Score",fg="gray2",bg="gray57",font=("Arial",25,"italic"))
title7.place(x=550,y=400)
title8=Label(text="Computer Score",fg="gray2",bg="gray57",font=("Arial",25,"italic"))
title8.place(x=550,y=500)    
guiscreen.mainloop()
