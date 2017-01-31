# Wait, left() exists? Oh...

# Imports
from turtle import *
from time import *

setup(400,500) # Set window size # This comment is commenting about the comment about setting the window size in our code order to satisfy the requirment that requires comments on our code using comments.


print("""
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
      """) # Inform user of instructions

tracer(0,0) # Used to remove turtle animation, update() to refresh screen

# Variables
grid = [0,0,0,0,0,0,0,0,0] # Set an array to store the grid inputs
winnerExists = False
playerUp = 1

# Move start to the upper right
penup()
goto(-150,150)
pendown()

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

# Functions to draw text
def playUpDraw():
    right(270)
    forward(50)
    right(90)
    write("Player up: " + str(playerUp), font=("Arial", 24, "bold"))
    right(90)
    forward(50)
    right(270)

def playerWins(winner):
    right(270)
    forward(50)
    right(90)
    write("Player " + str(winner) + " wins.", font=("Arial", 24, "bold"))
    right(90)
    forward(50)
    right(270)

# Functions to draw grid spaces
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


# Moves down a row and to the start
def nextRow():
    penup()
    right(90)
    forward(100)
    right(90)
    forward(300)
    right(180)
    pendown()


# Make sure that the space is not already ocupied
def checkForError(num):
    try:
        if grid[int(num)-1] == 0:
            return False
        return True
    except ValueError: # Checks for if the user inputs a string
        return False
 
    
#Check for every possible win
def detectWin():
    if grid[0] == 1 and grid[1] == 1 and grid[2] == 1:
        win(1)
        playerWins(1)
    if grid[3] == 1 and grid[4] == 1 and grid[5] == 1:
        win(1)
        playerWins(1)
    if grid[6] == 1 and grid[7] == 1 and grid[8] == 1:
        win(1)
        playerWins(1)
    if grid[0] == 1 and grid[3] == 1 and grid[6] == 1:
        win(1)
        playerWins(1)
    if grid[1] == 1 and grid[4] == 1 and grid[7] == 1:
        win(1)
        playerWins(1)
    if grid[2] == 1 and grid[5] == 1 and grid[8] == 1:
        win(1)
        playerWins(1)
    if grid[0] == 1 and grid[4] == 1 and grid[8] == 1:
        win(1)
        playerWins(1)
    if grid[2] == 1 and grid[4] == 1 and grid[6] == 1:
        win(1)
        playerWins(1)
        

    if grid[0] == 2 and grid[1] == 2 and grid[2] == 2:
        win(2)
        playerWins(2)
    if grid[3] == 2 and grid[4] == 2 and grid[5] == 2:
        win(2)
        playerWins(2)
    if grid[6] == 2 and grid[7] == 2 and grid[8] == 2:
        win(2)
        playerWins(2)
    if grid[0] == 2 and grid[3] == 2 and grid[6] == 2:
        win(2)
        playerWins(2)
    if grid[1] == 2 and grid[4] == 2 and grid[7] == 2:
        win(2)
        playerWins(2)
    if grid[2] == 2 and grid[5] == 2 and grid[8] == 2:
        win(2)
        playerWins(2)
    if grid[0] == 2 and grid[4] == 2 and grid[8] == 2:
        win(2)
        playerWins(2)
    if grid[2] == 2 and grid[4] == 2 and grid[6] == 2:
        win(2)
        playerWins(2)


#Fluff
def win(winner):
    global winnerExists
    winnerExists = True
    grid = ['']
    
# This is the master function to update the screen, called at the end of each turn
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
    for i in grid[0:3]:
        if i == 0:
            drawNothing()
        if i == 1:
            drawX()
        if i == 2:
            drawO()
    nextRow()
    for i in grid[3:6]:
        if i == 0:
            drawNothing()
        if i == 1:
            drawX()
        if i == 2:
            drawO()
    nextRow()
    for i in grid[6:9]:
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
    global playerUp
    playUpDraw()
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
            gridInput = None
    while not 9 >= int(gridInput) >= 1:
        try:
            gridInput = input("Not a valid input, try another.")
        except ValueError:
            print("Enter a number please")
            gridInput = None
    while checkForError(gridInput):
        gridInput = input("Already filled, try another.")

    grid[gridInput-1] = playerUp
    

def turn():
    global winnerExists
    askInput()
    global playerUp
    if playerUp == 1:
        playerUp = 2
    else:
        playerUp = 1
    detectWin()
    if winnerExists == False:
        screenUpdate()
        turn()

turn()

