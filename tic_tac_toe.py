import tkinter.messagebox
from tkinter import *

root = Tk()
root.geometry("1350x750+0+0")
root.title("Tic Tac Toe")
root.configure(background="Cadet Blue")
    
tops = Frame(root, bg = "Cadet Blue", pady = 2, width = 1350, height = 100, relief = RIDGE)
tops.grid(row = 0, column=0)

lblTitle = Label(tops, font=('calibri',50,'bold'), text="Tic Tac Toe", bd=21, bg="Cadet Blue", fg="Cornsilk", justify=CENTER)
lblTitle.grid(row=0, column=0)

# mainFrame for whole application
mainFrame = Frame(root, bg = "Powder Blue", bd=10, width = 1350, height = 600, relief = RIDGE)
mainFrame.grid(row = 1, column=0)

# leftFrame for grid
leftFrame = Frame(mainFrame, bd=10, width = 750, height = 500, pady = 2, padx = 10, bg="Cadet Blue", relief=RIDGE)
leftFrame.pack(side=LEFT)

# right frame for kepping score
rightFrame = Frame(mainFrame, bd=10, width = 560, height = 500, pady = 2, padx = 10, bg="Cadet Blue", relief=RIDGE)
rightFrame.pack(side=RIGHT)

# rightframe for player names and score
rightFrame1 = Frame(rightFrame, bd=10, width = 560, height = 200, pady = 2, padx = 10, bg="Cadet Blue", relief=RIDGE)
rightFrame1.grid(row=0, column=0)

# rightframe for new game and reset button
rightFrame2 = Frame(rightFrame, bd=10, width = 560, height = 200, pady = 2, padx = 10, bg="Cadet Blue", relief=RIDGE)
rightFrame2.grid(row=1, column=0)

# variables for kepping score
PlayerX = IntVar()
PlayerO = IntVar()

PlayerX.set(0)
PlayerO.set(0)

btns = StringVar()
click = True

#for checking status of button in X's and O's
def checker(btns):
    global click
    if btns["text"] == " " and click == True:
        btns["text"] = "X"
        click = False
        scoreKepper()

    elif btns["text"] == " " and click == False:
        btns["text"] = "O"
        click = True
        scoreKepper()

# for checking the score of the player
def scoreKepper():

# Player X is the winner

    if button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X":
        button1.configure(background="Green")
        button2.configure(background="Green")
        button3.configure(background="Green")
        n = int(PlayerX.get())
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You have won the game")
        reset()

    if button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X":
        button4.configure(background="Green")
        button5.configure(background="Green")
        button6.configure(background="Green")
        n = int(PlayerX.get())
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You have won the game")
        reset()

    if button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X":
        button7.configure(background="Green")
        button8.configure(background="Green")
        button9.configure(background="Green")
        n = int(PlayerX.get())
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You have won the game")
        reset()
    
    if button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X":
        button1.configure(background="Green")
        button5.configure(background="Green")
        button9.configure(background="Green")
        n = int(PlayerX.get())
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You have won the game")
        reset()

    if button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X":
        button3.configure(background="Green")
        button5.configure(background="Green")
        button7.configure(background="Green")
        n = int(PlayerX.get())
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You have won the game")
        reset()

    if button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X":
        button1.configure(background="Green")
        button4.configure(background="Green")
        button7.configure(background="Green")
        n = int(PlayerX.get())
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You have won the game")
        reset()

    if button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X":
        button2.configure(background="Green")
        button5.configure(background="Green")
        button8.configure(background="Green")
        n = int(PlayerX.get())
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You have won the game")
        reset()

    if button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X":
        button3.configure(background="Green")
        button6.configure(background="Green")
        button9.configure(background="Green")
        n = int(PlayerX.get())
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You have won the game")
        reset()

# Player O is the winner

    if button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O":
        button1.configure(background="Blue")
        button2.configure(background="Blue")
        button3.configure(background="Blue")
        n = int(PlayerO.get())
        score = n+1
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "You have won the game")
        reset()

    if button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O":
        button4.configure(background="Blue")
        button5.configure(background="Blue")
        button6.configure(background="Blue")
        n = int(PlayerO.get())
        score = n+1
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "You have won the game")
        reset()

    if button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O":
        button7.configure(background="Blue")
        button8.configure(background="Blue")
        button9.configure(background="Blue")
        n = int(PlayerO.get())
        score = n+1
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "You have won the game")
        reset()
    
    if button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O":
        button1.configure(background="Blue")
        button5.configure(background="Blue")
        button9.configure(background="Blue")
        n = int(PlayerO.get())
        score = n+1
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "You have won the game")
        reset()

    if button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O":
        button3.configure(background="Blue")
        button5.configure(background="Blue")
        button7.configure(background="Blue")
        n = int(PlayerO.get())
        score = n+1
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "You have won the game")
        reset()

    if button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O":
        button1.configure(background="Blue")
        button4.configure(background="Blue")
        button7.configure(background="Blue")
        n = int(PlayerO.get())
        score = n+1
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "You have won the game")
        reset()

    if button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O":
        button2.configure(background="Blue")
        button5.configure(background="Blue")
        button8.configure(background="Blue")
        n = int(PlayerO.get())
        score = n+1
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "You have won the game")
        reset()

    if button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O":
        button3.configure(background="Blue")
        button6.configure(background="Blue")
        button9.configure(background="Blue")
        n = int(PlayerO.get())
        score = n+1
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "You have won the game")
        reset()

# for resetting the grid
def reset():
    button1['text'] = " "
    button2['text'] = " "
    button3['text'] = " "
    button4['text'] = " "
    button5['text'] = " "
    button6['text'] = " "
    button7['text'] = " "
    button8['text'] = " "
    button9['text'] = " "

    button1.configure(background="gainsboro")
    button2.configure(background="gainsboro")
    button3.configure(background="gainsboro")
    button4.configure(background="gainsboro")
    button5.configure(background="gainsboro")
    button6.configure(background="gainsboro")
    button7.configure(background="gainsboro")
    button8.configure(background="gainsboro")
    button9.configure(background="gainsboro")

# for starting new game
def newGame():
    reset()
    PlayerX.set(0)
    PlayerO.set(0)

# PLayer x
lblPlayerX = Label(rightFrame1, font=('calibri',40,'bold'), text="Player X:", padx=2, pady=2, bg="Cadet Blue", fg="Cornsilk")
lblPlayerX.grid(row=0, column=0, sticky=W)

txtPlayerX = Label(rightFrame1, font=('calibri',40,'bold'), textvariable = PlayerX, padx=4, pady=2, bg="Cadet Blue", fg="Cornsilk")
txtPlayerX.grid(row=0, column=1, sticky=W)

# Player O
lblPlayerO = Label(rightFrame1, font=('calibri',40,'bold'), text="Player O:", padx=2, pady=2, bg="Cadet Blue", fg="Cornsilk")
lblPlayerO.grid(row=1, column=0, sticky=W)

txtPlayerO = Label(rightFrame1, font=('calibri',40,'bold'), textvariable = PlayerO, padx=4, pady=2, bg="Cadet Blue", fg="Cornsilk")
txtPlayerO.grid(row=1, column=1, sticky=W)

#Start and Reset Button

btnReset = Button(rightFrame2, text="Reset", font=("calibri", 26 ,"bold"), height = 3, width = 40, command= reset)
btnReset.grid(row=2, column=0, padx=6, pady=11)

btnStart = Button(rightFrame2, text="New Game", font=("calibri", 26 ,"bold"), height = 3, width = 40, command= newGame)
btnStart.grid(row=3, column=0, padx=6, pady=10)

# X's and O's Grid

button1 = Button(leftFrame, text=" ", font=("calibri 26 bold"), height = 3, width = 8, bg = "gainsboro", command=lambda:checker(button1))
button1.grid(row=1, column=0, sticky=S+N+E+W)

button2 = Button(leftFrame, text=" ", font=("calibri 26 bold"), height = 3, width = 8, bg = "gainsboro", command=lambda:checker(button2))
button2.grid(row=1, column=1, sticky=S+N+E+W)

button3 = Button(leftFrame, text=" ", font=("calibri 26 bold"), height = 3, width = 8, bg = "gainsboro", command=lambda:checker(button3))
button3.grid(row=1, column=2, sticky=S+N+E+W)

button4 = Button(leftFrame, text=" ", font=("calibri 26 bold"), height = 3, width = 8, bg = "gainsboro", command=lambda:checker(button4))
button4.grid(row=2, column=0, sticky=S+N+E+W)

button5 = Button(leftFrame, text=" ", font=("calibri 26 bold"), height = 3, width = 8, bg = "gainsboro", command=lambda:checker(button5))
button5.grid(row=2, column=1, sticky=S+N+E+W)

button6 = Button(leftFrame, text=" ", font=("calibri 26 bold"), height = 3, width = 8, bg = "gainsboro", command=lambda:checker(button6))
button6.grid(row=2, column=2, sticky=S+N+E+W)

button7 = Button(leftFrame, text=" ", font=("calibri 26 bold"), height = 3, width = 8, bg = "gainsboro", command=lambda:checker(button7))
button7.grid(row=3, column=0, sticky=S+N+E+W)

button8 = Button(leftFrame, text=" ", font=("calibri 26 bold"), height = 3, width = 8, bg = "gainsboro", command=lambda:checker(button8))
button8.grid(row=3, column=1, sticky=S+N+E+W)

button9 = Button(leftFrame, text=" ", font=("calibri 26 bold"), height = 3, width = 8, bg = "gainsboro", command=lambda:checker(button9))
button9.grid(row=3, column=2, sticky=S+N+E+W)

# main loop
root.mainloop()