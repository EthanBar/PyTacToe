from turtle import *
from time import *

setup(400,400)

# Wait, left() exists? Oh...

tracer(0,0) # Used to remove turtle animation, update() to refresh screen

# Grid variables
column1 = [0,0,0]
column2 = [0,0,0]
column3 = [0,0,0]

winnerExists = False
playerUp = 1

# Move start to the upper right
penup()
right(180)
forward(150)
right(90)
forward(150)
right(90)

# Draw inital grid lines
penup()
forward(100)
right(90)
pendown()
forward(300)
penup()
right(270)
forward(100)
right(270)
pendown()
forward(300)
penup()
right(90)
forward(100)
right(90)
forward(100)
right(90)
pendown()
forward(300)
penup()
right(270)
forward(100)
right(270)
pendown()
forward(300)
penup()
right(270)
forward(200)
right(270)
forward(300)
right(180)
update()

# Get input and calculate CPU


# Functions to draw grids
def drawNothing():
    penup()
    forward(100)
    pendown()

def drawX():
    right(45)
    penup()
    forward(10)
    pendown()
    forward(121.42)
    penup()
    forward(10)
    right(135)
    forward(100)
    right(135)
    forward(10)
    pendown()
    forward(121.42)
    penup()
    forward(10)
    right(45)

def drawO():
    penup()
    right(90)
    forward(100)
    right(270)
    forward(50)
    right(270)
    forward(5)
    right(90)
    pendown()
    circle(45)
    penup()
    right(90)
    forward(5)
    right(270)
    forward(50)
    right(270)
    forward(100)
    right(90)
    pendown()



def nextRow():
    penup()
    right(90)
    forward(100)
    right(90)
    forward(300)
    right(180)
    pendown()

def checkForError(num):
    if 3 >= num >= 1:
        if num == 1:
            if column1[0] == 0:
                return False
        if num == 2:
            if column1[1] == 0:
                return False
        if num == 3:
            if column1[2] == 0:
                return False
    if 6 >= num >= 4:
        if num == 4:
            if column2[0] == 0:
                return False
        if num == 5:
            if column2[1] == 0:
                return False
        if num == 6:
            if column2[2] == 0:
                return False
    if 9 >= num >= 7:
        if num == 7:
            if column3[0] == 0:
                return False
        if num == 8:
            if column3[1] == 0:
                return False
        if num == 9:
            if column3[2] == 0:
                return False
    return True
 
    

def detectWin():
    if column1 == [1,1,1]:
        win(1)
    if column2 == [1,1,1]:
        win(1)
    if column3 == [1,1,1]:
        win(1)
    if column1[0] == 1 and column2[0] == 1 and column3[0] == 1:
        win(1)
    if column1[1] == 1 and column2[1] == 1 and column3[1] == 1:
        win(1)
    if column1[2] == 1 and column2[2] == 1 and column3[2] == 1:
        win(1)
    if column1[0] == 1 and column2[1] == 1 and column3[2] == 1:
        win(1)
    if column1[2] == 1 and column2[1] == 1 and column3[0] == 1:
        win(1)

    if column1 == [2,2,2]:
        win(2)
    if column2 == [2,2,2]:
        win(2)
    if column3 == [2,2,2]:
        win(2)
    if column1[0] == 2 and column2[0] == 2 and column3[0] == 2:
        win(2)
    if column1[1] == 2 and column2[1] == 2 and column3[1] == 2:
        win(2)
    if column1[2] == 2 and column2[2] == 2 and column3[2] == 2:
        win(2)
    if column1[0] == 2 and column2[1] == 2 and column3[2] == 2:
        win(2)
    if column1[2] == 2 and column2[1] == 2 and column3[0] == 2:
        win(2)

def win(winner):
    global winnerExists
    if winner == 1:
        print("Player 1 wins!!!!!!")
    elif winner == 2:
        print("Player 2 wins!!!!!!")
    winnerExists = True
    

def screenUpdate():
    clear()
    penup()
    forward(100)
    right(90)
    pendown()
    forward(300)
    penup()
    right(270)
    forward(100)
    right(270)
    pendown()
    forward(300)
    penup()
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    pendown()
    forward(300)
    penup()
    right(270)
    forward(100)
    right(270)
    pendown()
    forward(300)
    penup()
    right(270)
    forward(200)
    right(270)
    forward(300)
    right(180)

    pendown()
    for i in column1:
        if i == 0:
            drawNothing()
        if i == 1:
            drawX()
        if i == 2:
            drawO()
    nextRow()
    for i in column2:
        if i == 0:
            drawNothing()
        if i == 1:
            drawX()
        if i == 2:
            drawO()
    nextRow()
    for i in column3:
        if i == 0:
            drawNothing()
        if i == 1:
            drawX()
        if i == 2:
            drawO()
    penup()
    right(270)
    forward(200)
    right(270)
    forward(300)
    right(180)
    pendown()
    update()

def askInput():
    global column1
    global column2
    global column3
    if playerUp == 1:
        print("Player 1 Up. Choose number between 1 and 9")
    else:
        print("Player 2 Up. Choose number between 1 and 9")
    integer = False
    while not integer:
        try:
            gridInput = int(input())
            integer = True
        except ValueError:
            print("Enter a number please.")
    while not 9 >= int(gridInput) >= 1:
        gridInput = input("Not a valid input, try another.")
    while checkForError(int(gridInput)):
        gridInput = input("Already filled, try another.")
    if 3 >= int(gridInput) >= 1:
        if int(gridInput) == 1:
            if column1[0] == 0:
                if playerUp == 1:
                    column1[0] = 1
                else:
                    column1[0] = 2
        if int(gridInput) == 2:
            if column1[1] == 0:
                if playerUp == 1:
                    column1[1] = 1
                else:
                    column1[1] = 2
        if int(gridInput) == 3:
            if column1[2] == 0:
                if playerUp == 1:
                    column1[2] = 1
                else:
                    column1[2] = 2
    if 6 >= int(gridInput) >= 4:
        if int(gridInput) == 4:
            if column2[0] == 0:
                if playerUp == 1:
                    column2[0] = 1
                else:
                    column2[0] = 2
        if int(gridInput) == 5:
            if column2[1] == 0:
                if playerUp == 1:
                    column2[1] = 1
                else:
                    column2[1] = 2
        if int(gridInput) == 6:
            if column2[2] == 0:
                if playerUp == 1:
                    column2[2] = 1
                else:
                    column2[2] = 2
    if 9 >= int(gridInput) >= 7:
        if int(gridInput) == 7:
            if column3[0] == 0:
                if playerUp == 1:
                    column3[0] = 1
                else:
                    column3[0] = 2
        if int(gridInput) == 8:
            if column3[1] == 0:
                if playerUp == 1:
                    column3[1] = 1
                else:
                    column3[1] = 2
        if int(gridInput) == 9:
            if column3[2] == 0:
                if playerUp == 1:
                    column3[2] = 1
                else:
                    column3[2] = 2
    

def turn():
    global winnerExists
    askInput()
    global playerUp
    if playerUp == 1:
        playerUp = 2
    else:
        playerUp = 1
    detectWin()
    screenUpdate()
    if winnerExists == False:
        turn()

turn()

