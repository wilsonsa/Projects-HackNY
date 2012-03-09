# events-example0.py
# Barebones timer, mouse, and keyboard events
# as we will use them in Spring 2011's 15-110

# termProject
# SphereRunner

from Tkinter import *
import random

#import tkSnack
#tkSnack.initializeSnack(root)

# File Input/Output in Python

import os

def getDesktopPath(filename = ""):
    # next line is odd, but works in Windows/Mac/Linux
    homepath = os.getenv('USERPROFILE') or os.getenv('HOME')
    return homepath + os.sep + "Desktop" + os.sep + filename

def fileExists(filename):
    return os.path.exists(filename)
    
def deleteFile(filename):
    if (fileExists(filename) == True):
        os.remove(filename)

def readTextFile(filename):
    if (fileExists(filename) == False):
        print "File does not exist:", filename
        return None
    fileHandler = open(filename, "rt")
    text = fileHandler.read()
    fileHandler.close()
    return text

def readTextFileAsList(filename):
    # readlines includes '\n' characters, so we'll use split() instead
    text = readTextFile(filename)
    if (text == None):
        return None
    return text.split("\n")

def writeTextFile(text, filename):
    fileHandler = open(filename, "wt")
    fileHandler.write(text)
    fileHandler.close()

def testFileIO():
    #print "Testing File IO..."
    filename = getDesktopPath("test.txt")
    deleteFile(filename)
    assert(fileExists(filename) == False)
    #print "Reading from a non-existent file (error message expected)..."
    text = readTextFile(filename)
    assert(text == None)
    text = "This is a test.\nIt is only a test."
    writeTextFile(text, filename)
    assert(fileExists(filename) == True)
    text = readTextFile(filename)
    assert(text == "This is a test.\nIt is only a test.")
    textList = readTextFileAsList(filename)
    assert(textList == ["This is a test.", "It is only a test."])
    assert(fileExists(filename) == True)
    #deleteFile(filename)
    #assert(fileExists(filename) == False)
    #print "Passed!"

testFileIO()




def mousePressed(event):
    #not used
    return

def keyPressed(event):
    if (canvas.data.playGame == True): # keys only work if game is on
        if (event.keysym == "r"):
            resetGame()
            playGame()
        elif (event.keysym == "m"):
            menuButtonPressed()
            menu()
        elif (event.keysym == "i"):
            infoButtonPressed()
            info()
        elif (event.keysym == "s"):
            settingsButtonPressed()
            settings()
        elif (event.keysym == "p"):
            canvas.data.running = not canvas.data.running
        elif (event.keysym == " "):
            canvas.data.beforeRedrawMenu = not canvas.data.beforeRedrawMenu
        elif (canvas.data.running == True):
                if event.keysym not in canvas.data.keyPressed:
                    canvas.data.keyPressed += [event.keysym]
        

def keyReleased(event):
    #removes key from list when released
    if event.keysym in canvas.data.keyPressed:
        canvas.data.keyPressed.remove(event.keysym)
    
                


def continuousPress():
    #continuous pressed allows you to hold down a key and not have lag
    #it adds the key to a list when it is pressed and then removes
    #it when you realease
    
    canvas.data.slow = False 
    canvas.data.fast = False
    if (canvas.data.playGame == True):
        for i in canvas.data.keyPressed:
            if (i == "Left"):
                canvas.data.leftEdge -= 1
                canvas.data.shift -= 1
                
            elif (i == "Right"):
                canvas.data.leftEdge += 1
                canvas.data.shift += 1
    
            elif (i == "Down"):
                if (canvas.data.boost >0):
                    canvas.data.boost -=5
                    canvas.data.slow = True
            elif (i == "Up"):
                if (canvas.data.boost < 100):
                    canvas.data.boost +=5
                    canvas.data.fast = True
    return
    
    

def timerFired():
    delay = 150 # milliseconds
    canvas.data.timerCounter += 1 ################

    #acounts for what speed setting you have selected (default is Medium)
    speedLevelChange = delay/3
    if(canvas.data.speed == "Slow"):
        delay += speedLevelChange
    elif (canvas.data.speed == "Fast"):
        delay -= speedLevelChange

    #Makes game speed up as the game goes on
    maxTimerFiredReductionByCounter = 20
    if(canvas.data.timerCounter/50 < maxTimerFiredReductionByCounter):
        delay -= canvas.data.timerCounter/50

    #calls the continuously held keys
    continuousPress()
        
    #accounts for if front or back arrows are pressed
    delayPercent = delay/3
    if(canvas.data.slow == True):
        delay += delayPercent
    elif(canvas.data.fast == True):
        delay -= delayPercent
    
    #if(canvas.data.beforeRedrawMenu and canvas.data.gameOver):
    #    menuButtonPressed()
    #else:
   
    canvas.after(delay, timerFired) # pause, then call timerFired again
    redrawAll()



def drawBackBoard():
    #draws the clouds on top of screen and dark blue on bottom
    canvas.create_rectangle(0,0, canvas.data.canvasWidth,
                            canvas.data.canvasHeight/2,
                            fill = "lightblue", width=0)
    canvas.create_rectangle(0, canvas.data.canvasHeight/2,
                            canvas.data.canvasWidth,canvas.data.canvasHeight,
                            fill = "darkblue", width=0)

    #cloud image
    canvas.create_image(0,0, image = canvas.data.cloudPicture, anchor = NW)





##################################################### 
################# menu stuff begin ##################
#####################################################

def menu():
    #this id the page the game will originally open in
    #it allows you to navigate
    drawBackBoard()
    score() #draw score
    maxScoreEver() #draw maxScoreEver
    if(canvas.data.lastGamesScore > 0):
        printingCrashedBox()
    printingMenuPagesButtons()
    
    canvas.create_text(canvas.data.canvasWidth/2,
                       canvas.data.canvasHeight/4,
                       text="SphereRunner", fill="red",
                       font="Helvetica 60 bold underline") 
    

def printingCrashedBox():
    #this will be called on the menu page if you crashed
    boxHeight = 41
    borderWidth = 6
    borderBoxShift = borderWidth/2
    canvas.create_rectangle(canvas.data.canvasWidth/6,
            (canvas.data.canvasHeight/2) - boxHeight - borderBoxShift,
            canvas.data.canvasWidth*5/6,
            (canvas.data.canvasHeight/2) - borderBoxShift,
            fill = "red", width = borderWidth)
    
    canvas.create_text(canvas.data.canvasWidth/2,
                   (canvas.data.canvasHeight/2) - borderBoxShift,
                   text="!!!YOU CRASHED!!!", fill="yellow",anchor = S,
                   font="Helvetica 35 bold")

def printingMenuPagesButtons():
    playGameButton = canvas.data.playGameButton ##printing Play Game Button
    canvas.create_window(canvas.data.canvasWidth/2,
                    canvas.data.canvasHeight - canvas.data.canvasHeight/6,
                    window=playGameButton)
    infoButton = canvas.data.infoButton ##printing info button
    canvas.create_window(canvas.data.canvasWidth/4,
                    canvas.data.canvasHeight - canvas.data.canvasHeight/3,
                    window=infoButton)
    settingsButton = canvas.data.settingsButton #printing settings button
    canvas.create_window(canvas.data.canvasWidth*3/4,
                    canvas.data.canvasHeight - canvas.data.canvasHeight/3,
                    window=settingsButton)


def menuButtonPressed():
    canvas.data.playGame = False
    canvas.data.running = False
    canvas.data.menu = True
    canvas.data.info = False
    canvas.data.settings = False
    
####################################################
################# menu stuff end ###################
####################################################





####################################################
################# info stuff begin #################
####################################################


def info():
    #this page gives you various information about the game
    drawBackBoard()
    printingSphereRunnerInformation()
    printingPlayGameAndMenuButton()
    
    #creates the text of info on the page
    canvas.create_text(canvas.data.canvasWidth/4, canvas.data.canvasHeight/2,
        text = "\nkey p = pause\nkey m = menu\nkey i = info\nkey s = settings",
                       anchor = N, fill = "yellow", font = "Helvetica 23 bold")
    t1 = "\narrow right = move right\narrow left = move left\narrow down"
    t2 = " = slow down\narrow up = speed up"
    printText = t1+t2
    canvas.create_text(canvas.data.canvasWidth*3/4, canvas.data.canvasHeight/2,
        text = printText,anchor = N,
        fill = "orange", font = "Helvetica 23 bold")

    printingBoostInfoButton()
    printingHitGreenSpheresButton()
    printingInstructionsButton()
    

def boostInfoButtonPressed():
    canvas.data.boostInfoButtonPressed = not canvas.data.boostInfoButtonPressed
    canvas.data.hitGreenSpheresButtonPressed = False
    canvas.data.instructionsButtonPressed = False

def hitGreenSpheresButtonPressed():
    a = canvas.data.hitGreenSpheresButtonPressed
    a = not a
    canvas.data.hitGreenSpheresButtonPressed = a
    canvas.data.boostInfoButtonPressed = False
    canvas.data.instructionsButtonPressed = False
    
def instructionsButtonPressed():
    a = canvas.data.instructionsButtonPressed
    a = not a
    canvas.data.instructionsButtonPressed = a
    canvas.data.boostInfoButtonPressed = False
    canvas.data.hitGreenSpheresButtonPressed = False

def printingSphereRunnerInformation():
    #prints the headings in the top middle
    canvas.create_text(canvas.data.canvasWidth/2,
                        canvas.data.canvasHeight/6,
                        text="SphereRunner", fill="red",
                        font="Helvetica 60 bold underline")
    canvas.create_text(canvas.data.canvasWidth/2,
                        canvas.data.canvasHeight/3,
                        text="INFORMATION", fill="red",
                        font="Helvetica 60 bold underline")

def printingPlayGameAndMenuButton():
    #creates the play game and menu button
    playGameButton = canvas.data.playGameButton
    canvas.create_window(canvas.data.canvasWidth*3/4,
                        canvas.data.canvasHeight - canvas.data.canvasHeight/6,
                        window=playGameButton)
    menuButton = canvas.data.menuButton
    canvas.create_window(canvas.data.canvasWidth/4,
                        canvas.data.canvasHeight - canvas.data.canvasHeight/6,
                        window=menuButton)

def printingBoostInfoButton():
    #creates boost info button at bottom
    t1="If the forward arrow button is pressed, the \ngame will speed up and"
    t2="the boost bar will fill.\nIf the backward arrow is pressed, the game "
    t3="will slow \ndown and the boost bar will deplenish. Speed up \nin easy "
    t4="areas and slow down in harder \nareas to make the game easier!!"
    printText = t1+t2+t3+t4
    boostInfoButton = canvas.data.boostInfoButton
    canvas.create_window(canvas.data.canvasWidth/4,
                        canvas.data.canvasHeight - canvas.data.canvasHeight/18,
                        window=boostInfoButton)
    if(canvas.data.boostInfoButtonPressed == True):
        canvas.create_rectangle(canvas.data.canvasWidth/12,
                                canvas.data.canvasHeight/12,
                                canvas.data.canvasWidth*11/12,
                                canvas.data.canvasHeight*9/12,
                                fill = "green", stipple="")
        canvas.create_text(canvas.data.canvasWidth/2,
                           canvas.data.canvasHeight*5/12,
                           text = printText,
                           font = "Helvetica 20")


def printingHitGreenSpheresButton():
    #creates hits green sphers button at bottom
    t1="While playing the game, instead of avoiding\nthe green spheres coming "
    t2="at you, hit the green\nspheres and receive an instant 50 points "
    t3="\nadded to your score.  It doesn't get much \neasier than that!!"
    printText = t1+t2+t3
    hitGreenSpheresButton = canvas.data.hitGreenSpheresButton
    canvas.create_window(canvas.data.canvasWidth*3/4,
                        canvas.data.canvasHeight - canvas.data.canvasHeight/18,
                        window=hitGreenSpheresButton)
    if(canvas.data.hitGreenSpheresButtonPressed == True):
        canvas.create_rectangle(canvas.data.canvasWidth/12,
                                canvas.data.canvasHeight/12,
                                canvas.data.canvasWidth*11/12,
                                canvas.data.canvasHeight*9/12,
                                fill = "green", stipple="gray25")
        canvas.create_text(canvas.data.canvasWidth/2,
                           canvas.data.canvasHeight*5/12,
                           text = printText,
                           font = "Helvetica 20")
    instructionsButton = canvas.data.instructionsButton
    canvas.create_window(canvas.data.canvasWidth/2,
                        canvas.data.canvasHeight - canvas.data.canvasHeight/18,
                        window=instructionsButton)

def printingInstructionsButton():
    #creates instructions button at bottom
    t1="Welcome to SphereRunner!!\nThe main objective of this game is to steer"
    t2="left and\nright while trying to avoid all spheres coming at you\n(the"
    t3="arrow at the bottom of the screen).  If you are\nable to do this, your"
    t4="score will increase as you\ncover more and more land. If you are good "
    t5="enough\nto beat the max score, your name will be \npreserved for all "
    t6="to see until it is overtaken."
    printText = t1+t2+t3+t4+t5+t6
    if(canvas.data.instructionsButtonPressed == True):
        canvas.create_rectangle(canvas.data.canvasWidth/12,
                                canvas.data.canvasHeight/12,
                                canvas.data.canvasWidth*11/12,
                                canvas.data.canvasHeight*9/12,
                                fill = "green", stipple="")
        canvas.create_text(canvas.data.canvasWidth/2,
                           canvas.data.canvasHeight*5/12,
                           text = printText,
                           font = "Helvetica 20")
        
def infoButtonPressed():
    canvas.data.playGame = False
    canvas.data.running = False
    canvas.data.menu = False
    canvas.data.info = True
    canvas.data.settings = False
    canvas.data.boostInfoButtonPressed = False
    canvas.data.hitGreenSpheresButtonPressed = False
    canvas.data.instructionsButtonPressed = False

##############################################
################# info stuff end #############
##############################################


        
        
######################################################
################# settings stuff begin ###############
######################################################

def settings():
    drawBackBoard()
    
    printingSphereRunnerSettings()
    printingPlayGameandMenuButtonOnSettings()
    printingDifferentSpeedSettingsButtons()
    printingDifferentDensitySettingsButtons()




def printingSphereRunnerSettings():
    #prints the heading on top middle of page
    canvas.create_text(canvas.data.canvasWidth/2,
                        canvas.data.canvasHeight/6,
                        text="SphereRunner", fill="red",
                        font="Helvetica 60 bold underline")
    canvas.create_text(canvas.data.canvasWidth/2,
                        canvas.data.canvasHeight/3,
                        text="SETTINGS", fill="red",
                        font="Helvetica 60 bold underline")

    
def printingPlayGameandMenuButtonOnSettings():
    #allows you to press play game or go back to menu
    playGameButton = canvas.data.playGameButton
    canvas.create_window(canvas.data.canvasWidth*3/4,
                        canvas.data.canvasHeight - canvas.data.canvasHeight/14,
                        window=playGameButton)
    menuButton = canvas.data.menuButton
    canvas.create_window(canvas.data.canvasWidth/4,
                        canvas.data.canvasHeight - canvas.data.canvasHeight/14,
                        window=menuButton)


def printingDifferentSpeedSettingsButtons():
    #creates buttons so you can choose which speed you want the game
    #default is set to medium
    canvas.create_text(canvas.data.canvasWidth/4, canvas.data.canvasHeight/2,
        text = "\nSPEED:",anchor = N,
        fill = "yellow", font = "Helvetica 23 bold underline")
    speedFastButton = canvas.data.speedFastButton
    canvas.create_window(canvas.data.canvasWidth/4,   
                    canvas.data.canvasHeight - canvas.data.canvasHeight*4/16,
                    window=speedFastButton)
    speedMediumButton = canvas.data.speedMediumButton
    canvas.create_window(canvas.data.canvasWidth/4,   
                    canvas.data.canvasHeight - canvas.data.canvasHeight*5/16,
                    window=speedMediumButton)
    speedSlowButton = canvas.data.speedSlowButton
    canvas.create_window(canvas.data.canvasWidth/4,   
                    canvas.data.canvasHeight - canvas.data.canvasHeight*3/8,
                    window=speedSlowButton)
    speedText = "Current = " + str(canvas.data.speed)
    canvas.create_text(canvas.data.canvasWidth/4,
            canvas.data.canvasHeight - canvas.data.canvasHeight*3/16,
            text = speedText,fill = "yellow", font = "Helvetica 23 bold")


def printingDifferentDensitySettingsButtons():
    #creates buttons so you can choose which density you want the game
    #default is set to medium
    canvas.create_text(canvas.data.canvasWidth*3
                       /4, canvas.data.canvasHeight/2,
        text = "\nSPHERE DENSITY:",anchor = N,
        fill = "orange", font = "Helvetica 23 bold underline")
    sphereDensityMaxButton = canvas.data.sphereDensityMaxButton
    canvas.create_window(canvas.data.canvasWidth*3/4,   
                    canvas.data.canvasHeight - canvas.data.canvasHeight*4/16,
                    window=sphereDensityMaxButton)
    sphereDensityMediumButton = canvas.data.sphereDensityMediumButton
    canvas.create_window(canvas.data.canvasWidth*3/4,   
                canvas.data.canvasHeight - canvas.data.canvasHeight*5/16,
                window=sphereDensityMediumButton)
    sphereDensityLeastButton = canvas.data.sphereDensityLeastButton
    canvas.create_window(canvas.data.canvasWidth*3/4,   
                canvas.data.canvasHeight - canvas.data.canvasHeight*3/8,
                window=sphereDensityLeastButton)
    sphereDensityText = "Current = " + str(canvas.data.density)
    canvas.create_text(canvas.data.canvasWidth*3/4,
                canvas.data.canvasHeight - canvas.data.canvasHeight*3/16,
                text = sphereDensityText,
                fill = "orange", font = "Helvetica 23 bold")


####set the global variables of speed and density to the selected amount
def speedFastButtonPressed():
    canvas.data.speed = "Fast"
def speedMediumButtonPressed():
    canvas.data.speed = "Medium"
def speedSlowButtonPressed():
    canvas.data.speed = "Slow"
def sphereDensityMaxButtonPressed():
    canvas.data.density = "Max"
def sphereDensityMediumButtonPressed():
    canvas.data.density = "Medium"
def sphereDensityLeastButtonPressed():
    canvas.data.density = "Least"


    

def settingsButtonPressed():
    canvas.data.playGame = False
    canvas.data.running = False
    canvas.data.menu = False
    canvas.data.info = False
    canvas.data.settings = True

######################################################
################ settings stuff end ##################
######################################################









######################################################
################ playGame stuff begin ################
######################################################
    
    
def playGame():
    #If this function is called, it will start you playing the game
    drawBackBoard()
    if(canvas.data.running == True):
        addNewRowToBoard()
    printBoard()
    drawArrow()
    score()
    boost()
    showKeyOptionsWhileGameRunning()
    maxScoreEver()
    sphereCrash()
    
    
    

def resetGame():
    #sets all parameters to the starting value
    createGrid()
    canvas.data.score = 0
    canvas.data.boost = 0
    canvas.data.timerCounter = 0
    canvas.data.leftEdge = canvas.data.startingLeftEdge
    canvas.data.shift = 0

                           

def createGrid():
    #creates a 2-D list
    board = []
    rows = canvas.data.rows
    cols = canvas.data.cols
    for row in range (rows):
        board += [[0] * cols]
    canvas.data.board = [] + board
    


def randomBoardRow():
    #creates a random row that can be added to the 2-D list
    spheresPerRowDeterminer = 10
    percentageChange = 4
    #percentage change will change the max num of spheres per row
    changeSpheresPerRow = spheresPerRowDeterminer/percentageChange
    if (canvas.data.density == "Max"):             
        spheresPerRowDeterminer -= changeSpheresPerRow
    if (canvas.data.density == "Least"):
        spheresPerRowDeterminer += changeSpheresPerRow
    highSphereValue = canvas.data.cols/spheresPerRowDeterminer
    spheresPerRow = random.randint(0,highSphereValue) #how many in that row
    cols = canvas.data.cols
    row = []
    for col in range (cols): #creates list of all zero's
        row += [0]
    for i in range (spheresPerRow-1):
        location = random.randint(0, len(row)-1)#puts number in random location
        while (row[location] != 0):  #makes sure spot is empty
             location = random.randint(0,len(row)-1)   
        color = random.randint(1,len(canvas.data.colorList))
        row[location] = color#sets row location to a random color
    return row


def addNewRowToBoard():
    # this takes a random row from randomBoardRow() and adds it to the 
    #beginning of the 2-D list and pops the last row
    board = [] + canvas.data.board
    newRow = [] + randomBoardRow()
    newBoard = [] + board
    newBoard.insert(0, newRow)
    newBoard.pop()
    setScore() #calls the function to add to the score
    canvas.data.board = [] + newBoard
    #print canvas.data.board

def setScore():
    #for each time a new row is added, the score will go up
    #based on the settings page information
    #ie. if you are playing on the highest density, your score increases faster
    if (canvas.data.density == "Least"):
        canvas.data.score +=1
    elif (canvas.data.density == "Medium"):
        canvas.data.score +=2
    elif (canvas.data.density == "Max"):
        canvas.data.score +=3

    if (canvas.data.speed == "Slow"):
        canvas.data.score +=1
    elif (canvas.data.speed == "Medium"):
        canvas.data.score +=2
    elif (canvas.data.speed == "Fast"):
        canvas.data.score +=3
    





      
def printBoard():
    #calls drawSphere and this draws all the spheres moving down the board
    impactRow = 9 #determines what row the arrow will be on
    rows = canvas.data.rows
    cols = canvas.data.cols
    displayCols = canvas.data.displayCols
    displayRows = canvas.data.displayRows
    board = canvas.data.board
    leftEdge = canvas.data.leftEdge
    for row in range (displayRows): #goes row by col to each item in 2d list
        for col in range (leftEdge, leftEdge + displayCols):
            col = col%canvas.data.cols   ##This makes the list wrap around   
            if (board[row][col] > 0 and board[row][col] < 5):
                value = board[row][col] - 1
                color = canvas.data.colorList[value]
                drawSphere(row, col, color,leftEdge, impactRow)



def drawSphere(row, col, color,leftEdge, impactRow):
    #draws each individual sphere on the board
    sphereWidthGrowth = canvas.data.sphereWidthGrowth
    a = (canvas.data.canvasWidth/canvas.data.displayCols)
    colWidth = a + (sphereWidthGrowth*row)
    rowHeight = colWidth#(canvas.data.canvasHeight/canvas.data.displayRows)
    canvas.data.sphereDimensions = colWidth
    #----makes the spheres "3d" with focal point in center of screen----
    canvasCenter = canvas.data.canvasWidth/2
    colOffsetFromCenter = (col - (canvas.data.cols/2))
    
    left = canvasCenter + ((colOffsetFromCenter - canvas.data.shift)*colWidth) 
    right = left + colWidth
    top = (canvas.data.canvasHeight/2) + (row*rowHeight) - 5
    bottom = top + rowHeight

    canvas.create_oval(left,top,right,bottom, fill = color, width = 1)
              
                    
def drawArrow():
    #takes the cube dimensions for the given row based on the sphereWidthGrowth
    #it then finds the dimensions of that box and prints
    leftEdge = canvas.data.leftEdge
    row = canvas.data.impactRow #predetermined based on preferance
    col = leftEdge+(canvas.data.displayCols/2)
    sphereWidthGrowth = canvas.data.sphereWidthGrowth
    a = (canvas.data.canvasWidth/canvas.data.displayCols)
    colWidth = a + (sphereWidthGrowth*row)
    rowHeight = colWidth
    canvasCenter = canvas.data.canvasWidth/2
    colOffsetFromCenter = (col - (canvas.data.cols/2))
    left = canvasCenter + ((colOffsetFromCenter - canvas.data.shift)*colWidth) 
    top = (canvas.data.canvasHeight/2) + (row*rowHeight) - 5
   
    canvas.create_image(left,top,image = canvas.data.arrowPicture, anchor = NW)
    
    canvas.data.sphereCrashRow = row #saves the info for sphereCrash()
    canvas.data.sphereCrashCol = col


    

def sphereCrash():
    #checks the row, col from drawArrow and sees if that spot is empty
    row = canvas.data.sphereCrashRow
    col = canvas.data.sphereCrashCol
    board = canvas.data.board
    left1 = canvas.data.canvasWidth/2
    top1 = canvas.data.canvasHeight/4
    if (canvas.data.playGame == True and canvas.data.running == True):
        maxScoreEver()#prints max score in top right
        if(board[row][col] > 0 and board[row][col] <4):
            canvas.data.lastGamesScore=canvas.data.score#soit'll print in menu
            if (canvas.data.maxScoreEver == canvas.data.score):
                importMaxScoreEverName() #allows you to give your name
            canvas.data.score = 0
            menuButtonPressed()#goes to menu
        elif(board[row][col] == 4): #checks if equal to green
            canvas.data.score += 100 #adds 100 to score if you hit a green
            canvas.create_image(left1,top1,image=canvas.data.explosionPicture)
            #prints a picture so that you know you hit a green sphere

            

def score():
    #prints the score in the top left
    #also prints your last games score in menu page
    score = canvas.data.score
    lastGamesScore = canvas.data.lastGamesScore
    
    locX = canvas.data.canvasWidth/20
    locY = canvas.data.canvasHeight/16
    if (canvas.data.playGame == True):
        writeScore = str("Score = ") + str(score)
    elif (canvas.data.menu == True):
        writeScore = str("Score = ") + str(lastGamesScore)
    
    canvas.create_text(locX, locY, text = writeScore, anchor = NW,
                       fill = "green", font = "Helvetica 20 bold")


            

def maxScoreEver():
    #checks to see if your score is the max score ever
    locX = canvas.data.canvasWidth*19/20
    locY = canvas.data.canvasHeight/16
    locYName = canvas.data.canvasHeight*2/16
    
    if (canvas.data.score > int(canvas.data.maxScoreEver)):
        canvas.data.maxScoreEver = canvas.data.score
        canvas.data.maxScoreEverName = "YOU!!!" #chages name in game to "you"

    if(canvas.data.playGame == True or canvas.data.menu == True):
        maxScoreEverText=str("Max Score Ever = ")+str(canvas.data.maxScoreEver)
        maxScoreEverNameText = str("By: ") + str(canvas.data.maxScoreEverName)

    canvas.create_text(locX, locY, text = maxScoreEverText, anchor = NE,
                       fill = "green", font = "Helvetica 20 bold")
    canvas.create_text(locX, locYName, text = maxScoreEverNameText, anchor=NE,
                       fill = "black", font = "Helvetica 20 bold")


def importMaxScoreEverName():
    #after you crash, if you got max score, it will write your information
    #to a folder on the desktop

    #imports your name
    t1= "Congradulations!!\nYou Have Max Score\nEnter Your Name: "
    name = str(raw_input(t1))
    canvas.data.maxScoreEverName = name
    a = str(canvas.data.maxScoreEver)
    maxScoreEverText = a + "\n"+ str(canvas.data.maxScoreEverName)
    writeTextFile(str(maxScoreEverText), getDesktopPath("highScore.txt"))
        

def boost():
    #prints the boost bar in top left
    boost = canvas.data.boost
    locX = canvas.data.canvasWidth/20
    locY = canvas.data.canvasHeight*2/16
    writeBoost = str("Boost = ") 
    canvas.create_text(locX, locY, text = writeBoost, anchor = NW,
                       fill = "black", font = "Helvetica 20 bold")
    #creates the fullness box
    locX2 = 120
    boxHeight = 20
    boxWidth = 100
    canvas.create_rectangle(locX2-2,locY-2, locX2+boxWidth+2, locY+boxHeight+2,
                            fill = "",width=4) #outer border of box
    fillWidth = boost
    canvas.create_rectangle(locX2,locY, locX2+fillWidth, locY+boxHeight,
                            fill = "green",width=1) #prints how full it is
    
def showKeyOptionsWhileGameRunning():
    #shows what different keys will do while program is running
    canvas.create_text(canvas.data.canvasWidth/2, canvas.data.canvasHeight/100,
        text = "p = pause   m = menu   i = info   s = settings   r = restart",
        anchor = N, fill = "red", font = "Helvetica 18")


def playGameButtonPressed():
    resetGame()
    canvas.data.playGame = True
    canvas.data.running = True
    canvas.data.menu = False
    canvas.data.info = False
    canvas.data.settings = False



####################################################
################ playGame stuff end ################
####################################################            
            
            
    
            



    

def redrawAll():
    canvas.delete(ALL)
    if(canvas.data.menu == True):
        menu()
    elif(canvas.data.playGame == True):
        playGame()
    elif (canvas.data.info == True):
        info()
    elif (canvas.data.settings == True):
        settings()
    

def init():
    initSettingsButtons()
    initmainButtons1()
    initmainButtons2()
    initMaxScore()
    initStartingVariables1()
    initStartingVariables2()
    createGrid()
    redrawAll()
    

def initSettingsButtons():
    speedFastButton = Button(canvas, text="  FAST  ",
                        command=speedFastButtonPressed)
    canvas.data.speedFastButton = speedFastButton
    speedMediumButton = Button(canvas, text=" MEDIUM ",
                        command=speedMediumButtonPressed)
    canvas.data.speedMediumButton = speedMediumButton
    speedSlowButton = Button(canvas, text="  SLOW  ",
                        command=speedSlowButtonPressed)
    canvas.data.speedSlowButton = speedSlowButton
    sphereDensityMaxButton = Button(canvas, text="  MAX   ",
                        command=sphereDensityMaxButtonPressed)
    canvas.data.sphereDensityMaxButton = sphereDensityMaxButton
    sphereDensityMediumButton = Button(canvas, text=" MEDIUM ",
                        command=sphereDensityMediumButtonPressed)
    canvas.data.sphereDensityMediumButton = sphereDensityMediumButton
    sphereDensityLeastButton = Button(canvas, text="  LEAST   ",
                        command=sphereDensityLeastButtonPressed)
    canvas.data.sphereDensityLeastButton = sphereDensityLeastButton




def initmainButtons1():   
    playGameButton = Button(canvas, text="PLAY GAME", font="Helvetica 40 bold",
                        command=playGameButtonPressed)
    canvas.data.playGameButton = playGameButton
    infoButton = Button(canvas, text="  INFO  ",font="Helvetica 40 bold",
                        command=infoButtonPressed)
    canvas.data.infoButton = infoButton
    settingsButton = Button(canvas, text="SETTINGS",font="Helvetica 40 bold",
                            command=settingsButtonPressed)
    canvas.data.settingsButton = settingsButton
    menuButton = Button(canvas, text="  MENU  ",font="Helvetica 40 bold",
                            command=menuButtonPressed)
    canvas.data.menuButton = menuButton

def initmainButtons2():
    boostInfoButton= Button(canvas,text="Boost Info",
                            command = boostInfoButtonPressed)
    canvas.data.boostInfoButton = boostInfoButton
    hitGreenSpheresButton = Button(canvas,text="Hit Green Spheres",
                            command = hitGreenSpheresButtonPressed)
    canvas.data.hitGreenSpheresButton = hitGreenSpheresButton
    instructionsButton = Button(canvas,text="INSTRUCTIONS",
                            command = instructionsButtonPressed)
    canvas.data.instructionsButton = instructionsButton

def initMaxScore():
    #creates a file if it doesn't exist
    #reads data if it does exist
    if(fileExists(getDesktopPath("highScore.txt")) == True):
        #canvas.data.maxScoreEverList = a
        a = readTextFileAsList(getDesktopPath("highScore.txt"))
        canvas.data.maxScoreEverList = a
        canvas.data.maxScoreEver = int(canvas.data.maxScoreEverList[0])
        canvas.data.maxScoreEverName = str(canvas.data.maxScoreEverList[1])
        
    else:
        canvas.data.maxScoreEver = 0
        canvas.data.maxScoreEverName = "It Could Be YOU!!!"
        b=str(canvas.data.maxScoreEver)
        maxScoreEverText = b  + str(canvas.data.maxScoreEverName)
        c = str(canvas.data.maxScoreEver)
        writeTextFile(c,getDesktopPath("highScore.txt"))



def initStartingVariables1():
    canvas.data.density = "Medium"
    canvas.data.speed = "Medium"
    
    canvas.data.playGame = False
    canvas.data.running = False
    canvas.data.menu = True
    canvas.data.info = False
    canvas.data.settings = False
    canvas.data.boostInfoButtonPressed = False
    canvas.data.hitGreenSpheresButtonPressed = False
    canvas.data.instructionsButtonPressed = False
    

    
def initStartingVariables2():
    canvas.data.colorList = ["orange", "yellow", "red", "green"]
    canvas.data.impactRow = 8
    canvas.data.sphereCrashRow = 0
    canvas.data.sphereCrashCol = 0
    canvas.data.sphereWidthGrowth = 3
    canvas.data.shift = 0
    canvas.data.arrowSphereDimensions = 0
    canvas.data.lastGamesScore = 0
    canvas.data.timerCounter = 0
    canvas.data.sphereDimensions = 0
    canvas.data.score = 0 
    canvas.data.boost = 0
    canvas.data.startingLeftEdge = (canvas.data.cols-canvas.data.displayCols)/2
    canvas.data.leftEdge = canvas.data.startingLeftEdge
    
    

    

########### copy-paste below here ###########

def run():
    # create the root and the canvas
    global canvas
    root = Tk()
    root.resizable(width=FALSE, height=FALSE)
    width = 600
    height = 600
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    # Store canvas in root and in canvas itself for callbacks
    root.canvas = canvas.canvas = canvas
    # Set up canvas data and call init
    class Struct: pass
    canvas.data = Struct()
    canvas.data.canvasWidth = width
    canvas.data.canvasHeight = height
    canvas.data.startSphereWidth = 20
    canvas.data.rows = 30
    canvas.data.cols = 300
    canvas.data.displayRows = 20
    canvas.data.displayCols = 100
    canvas.data.keyPressed = []
    canvas.data.sphereHeight=canvas.data.canvasWidth/canvas.data.displayCols
    canvas.data.arrowPicture = PhotoImage(file = "arrow.gif")
    canvas.data.cloudPicture = PhotoImage(file = "clouds.gif")
    canvas.data.explosionPicture = PhotoImage(file = "100exp.gif")
    init()
    # set up events
    root.bind("<Button-1>", mousePressed)
    root.bind("<Key>", keyPressed)
    root.bind("<KeyRelease>", keyReleased)
    timerFired()
    # and launch the app
    root.mainloop()
    # This call BLOCKS (so your program waits until you close the window!)
run()
