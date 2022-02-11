from tkinter import *
from tkinter import ttk
from random import randint

root = Tk()
root.title("Rock Paper Scissors")
root.geometry("500x600")
root.config(bg=("white"))


Upoints = 0
Cpoints = 0


   
def func():
    global Upoints
    global Cpoints


    if (Cpoints >= 5):
            
            blank = Label(root, text="", bg='white',width=20, height=20, fg='white')
            blank.place(x=400, y=500)

            text1 = Label(root, text="YOU LOSE THE GAME", bg='black', fg='red', font=("Courier", 40))
            text1.place(x=40, y=0)


    
    elif (Upoints >= 5):

        blank = Label(root, text="", bg='white',width=20, height=20, fg='white')
        blank.place(x=400, y=500)
        
        text1 = Label(root, text="YOU WIN THE GAME", bg='black', fg='red', font=("Courier", 40))
        text1.place(x=40, y=0)


    x = var.get()
    # print(x)
    text.config(text=x)


    Upoints1 = Label(root, text="Your points:", bg='white', fg='black')
    Upoints1.place(x=20, y=300)

    Your_points = Label(root, text=Upoints, bg='white', fg='black')
    Your_points.place(x=100, y=300)


    Cpoints1 = Label(root, text="Computer points:", bg='white', fg='black')
    Cpoints1.place(x=320, y=300)

    computer_points = Label(root, text=Cpoints, bg='white', fg='black')
    computer_points.place(x=435, y=300)



    computer = (randint(0, 2))
    
    if computer == 0:
     stone = Label(root, text="Stone", bg='white',width=20, fg='black')
     stone.place(x=230, y=70)

    elif computer == 1:
     paper = Label(root, text="Paper", bg='white',width=20, fg='black')
     paper.place(x=230, y=70)

    elif computer == 2:
     Scissor = Label(root, text="Scissor", bg='white',width=20, fg='black')
     Scissor.place(x=230, y=70)



     
    if  computer == 0 and com.get() == "Stone":
        result = Label(root, text="it's tie",width=30, bg='white', fg='black')
        result.place(x=60, y=200)

         
    elif computer == 0 and com.get() == "Paper":
         Upoints+=1
         result1 = Label(root, text="you win paper cover's stone",width=30, bg='white', fg='black')
         result1.place(x=60, y=200)

         Your_points = Label(root, text=Upoints, bg='white', fg='black')
         Your_points.place(x=100, y=300)

         computer_points = Label(root, text=Cpoints, bg='white', fg='black')
         computer_points.place(x=435, y=300)



    elif computer == 0 and com.get() == "Scissor":
         Cpoints+=1
         result2 = Label(root, text="you lose stone break's scissor",width=30, bg='white', fg='black')
         result2.place(x=60, y=200)

         Your_points = Label(root, text=Upoints, bg='white', fg='black')
         Your_points.place(x=100, y=300)

         computer_points = Label(root, text=Cpoints, bg='white', fg='black')
         computer_points.place(x=435, y=300)


    if computer == 1 and com.get() == "Stone":
        Cpoints+=1
        result3 = Label(root, text="you lose paper cover's stone",width=30, bg='white', fg='black')
        result3.place(x=60, y=200)

        Your_points = Label(root, text=Upoints, bg='white', fg='black')
        Your_points.place(x=100, y=300)

        computer_points = Label(root, text=Cpoints, bg='white', fg='black')
        computer_points.place(x=435, y=300)

    
    elif computer == 1 and com.get() == "Paper":
        result = Label(root, text="it's tie",width=30, bg='white', fg='black')
        result.place(x=60, y=200)

    elif computer == 1 and com.get() == "Scissor":
         Upoints+=1
         result4 = Label(root, text="you win scissor cut's paper",width=30, bg='white', fg='black')
         result4.place(x=60, y=200)

         Your_points = Label(root, text=Upoints, bg='white', fg='black')
         Your_points.place(x=100, y=300)

         computer_points = Label(root, text=Cpoints, bg='white', fg='black')
         computer_points.place(x=435, y=300)

    
    if computer == 2 and com.get() == "Stone":
        Upoints+=1
        result5 = Label(root, text="you win stone break's scissor",width=30, bg='white', fg='black')
        result5.place(x=60, y=200)

        Your_points = Label(root, text=Upoints, bg='white', fg='black')
        Your_points.place(x=100, y=300)

        computer_points = Label(root, text=Cpoints, bg='white', fg='black')
        computer_points.place(x=435, y=300)
    
    elif computer == 2 and com.get() == "Paper":
        Cpoints+=1
        result6 = Label(root, text="you lose scissor cut's paper",width=30, bg='white', fg='black')
        result6.place(x=60, y=200)

        Your_points = Label(root, text=Upoints, bg='white', fg='black')
        Your_points.place(x=100, y=300)

        computer_points = Label(root, text=Cpoints, bg='white', fg='black')
        computer_points.place(x=435, y=300)

    elif computer == 2 and com.get() == "Scissor":
        result = Label(root, text="it's tie",width=30, bg='white', fg='black')
        result.place(x=60, y=200)

         



text = Label(root, text="", bg='white', fg='black')
text.place(x=20, y=70)



user = Label(root, text="You", bg='white', fg='black')
user.place(x=20, y=50)

Computer = Label(root, text="Computer", bg='white', fg='black')
Computer.place(x=300, y=50)


btn = Button(root, text="enter", fg=('white'), command=func)
btn.place(x=400, y=500)


var = StringVar()
com = ttk.Combobox(root, width=20, textvariable=var, value=("Stone", "Paper", "Scissor"))
com["state"] = 'readonly'

com.pack()
com.current(0)

copyright = Label(root, text="Copyright 2021 Samyak jain. All rights reserved.", bg='black', fg='white')
copyright.place(x=72, y=560)

root.mainloop()
