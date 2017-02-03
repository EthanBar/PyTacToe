#!/usr/bin/python
# Wait, left() exists? Oh...

# Imports
from turtle import *
from time import *
from random import randint
hideturtle()
setup(400,500) # Set window size # This comment is commenting about the comment about setting the window size in our code order to satisfy the requirment that requires comments on our code using comments.
startInput = ''
cpuPlaying = input("1 or 2 players?")
if cpuPlaying.lower() == "1":
    cpuPlaying = True
else:
    cpuPlaying = False
print(cpuPlaying)
while startInput.lower() != "no" and startInput.lower() != "n":
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
        penup()
        right(270)
        forward(50)
        right(90)
        write("Player up: " + str(playerUp), font=("Arial", 24, "bold"))
        right(90)
        forward(50)
        right(270)

    def drawCat():
        right(270)
        forward(50)
        right(90)
        write("It's a tie. You both feel depressed and reconsider your life.", font=("Arial", 24, "bold"))
        penup()
        right(270)
        forward(50)
        right(90)
        write("Cat's Game", font=("Arial", 24, "bold"))
        right(90)
        forward(50)
        right(270)
        update()

    def playerWins(winner):
        if winnerExists == True:
            screenUpdate()
            penup()
            right(270)
            forward(50)
            right(90)
            write("Player " + str(winner) + " wins.", font=("Arial", 24, "bold"))
            right(90)
            forward(50)
            right(270)
            update()
            print(str(winner) + " wins!")

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
        except TypeError:
            return False


    #Check for every possible win
    def detectWin(tempGrid):
        if tempGrid[0] == 1 and tempGrid[1] == 1 and tempGrid[2] == 1:
            return 1
        if tempGrid[3] == 1 and tempGrid[4] == 1 and tempGrid[5] == 1:
            return 1
        if tempGrid[6] == 1 and tempGrid[7] == 1 and tempGrid[8] == 1:
            return 1
        if tempGrid[0] == 1 and tempGrid[3] == 1 and tempGrid[6] == 1:
            return 1
        if tempGrid[1] == 1 and tempGrid[4] == 1 and tempGrid[7] == 1:
            return 1
        if tempGrid[2] == 1 and tempGrid[5] == 1 and tempGrid[8] == 1:
            return 1
        if tempGrid[0] == 1 and tempGrid[4] == 1 and tempGrid[8] == 1:
            return 1
        if tempGrid[2] == 1 and tempGrid[4] == 1 and tempGrid[6] == 1:
            return 1

        # Player 2 or CPU
        if tempGrid[0] == 2 and tempGrid[1] == 2 and tempGrid[2] == 2:
            return 2
        if tempGrid[3] == 2 and tempGrid[4] == 2 and tempGrid[5] == 2:
            return 2
        if tempGrid[6] == 2 and tempGrid[7] == 2 and tempGrid[8] == 2:
            return 2
        if tempGrid[0] == 2 and tempGrid[3] == 2 and tempGrid[6] == 2:
            return 2
        if tempGrid[1] == 2 and tempGrid[4] == 2 and tempGrid[7] == 2:
            return 2
        if tempGrid[2] == 2 and tempGrid[5] == 2 and tempGrid[8] == 2:
            return 2
        if tempGrid[0] == 2 and tempGrid[4] == 2 and tempGrid[8] == 2:
            return 2
        if tempGrid[2] == 2 and tempGrid[4] == 2 and tempGrid[6] == 2:
            return 2

        return 0

    def gridCopy(gridToCopy):
        copyGrid = []
        for i in gridToCopy:
            copyGrid.append(i)
        return copyGrid


    def cpuWinCheck():
        for i in range(0,9):
            copy = gridCopy(grid)
            if copy[i] == 0:
                copy[i] = 1
                if detectWin(copy) == 1:
                    return i
        return False

    def playerWinCheck():
        for i in range(0,9):
            copy = gridCopy(grid)
            if copy[i] == 0:
                copy[i] = 2
                if detectWin(copy) == 2:
                    return i
        return False




    # TODO - Combine with playerWins()
    def win(winner):
        global winnerExists
        if winner != 0:
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

    def CPU():
        print("cpu up")
        canWin = cpuWinCheck()
        if canWin != False:
            grid[canWin] = 1
            print("can win")
        else:
            canBlock = playerWinCheck()
            if canBlock != False:
                grid[canBlock] = 1
                print("can block")
            else:
                while True:
                    randomNum = randint(1,9)
                    if not checkForError(randomNum):
                        grid[randomNum-1] = 1
                        print("randoming and got: " + str(randomNum))
                        break
        print("cpu end")


    def cat():
        global winnerExists
        global grid
        if 0 not in grid and winnerExists == False:
            print("Cat's game!")
            winnerExists == True
            drawCat()
            grid = ['']
            return True
        return False



    def askInput():
        global playerUp # Make this variable global to apply across all functions
        if not (playerUp == 1 and cpuPlaying == True): # Check to see if CPU is playing
            playUpDraw() # Draw which player is up in text
            if playerUp == 1:
                print("Player 1 Up. Choose number between 1 and 9")
            else:
                print("Player 2 Up. Choose number between 1 and 9")
            integer = False
            while not integer: # Tests to see if input is a number
                try:
                    gridInput = int(input())
                    integer = True
                except ValueError: # Except stops the program from crashing when enocuntering an error
                    print("Enter a number please.")
                    gridInput = None
            while not 9 >= int(gridInput) >= 1: # Tests to see if input is in range
                try:
                    gridInput = int(input("Enter a number between 1 and 9, try another."))
                except ValueError:
                    print("Enter a number please")
                    gridInput = None
            while checkForError(gridInput): # Tests to see if input is already filled
                gridInput = input("Already filled, try another.")
                integer = False
                while not integer:
                    try:
                        gridInput = int(gridInput)
                        integer = True
                    except ValueError:
                        print("Enter a number please.")
                        gridInput = None

            grid[int(gridInput)-1] = playerUp # This should be an int that is in range and not already filled, so it is safe to write
        else:
            CPU()
            print("cpu is playing you boi")

    def turn():
        global winnerExists
        global playerUp
        if cat():
            return
        askInput()
        if playerUp == 1:
            playerUp = 2
        else:
            playerUp = 1
        winner = detectWin(grid)
        win(winner)
        playerWins(winner)
        cat()
        if winnerExists == False:
            screenUpdate()
            turn()
        else:
            return

    turn()
    update()
    restartInput=input ("Do you want to play again?") #This restarts the program.
    clear()
