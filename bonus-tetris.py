##please note, this was a class assignment. We were given some starter 
##code, but the implementation and logic behind each funct is self generated.


##BONUS CONDITIONS:
##Pause function (activated by 'p')
##Up now rotates pieces counter-clockwise, down rotates them clockwise,
##and space serves as the single-row down movement.
##Hard drop function controlled by tab
##Increasing difficulty as score increases(blocks move faster)
##Black screen when game is over instead of board background

from Tkinter import *
import random

def mousePressed(event):  
    pass

def keyPressed(event):
    if (canvas.data.isGameOver == False) and (canvas.data.isPaused == False):
        if (event.keysym == "Down"):        
            rotateFallingPieceClock()
        elif (event.keysym == "Left"):
            moveFallingPiece(0,-1)
        elif (event.keysym == "Right"):
            moveFallingPiece(0,+1)
        elif (event.keysym == "Up"):
            rotateFallingPieceCounter()     
        elif (event.keysym == "space"):
            moveFallingPiece(+1, 0)
        elif (event.keysym == "Tab"):
            hardDrop()
    if (event.keysym == "r"):
        init()
    if (event.keysym == "p"):
        canvas.data.isPaused = not canvas.data.isPaused      
    redrawAll()

def hardDrop():
    while moveFallingPiece(+1, 0):
        pass
    placeFallingPiece()
   
def placeFallingPiece():
    rows = len(canvas.data.fallingPiece)
    cols = len(canvas.data.fallingPiece[0])
    color = canvas.data.fallingPieceColor
    rowOffset = canvas.data.fallingPieceRow
    colOffset = canvas.data.fallingPieceCol
    for row in xrange(rows):
        for col in xrange(cols):         
            if (canvas.data.fallingPiece[row][col] == True):
                canvas.data.board[row+rowOffset][col+colOffset] = color
           
def removeFullRows():
    fullRows = 0
    col1 = 0
    score = 0
    for num in xrange(canvas.data.rows):
        for row in xrange(len(canvas.data.board)):
            for col in xrange(len(canvas.data.board[0])):
                if (num == row):
                    if (col1 == canvas.data.cols):
                        col1 = 0
                        fullRows = 0
                    col1+=1
                    if (canvas.data.board[row][col] != canvas.data.emptyColor):
                        fullRows += 1
                        if (fullRows == canvas.data.cols):
                            canvas.data.board.pop(row)
                            canvas.data.board.insert(0, ["blue","blue","blue",
                                                         "blue","blue","blue",
                                                         "blue","blue","blue",
                                                         "blue"])
                            score += 1
    canvas.data.score += (score**2)

def timerFired():
    if (canvas.data.isGameOver == False) and (canvas.data.isPaused == False):
        ##print "calling RemoveFullRows"
        if (moveFallingPiece(+1, 0) == False):
            placeFallingPiece()
            newFallingPiece()
            removeFullRows()
            if (fallingPieceIsLegal() == False):
                canvas.data.isGameOver = True
                redrawAll()
        redrawAll()
    if canvas.data.score <= 40:
        delay = 500 - (canvas.data.score*10)## milliseconds
    else:
        delay = 100
    canvas.after(delay, timerFired) ## pause, then call timerFired again

def fallingPieceCenter():
    centerRow=canvas.data.fallingPieceRow + (len(canvas.data.fallingPiece)/2)
    centerCol=canvas.data.fallingPieceCol + (len(canvas.data.fallingPiece[0])/2)
    return (centerRow,centerCol)

def rotateFallingPieceCounter():
    fallingPiece = canvas.data.fallingPiece
    (oldCenterRow,oldCenterCol) = fallingPieceCenter()
    fallingPieceRows = len(canvas.data.fallingPiece)
    fallingPieceCols = len(canvas.data.fallingPiece[0])
    newFallingPieceRows = fallingPieceCols
    newFallingPieceCols = fallingPieceRows
    newFallingPiece = []
    for row in range(newFallingPieceRows):
        newFallingPiece += [[0] * newFallingPieceCols]
    for row in xrange(newFallingPieceRows):
        for col in xrange(newFallingPieceCols): 
            magic = (newFallingPieceRows-row)-1 ##I thought of this at
                                                ##0300 and it was like
                                                ##magic to me.
            newFallingPiece[row][col] = fallingPiece[col][magic]
    canvas.data.fallingPiece = newFallingPiece
    (newCenterRow,newCenterCol) = fallingPieceCenter()
    canvas.data.fallingPieceRow += (oldCenterRow - newCenterRow)
    canvas.data.fallingPieceCol += (oldCenterCol - newCenterCol)
    if (fallingPieceIsLegal() == False):
        canvas.data.fallingPieceRow -= (oldCenterRow - newCenterRow)
        canvas.data.fallingPieceCol -= (oldCenterCol - newCenterCol)
        canvas.data.fallingPiece = fallingPiece

def rotateFallingPieceClock():
    fallingPiece = canvas.data.fallingPiece
    (oldCenterRow,oldCenterCol) = fallingPieceCenter()
    fallingPieceRows = len(canvas.data.fallingPiece)
    fallingPieceCols = len(canvas.data.fallingPiece[0])
    newFallingPieceRows = fallingPieceCols
    newFallingPieceCols = fallingPieceRows
    newFallingPiece = []
    for row in range(newFallingPieceRows):
        newFallingPiece += [[0] * newFallingPieceCols]
    for row in xrange(newFallingPieceRows):
        for col in xrange(newFallingPieceCols): 
            newVar = (newFallingPieceCols-col)-1
            newFallingPiece[row][col] = fallingPiece[newVar][row]
    canvas.data.fallingPiece = newFallingPiece
    (newCenterRow,newCenterCol) = fallingPieceCenter()
    canvas.data.fallingPieceRow += (oldCenterRow - newCenterRow)
    canvas.data.fallingPieceCol += (oldCenterCol - newCenterCol)
    if (fallingPieceIsLegal() == False):
        canvas.data.fallingPieceRow -= (oldCenterRow - newCenterRow)
        canvas.data.fallingPieceCol -= (oldCenterCol - newCenterCol)
        canvas.data.fallingPiece = fallingPiece

def fallingPieceIsLegal():
    for row in xrange(len(canvas.data.fallingPiece)):
        for col in xrange(len(canvas.data.fallingPiece[0])):
            if (canvas.data.fallingPiece[row][col] == True):
                colOnBoard = canvas.data.fallingPieceCol+col
                rowOnBoard = canvas.data.fallingPieceRow+row
                if (colOnBoard < 0) or (colOnBoard >= canvas.data.cols):
                    return False
                elif (rowOnBoard < 0) or (rowOnBoard >= canvas.data.rows):
                    return False
                elif(canvas.data.board[rowOnBoard][colOnBoard]
                     != canvas.data.emptyColor):
                    return False
    return True

def moveFallingPiece(drow,dcol):
    canvas.data.fallingPieceCol += dcol
    canvas.data.fallingPieceRow += drow
    if (fallingPieceIsLegal() == False):
        canvas.data.fallingPieceCol -= dcol
        canvas.data.fallingPieceRow -= drow
        return False
    return True
    
def drawCell(row,col,color):
    x0=canvas.data.margin + (canvas.data.cellSize*col)
    y0=canvas.data.margin + (canvas.data.cellSize*row)
    x1=canvas.data.margin + (canvas.data.cellSize*(col+1))
    y1=canvas.data.margin + (canvas.data.cellSize*(row+1))
    canvas.create_rectangle(x0+1, y0+1, x1-1, y1-1, fill=color, width=0)
    canvas.create_rectangle(x0, y0, x1, y1, fill="", width=4)
    
def drawBoard():
    for row in xrange(canvas.data.rows):
        for col in xrange(canvas.data.cols):
            drawCell(row,col,canvas.data.board[row][col])

def newFallingPiece():
    highRandom = len(canvas.data.tetrisPieces)
    randomNum = random.randint(0,highRandom-1)
    canvas.data.fallingPiece = canvas.data.tetrisPieces[randomNum]
    canvas.data.fallingPieceColor = canvas.data.tetrisPieceColors[randomNum]
    fallingPieceCols=len(canvas.data.fallingPiece[0])
    canvas.data.fallingPieceRow = 0
    canvas.data.fallingPieceCol = (canvas.data.cols/2) - (fallingPieceCols/2)
 
def drawFallingPiece():
    rows = len(canvas.data.fallingPiece)
    cols = len(canvas.data.fallingPiece[0])
    color = canvas.data.fallingPieceColor
    rowOffset = canvas.data.fallingPieceRow
    colOffset = canvas.data.fallingPieceCol
    for row in xrange(rows):
        for col in xrange(cols):         
            if (canvas.data.fallingPiece[row][col] == True):
                drawCell(row+canvas.data.fallingPieceRow,
                         col+canvas.data.fallingPieceCol,color)         
        
def drawGame():
    canvas.create_rectangle(0,0,canvas.data.canvasWidth,
                            canvas.data.canvasHeight, fill="orange", width=0)
    drawBoard()
    drawFallingPiece()

def redrawAll():
    canvas.delete(ALL)
    drawGame()
    if (canvas.data.isPaused == True):
        canvas.create_text(canvas.data.canvasWidth/2,
                           canvas.data.canvasHeight/2, text="PAUSED",
                           anchor = S, fill="white", font="ComicSans 24 bold")
        canvas.create_text(canvas.data.canvasWidth/2,
                           canvas.data.canvasHeight/2,
                           text="P to Resume, R to Restart",
                           anchor = N, fill="white", font="ComicSans 12 bold")
    if (canvas.data.isGameOver == True):
        canvas.create_rectangle(0,0,canvas.data.canvasWidth,
                                canvas.data.canvasHeight,fill="black", width=0)
        canvas.create_text(canvas.data.canvasWidth/2,canvas.data.canvasHeight/2,
                           text="Game Over", anchor = S,
                           fill="white",font="ComicSans 30 bold")
        canvas.create_text(canvas.data.canvasWidth/2,canvas.data.canvasHeight/2,
                           text="Play Again? Press R",anchor = N,
                           fill="white", font="ComicSans 18 bold")
    canvas.create_text(canvas.data.canvasWidth/2, 0, text = ("SCORE: " +
                        str(canvas.data.score)),anchor=N, fill="black",
                        font="ComicSans 12 bold")                                   
             

def createBoard(rows, cols):
    emptyColor = canvas.data.emptyColor
    board = []
    for row in range(rows):
        board += [[emptyColor] * cols]
    return board
   
def init():
    canvas.data.isPaused = False
    canvas.data.emptyColor = "blue"
    canvas.data.isGameOver = False
    canvas.data.board = createBoard(canvas.data.rows,canvas.data.cols)
    canvas.data.score = 0
    ##Seven "standard" pieces (tetrominoes)
    iPiece = [[ True,  True,  True,  True]]
    jPiece = [[ True, False, False ],[ True, True,  True]]
    lPiece = [[ False, False, True],[ True,  True,  True]]
    oPiece = [[ True, True],[ True, True]]
    sPiece = [[ False, True, True],[ True,  True, False ]]
    tPiece = [[ False, True, False ],[ True,  True, True]]
    zPiece = [[ True,  True, False ],[ False, True, True]]
    canvas.data.tetrisPieces = [iPiece, jPiece, lPiece,
                                oPiece, sPiece, tPiece, zPiece]
    canvas.data.tetrisPieceColors = [ "red", "yellow", "magenta", "pink",
                                      "cyan", "green", "orange" ]
    highRandom = len(canvas.data.tetrisPieces)
    randomNum = random.randint(0,highRandom-1)
    canvas.data.fallingPiece = canvas.data.tetrisPieces[randomNum]
    canvas.data.fallingPieceColor = canvas.data.tetrisPieceColors[randomNum]
    fallingPieceCols = len(canvas.data.fallingPiece[0])
    canvas.data.fallingPieceRow = 0
    canvas.data.fallingPieceCol = (canvas.data.cols/2) - (fallingPieceCols/2)
    redrawAll()

 ########### copy-paste below here ###########

def run():
    ## create the root and the canvas
    global canvas
    root = Tk()
    rows = 15
    cols = 10
    cellSize = 20
    orangeMargin=24
    canvasWidth = (cols*cellSize) + (2*orangeMargin)
    canvasHeight = (rows*cellSize) + (2*orangeMargin)
    canvas = Canvas(root, width=canvasWidth, height=canvasHeight)
    canvas.pack()
    root.resizable(width=0, height=0)
    ## Store canvas in root and in canvas itself for callbacks
    root.canvas = canvas.canvas = canvas
    ## Set up canvas data and call init
    class Struct: pass
    canvas.data = Struct()
    canvas.data.rows=rows
    canvas.data.cols=cols
    canvas.data.cellSize=cellSize
    canvas.data.canvasWidth=canvasWidth
    canvas.data.canvasHeight=canvasHeight
    canvas.data.margin=orangeMargin
    init()
    ## set up events
    root.bind("<Button-1>", mousePressed)
    root.bind("<Key>", keyPressed)
    timerFired()
    ## and launch the app
    root.mainloop()  ## This call BLOCKS (so your program waits
                     ##until you close the window!)

run()  
