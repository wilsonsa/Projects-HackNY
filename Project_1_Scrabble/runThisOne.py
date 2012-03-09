# events-example0.py
# Barebones timer, mouse, and keyboard events
# as we will use them in Spring 2011's 15-110

import random
from Tkinter import *
from tile import *
from isAWord import *

def makeMenuPage():
    if canvas.data.gameMode==0:
        canvas.create_rectangle(0,0,
                                canvas.data.canvasWidth,
                                canvas.data.canvasHeight,
                                fill="FireBrick3")
        canvas.create_image(canvas.data.canvasWidth/2,#draws scrabTITlE picture
                            canvas.data.canvasHeight/4,
                            image=canvas.data.scrabbleTitle)
        canvas.create_image(canvas.data.canvasWidth/7,
                            canvas.data.canvasHeight/2,
                            image=canvas.data.scrabbleDecoration)
        canvas.create_image(canvas.data.canvasWidth*6/7,#draws both vertScrab
                            canvas.data.canvasHeight/2,
                            image=canvas.data.scrabbleDecoration)
        canvas.create_window(canvas.data.canvasWidth/2, #drawButtons
                             canvas.data.canvasHeight/2-30,
                             window=canvas.data.button1)
        canvas.create_window(canvas.data.canvasWidth/2,
                             canvas.data.canvasHeight/2,
                             window=canvas.data.button2)
        canvas.create_window(canvas.data.canvasWidth/2,
                             canvas.data.canvasHeight/2+30,
                             window=canvas.data.button3)
def makeGameInstructionPage():
    if canvas.data.gameMode==2:
        canvas.create_rectangle(0,0,
                                canvas.data.canvasWidth,
                                canvas.data.canvasHeight,
                                fill="Green")
        canvas.create_text(canvas.data.canvasWidth/12,50,
                           text= "GAME INSTRUCTIONS HERE",
                           anchor=NW,fill="Black",
                           font="times 23 underline" )
        canvas.create_text(canvas.data.canvasWidth/12+25,90,
                           text= "Scrabble Tiles\n\n\n\n\n"+
                           "Board Point Values\n\n\n\n\n"+
                           "Starting a Game\n\n\n"+
                           "End of a Game", anchor=NW,fill="Black",
                           font="times 22" )
        canvas.create_text(canvas.data.canvasWidth/12+50,130,
                           text= ("-A Scrabble game board is a 15 x 15 square"+
                                  "grid."+
                           "Scrabble is played with exactly100 tiles. 98 of"+
                                  "these tiles contain\n"
                           "  letters on them, while there are 2 blank tiles."+
                                  "These blank tiles add a wildcard aspect to"+
                                  "Scrabble. \n"+
                           "-Various letters have different point values,"+ 
                                  "depending on the rarity of the letter and"+
                                  "the difficulty in playing it. Blank\n"+
                           "  tiles have no point value.\n\n\n"+
                           "-Some squares on the Scrabble board represent"+
                                  "multipliers. If a tile is placed on this"+
                                  "square, then the tile's value is\n"+
                           "  multiplied by a factor or either 2x or 3x."+
                                  "Certain tiles multiply the point value of"+
                                  "an entire word and not simply the\n"+
                           "  tile on that space.\n"
                           "-These multipliers only work once.\n\n\n"+
                           "-Each player starts with seven pieces. The player"+
                                  "can do one of three things on a turn. The "+
                                  "player can place a word,\n"+
                           "  exchange tiles or pass.\n\n\n"+
                           "-When all of the tiles have been taken from the"+
                                  "bag and one player has used all of the "+
                                  "tiles on their rack, then the \n"+
                           "game ends.\n"+
                           "-The Scrabble player with the highest score after"+
                                  " all final scores are tallied wins.")
                           , anchor=NW,fill="Black", font="times 18" )
        canvas.create_window(canvas.data.canvasWidth/16,
                             canvas.data.canvasHeight*13/15,
                             window=canvas.data.button4)
        
def makeKeyInstructionPage():
    if canvas.data.gameMode==3:
        canvas.create_rectangle(0,0,
                                canvas.data.canvasWidth,
                                canvas.data.canvasHeight,
                                fill="Green")
        canvas.create_text(5,15,
                           text= "GAME KEY EXPLANATIONS\n",
                           anchor=NW, fill="Black", font="times 23 underline" )
        canvas.create_text(30,70, text="-Tiles, found on the bottom  rack,"+
                           "can be dragged directly onto the board.\n\n"+
                           "\n-On the right, clicking the GRAB button "+
                           "fills empty space in rack with a \n"+
                           "  random letter.\n\n"+
                           "\n-The box on the right records the earned"+
                           "score for each player. At the end\n"+
                           "  of the game, the player with highest score "+
                           "wins.\n\n"+
                           "-The SCRAMBLE button on the right rearranges"+
                           "the letters of the tiles on \n"+
                           "  your rack.\n"
                           "-The SUBMIT button on the right is pressed "+
                           "when you've completed a \n"+
                           "  word on the board. If the word you've placed"+
                           "it valid, you can continue\n"+
                           "  on, otherwise, you must rearrange.\n\n"+
                           "-The box containing the number on the right"+
                           "indicated the number of \n"+
                           "  pieces left in the bag.\n\n"+
                           "-The box containing the 7 blank cells is your"
                           +"Tile Holder. It will \n"+
                           "  contain the tiles that you will drag onto "+
                           "the board"
                           ,anchor=NW, fill="Black", font="times 18" )   
        canvas.create_window(canvas.data.canvasWidth/16,
                             canvas.data.canvasHeight*13/15,
                             window=canvas.data.button5)

def button1Pressed():
    canvas.data.gameMode=1
    redrawAll()
def button2Pressed(): #Game Instruction
    canvas.data.gameMode=2
    redrawAll()
def button3Pressed(): #Keys Tutorial
    canvas.data.gameMode=3
    redrawAll()
    
def button4Pressed(): #From game Instruction back to mainPage
    canvas.data.gameMode=0
    makeMenuPage()
    redrawAll()
def button5Pressed(): #from keys tutorial back to mainPage
    canvas.data.gameMode=0
    makeMenuPage()
    redrawAll()
def button6Pressed(): #from game backt to mainPage
    canvas.data.gameMode=0
    makeMenuPage()
    redrawAll()
def leftMousePressed(event):
#These are grabBag Coordinates
    if canvas.data.gameMode==1:
        x1=canvas.data.grabCoordX1
        y1=canvas.data.grabCoordY1    
        x2=canvas.data.grabCoordX2
        y2=canvas.data.grabCoordY2

        x3=canvas.data.scrambleCoordX1
        y3=canvas.data.scrambleCoordY1
        x4=canvas.data.scrambleCoordX2
        y4=canvas.data.scrambleCoordY2

        x5=canvas.data.submitCoordX1
        y5=canvas.data.submitCoordY1
        x6=canvas.data.submitCoordX2
        y6=canvas.data.submitCoordY2

        boardDimensionX1=10
        boardDimensionX2=730
        boardDimensionY1=10
        boardDimensionY2=730
        
        if (x1<event.x<x2 and y1<event.y<y2): #if click in Grab Box
            #print "asdkjhaskdjhakjshdjkas PRESSING GRAB BOX"
            makePiece()

        elif (x3<event.x<x4 and y3<event.y<y4): #if click in Scramble Box
            scrambleRack()

        elif (x5<event.x<x6 and y5<event.y<y6): #if click in Submit Box
            if (canvas.data.gameStatus=="First Move"):
                if wordPlacementIsValid()==True:
                    canvas.data.gameStatus="NormalMove1"
                    canvas.data.piecesOnRack = canvas.data.player2Pieces
                    canvas.data.score= canvas.data.score2
                    c = 0
                    for row in range (len(canvas.data.piecesOnRack)):
                        drawPieces(canvas.data.piecesOnRack[row],c)
                        c += 1
                    canvas.data.piecesPlacedInATurn=[] 
                #print "GameStatus:",canvas.data.gameStatus
            elif (canvas.data.gameStatus=="NormalMove1"):
                if wordPlacementIsValid()==True:
                    canvas.data.gameStatus="NormalMove2"
                    canvas.data.piecesOnRack = canvas.data.player1Pieces
                    canvas.data.score= canvas.data.score1
                    c = 0
                    for row in range (len(canvas.data.piecesOnRack)):
                        drawPieces(canvas.data.piecesOnRack[row],c)
                        c += 1
                    canvas.data.piecesPlacedInATurn=[]
                    
                #print "GameStatus:",canvas.data.gameStatus
                #changeTiles()
                #takes player2 tiles and places over player1 Tiles
                #wordPlacementIsValid()
            elif (canvas.data.gameStatus=="NormalMove2"):
                if wordPlacementIsValid()==True:
                    canvas.data.gameStatus="NormalMove1"
                    canvas.data.piecesOnRack = canvas.data.player2Pieces
                    canvas.data.score= canvas.data.score2
                    c = 0
                    for row in range (len(canvas.data.piecesOnRack)):
                        drawPieces(canvas.data.piecesOnRack[row],c)
                        c += 1
                    canvas.data.piecesPlacedInATurn=[]
                #print "GameStatus:",canvas.data.gameStatus
                #changeTiles()
                #takes player1 tiles and palces over player2 tiles
                #wordPlacementIsValid()
    #These are placerCell Coordinates

        elif (793<event.x<841 and 677<event.y<725):
            col=0
            #print canvas.data.piecesOnRack[0]
            canvas.data.pieceInHand=True
            isABlank(canvas.data.piecesOnRack[0])
            liftPieceFromPlacer(col, canvas.data.piecesOnRack[0])

        elif (841<event.x<889 and 677<event.y<725):
            #print canvas.data.piecesOnRack[1]
            canvas.data.pieceInHand=True
            isABlank(canvas.data.piecesOnRack[1])
            col=1
            liftPieceFromPlacer(col, canvas.data.piecesOnRack[1])

        elif (889<event.x<937 and 677<event.y<725):
            #print canvas.data.piecesOnRack[2]
            canvas.data.pieceInHand=True
            isABlank(canvas.data.piecesOnRack[2])
            col=2
            liftPieceFromPlacer(col, canvas.data.piecesOnRack[2])

        elif (937<event.x<985 and 677<event.y<725):
            #print canvas.data.piecesOnRack[3]
            canvas.data.pieceInHand=True
            isABlank(canvas.data.piecesOnRack[3])
            col=3
            liftPieceFromPlacer(col, canvas.data.piecesOnRack[3])

        elif (985<event.x<1033 and 677<event.y<725):
            #print canvas.data.piecesOnRack[4]
            canvas.data.pieceInHand=True
            isABlank(canvas.data.piecesOnRack[4])
            col=4
            liftPieceFromPlacer(col, canvas.data.piecesOnRack[4])

        elif (1033<event.x<1081 and 677<event.y<725):
            #print canvas.data.piecesOnRack[5]
            canvas.data.pieceInHand=True
            isABlank(canvas.data.piecesOnRack[5])
            col=5
            liftPieceFromPlacer(col, canvas.data.piecesOnRack[5])

        elif (1081<event.x<1129 and 677<event.y<725):
            #print canvas.data.piecesOnRack[6]
            canvas.data.pieceInHand=True
            isABlank(canvas.data.piecesOnRack[6])
            col=6
            liftPieceFromPlacer(col, canvas.data.piecesOnRack[6])

        #This is when you're actually moving a piece
        #already on the board to another place    
        elif ((boardDimensionX1<event.x<boardDimensionX2 and
               boardDimensionY1<event.y<boardDimensionY2) and
               isOccupied(viewToModel(event.x, event.y)[0],
                          viewToModel(event.x, event.y)[1])):
        
            canvas.data.pieceInHand=True

            tileInfo=(canvas.data.tilesOnBoard[
                viewToModel(event.x, event.y)[0]]
                      [viewToModel(event.x, event.y)[1]])
            #use the thing on the print function that
            #takes in the different x and y
            liftPieceFromBoard(tileInfo)
      

def leftMouseMoved(event):
    if canvas.data.pieceInHand==True:
        canvas.data.mouseX=event.x
        canvas.data.mouseY=event.y
        redrawAll()
        drawPiece(event.x, event.y, canvas.data.currentPiece)
    else:
        redrawAll()
    

def leftMouseReleased(event):         #within the Board Dimensions
    if (10<event.x<730 and 10<event.y<730 and canvas.data.pieceInHand==True): 
        x=event.x
        y=event.y
        #print "viewToModel:",viewToModel(x,y)
        viewToModel(x,y)
        tileInfo=canvas.data.currentPiece
        tileInfo.row=viewToModel(x,y)[0]
        tileInfo.col=viewToModel(x,y)[1]

        if (canvas.data.tilesOnBoard[tileInfo.row][tileInfo.col]!=False):
            moveBackToRack(tileInfo)
        else: #puts tile into a previously empty spot
            canvas.data.piecesPlacedInATurn.append(tileInfo)
            #print canvas.data.piecesPlacedInATurn
            
            #for x in range (len(canvas.data.piecesPlacedInATurn)):
                #print "row:",canvas.data.piecesPlacedInATurn[x].row
                #print "col:",canvas.data.piecesPlacedInATurn[x].col
            canvas.data.tilesOnBoard[tileInfo.row][tileInfo.col]=tileInfo
            
        #print canvas.data.tilesOnBoard
        
        drawPieceToBoard()
        computeScore(tileInfo.row, tileInfo.col, tileInfo)
        
        
        
        canvas.data.pieceInHand=False
    elif((not(10<event.x<730 and 10<event.y<730) #if it's not on board, 
         and canvas.data.pieceInHand==True)):    #move back to Rack
        tileInfo=canvas.data.currentPiece
        moveBackToRack(tileInfo)

        
        canvas.data.pieceInHand=False
    redrawAll()

def computeScore(row, col, tile):
    if (canvas.data.gameStatus=="First Move"
        or canvas.data.gameStatus=="NormalMove2"):
        if canvas.data.twoDCoordinates[row][col]=="DeepSkyBlue":
            canvas.data.score1+=3*tile.value
        elif canvas.data.twoDCoordinates[row][col]=="PaleTurquoise":
            canvas.data.score1+=2*tile.value
        else:
            canvas.data.score1+=tile.value
    elif canvas.data.gameStatus=="NormalMove1":
        if canvas.data.twoDCoordinates[row][col]=="DeepSkyBlue":
            canvas.data.score2+=3*tile.value
        elif canvas.data.twoDCoordinates[row][col]=="PaleTurquoise":
            canvas.data.score2+=2*tile.value
        else:
            canvas.data.score2+=tile.value
    #else:
        #print "oh noes"



def isOccupied(row, col):
    if canvas.data.tilesOnBoard[row][col]==False:
        return False
    else:
        return True
    
def isABlank(tile):
    if (tile.letter==" "):
        newLetter = str(raw_input("What is this letter? "))
        while (len(newLetter)!=1 or
               ((ord(newLetter)<65)
                or 90<ord(newLetter)<97
                or ord(newLetter)>122)):
            if(len(newLetter)!=1):
                newLetter= raw_input("One letter only please: ")        
            elif((ord(newLetter)<65) or 90<ord(newLetter)<97 or
                 ord(newLetter)>122):
                newLetter= raw_input("Between A and Z please: ")

        tile.letter=newLetter.upper()
        
def moveBackToRack(tileInfo):
    tileInfo.row=-1
    tileInfo.col=len(canvas.data.piecesOnRack)
    canvas.data.numPiecesOnRack+=1
    storePiecesOnRack(tileInfo)

def keyPressed(event):
    redrawAll()

def viewToModel(x, y):
    row = (y - canvas.data.margin) / canvas.data.colWidth
    col = (x - canvas.data.margin) / canvas.data.rowHeight
    return (row, col)

def drawPieceToBoard():
    board=canvas.data.tilesOnBoard   #contains "False" and Tile
    for row in range (len(board)):
        for col in range (len(board[0])):
            if board[row][col]!=False:
                drawTile(board[row][col])
    

def drawTile(piece):
    col = piece.col
    row = piece.row
    x0 = canvas.data.margin + col * canvas.data.colWidth+3
    x1 = x0 + canvas.data.colWidth-6
    y0 = canvas.data.margin + row * canvas.data.rowHeight+3
    y1 = y0 + canvas.data.rowHeight-6

    canvas.create_rectangle(x0, y0, x1, y1, fill = "LightGoldenrod1")
    letter=piece.letter
    value=piece.value
    canvas.create_text(((x1+x0)/2),((y1+y0)/2),text=letter,
                       fill="Black", font = "times 23", activefill="blue")
    canvas.create_text(((x1+x0)/2+16),((y1+y0)/2+14),text=value,
                       fill="Black", font = "times 10", activefill="blue")

def timerFired():
    redrawAll()
    delay = 99999999999999999 # milliseconds
    canvas.after(delay, timerFired) # pause, then call timerFired again

def drawPlayerTurn():
    playerTurn=""
    if (canvas.data.gameStatus=="First Move" or
        canvas.data.gameStatus=="NormalMove2"):
                playerTurn="Player 1's Turn"     
    elif canvas.data.gameStatus=="NormalMove1":
        playerTurn="Player 2's Turn"

    canvas.create_text(793, 640, text=playerTurn, anchor=NW,
                       fill="Gold", font="Times 20 underline")
def redrawAll():
    canvas.delete(ALL)
    if canvas.data.gameMode==1:
        drawBoard()
        drawSideBoard()
        drawGrabBag()
        drawScoreBoard()
        drawTilePlacer()
        drawRackScrambler()
        drawSubmitButton()
        drawPieceToBoard()
        drawNumPiecesLeft()
        drawPlayerTurn()
        c=0
        for row in range (len(canvas.data.piecesOnRack)):
            drawPieces(canvas.data.piecesOnRack[row],c)
            canvas.data.coordsOnRack+=1
            c+=1

    elif canvas.data.gameMode==0:
        makeMenuPage()

    elif canvas.data.gameMode==2:
        makeGameInstructionPage()
    elif canvas.data.gameMode==3:
        makeKeyInstructionPage()        
        #drawBoard()
        drawSideBoard()
        drawGrabBag()
        drawScoreBoard()
        drawTilePlacer()
        drawRackScrambler()
        drawSubmitButton()
        #drawPieceToBoard()
        drawNumPiecesLeft()


def liftPieceFromPlacer(col, tileInfo):
     drawTilePlacerCell(0,col)
     canvas.data.piecesOnRack.remove(tileInfo)
     canvas.data.numPiecesOnRack-=1
     canvas.data.currentPiece=tileInfo
     drawPiece(canvas.data.mouseX, canvas.data.mouseY, tileInfo)
     redrawAll()

def liftPieceFromBoard(tileInfo):
    row=tileInfo.row
    col=tileInfo.col
    drawCell(row,col)
    #print "BeforeLiftPiece:",isOccupied(row,col)
    canvas.data.tilesOnBoard[row][col]=False
    canvas.data.currentPiece=tileInfo
    canvas.data.piecesPlacedInATurn.pop()
    drawPiece(canvas.data.mouseX, canvas.data.mouseY, tileInfo)
    #print "AfterLiftPiece:",isOccupied(row,col)
    if (canvas.data.gameStatus=="First Move" or
        canvas.data.gameStatus=="NormalMove2"):
        canvas.data.score1-=tileInfo.value

    elif canvas.data.gameStatus=="NormalMove1":
        canvas.data.score2-=tileInfo.value
    drawScoreBoard()
    redrawAll()
    
    
def drawPiece(x, y, tileInfo):
    x0 = x - canvas.data.pieceWidth/2
    y0 = y - canvas.data.pieceHeight/2
    x1 = x + canvas.data.pieceWidth/2    
    y1 = y + canvas.data.pieceHeight/2
    #print "*****************"
    #print "x=", x, "y=",y
    #print "x0=", x0, "y0=",y0
    #print "x1=",x1, "y1=",y1
    #print "*****************"
    
    #print "TopLeft:",x0, ",", y0, "          ","BotRight:",x1,",",y1
    canvas.create_rectangle(x0, y0, x1, y1,
                            fill = "LightGoldenrod1")
    letter=tileInfo.letter 
    value=tileInfo.value
    canvas.create_text(((x1+x0)/2),((y1+y0)/2),
                       text=letter,
                       fill="Black",
                       font = "times 20")
    canvas.create_text(((x1+x0)/2+16),((y1+y0)/2+14),
                       text=value,
                       fill="Black",
                       font = "times 10")

def threeTimesWS(row,col):
    if (row==0 and col==0 or
        row==0 and col==7 or
        row==0 and col==14 or
        row==7 and col==0 or
        row==7 and col==14 or
        row==14 and col==0 or
        row==14 and col==7 or
        row==14 and col==14):
        return True #"red"       
        
def twoTimesWS(row,col):
    if (row==1 and col==1 or
        row==2 and col==2 or
        row==3 and col==3 or
        row==4 and col==4 or
        row==10 and col==10 or
        row==11 and col==11 or
        row==12 and col==12 or
        row==13 and col==13 or
        row==13 and col==1 or
        row==12 and col==2 or
        row==11 and col==3 or
        row==10 and col==4 or
        row==4 and col==10 or
        row==3 and col==11 or
        row==2 and col==12 or
        row==1 and col==13):
        return True#"IndianRed1"
    
def centerPiece(row,col):
    if (row==7 and col==7):
        return True
    
def threeTimesLS(row,col):
    if (row==1 and col==5 or
        row==1 and col==9 or
        row==5 and col==1 or
        row==5 and col==5 or
        row==5 and col==9 or
        row==5 and col==13 or
        row==9 and col==1 or
        row==9 and col==5 or
        row==9 and col==9 or
        row==9 and col==13 or
        row==13 and col==5 or
        row==13 and col==9):
        return True#"DeepSkyBlue"
        
def twoTimesLS(row,col):
    if (row==0 and col==3 or
        row==0 and col==11 or
        row==2 and col==6 or
        row==2 and col==8 or
        row==3 and col==0 or
        row==3 and col==7 or
        row==3 and col==14 or
        row==6 and col==2 or
        row==6 and col==12 or
        row==7 and col==3 or
        row==7 and col==11 or
        row==8 and col==2 or
        row==8 and col==12 or
        row==11 and col==0 or
        row==11 and col==7 or
        row==11 and col==14 or
        row==12 and col==6 or
        row==12 and col==8 or
        row==14 and col==3 or
        row==14 and col==11 or
        row==6 and col==6 or
        row==6 and col==8 or
        row==8 and col==6 or
        row==8 and col==8):
        return True#"PaleTurquoise"
    
def drawBoard():
    canvas.create_rectangle(0,0,
                            canvas.data.boardWidth,
                            canvas.data.boardHeight,
                            fill="gold")
    for row in xrange(canvas.data.rows):
        for col in xrange(canvas.data.cols):
            drawCell(row, col)
            
    for row in xrange(canvas.data.rows):
        for col in xrange(canvas.data.cols):
            writeBoardWords(row, col)
    canvas.create_window(canvas.data.canvasWidth*15/16,
                         canvas.data.canvasHeight*13/15,
                         window=canvas.data.button6)

def drawTilePlacer():
    canvas.data.boardWidth
    canvas.data.canvasWidth
    canvas.data.tilePlacerCoordX0=(canvas.data.boardWidth+canvas.data.colWidth)
    canvas.data.tilePlacerCoordY0=(canvas.data.canvasHeight-148)
    canvas.data.tilePlacerCoordX1=(canvas.data.boardWidth+
                                   canvas.data.colWidth+
                                   (canvas.data.colWidth*7)+
                                   canvas.data.margin1*2 )
    canvas.data.tilePlacerCoordY1=(canvas.data.canvasHeight-100
                                   +canvas.data.margin1*2)
    canvas.create_rectangle(canvas.data.tilePlacerCoordX0,
                            canvas.data.tilePlacerCoordY0,
                            canvas.data.tilePlacerCoordX1,
                            canvas.data.tilePlacerCoordY1,
                            fill="Brown")
    for col in range(7):
        drawTilePlacerCell(0,col)
        
def drawTilePlacerCell(row,col):

    x0 = (canvas.data.margin1 + col *
          canvas.data.colWidth+canvas.data.tilePlacerCoordX0)
    
    y0 = (canvas.data.margin1 + row *
          canvas.data.rowHeight+canvas.data.tilePlacerCoordY0)
    x1 = x0 + canvas.data.colWidth    
    y1 = y0 + canvas.data.rowHeight

    #print "TopLeft:",x0, ",", y0, "          ","BotRight:",x1,",",y1
    canvas.create_rectangle(x0, y0, x1, y1, fill = "yellow")
    
def drawCell(row,col):
    color = ""
    
    if threeTimesWS(row,col):
        color ="Red"
        canvas.data.coordinates+=[color]
        canvas.data.coordinatesTilesOnBoard+=[False]
    elif twoTimesWS(row,col):
        color="IndianRed1"
        canvas.data.coordinates+=[color]
        canvas.data.coordinatesTilesOnBoard+=[False]
    elif centerPiece(row,col):
        color="IndianRed1"
        canvas.data.coordinates+=[color]
        canvas.data.coordinatesTilesOnBoard+=[False]
    elif threeTimesLS(row,col):
        color="DeepSkyBlue"
        canvas.data.coordinates+=[color]
        canvas.data.coordinatesTilesOnBoard+=[False]
    elif twoTimesLS(row,col):
        color="PaleTurquoise"
        canvas.data.coordinates+=[color]
        canvas.data.coordinatesTilesOnBoard+=[False]
    else:
        color="wheat"
        canvas.data.coordinatesTilesOnBoard+=[False]
        canvas.data.coordinates+=[color]
        



    x0 = canvas.data.margin + col * canvas.data.colWidth
    x1 = x0 + canvas.data.colWidth
    y0 = canvas.data.margin + row * canvas.data.rowHeight
    y1 = y0 + canvas.data.rowHeight

    
    canvas.create_rectangle(x0, y0, x1, y1, fill = color)


def oneDToTwoD(list):
    #print list
    twoDList=[]
    oneDList=[]

    while(len(list)!= 0):
        oneDList+= [list.pop(0)]
        if (len(oneDList)==15):
            twoDList+=[oneDList]
            oneDList=[]
    return twoDList
    
    #print canvas.data.twoDCoordinates


def drawCenterStar():    
    verts = [5,20,20,20,25,5,30,20,45,20,32.5,30,
             37.5,45,25,35,12.5,45,17.5,30]
    for i in range(len(verts)):
        verts[i] += canvas.data.colWidth*7+7
    canvas.create_polygon(verts, fill='black')

def writeBoardWords(row,col):
    x0 = canvas.data.margin + col * canvas.data.colWidth
    x1 = x0 + canvas.data.colWidth
    y0 = canvas.data.margin + row * canvas.data.rowHeight
    y1 = y0 + canvas.data.rowHeight
    #print canvas.data.twoDCoordinates

    if (threeTimesWS(row,col)):
        written="Triple\nWord\nScore"
        canvas.create_text((x0+x1)/2, (y0+y1)/2, text=written,
                           fill="black", font="NewsGothic 7 bold")
    if (twoTimesWS(row,col)):
        written="Double\nWord\nScore"
        canvas.create_text((x0+x1)/2, (y0+y1)/2, text=written,
                           fill="black", font="NewsGothic 7 bold")
    if (centerPiece(row,col)):
        drawCenterStar()
    if (threeTimesLS(row,col)):
        written="Triple\nLetter\nScore"
        canvas.create_text((x0+x1)/2, (y0+y1)/2, text=written,
                           fill="black", font="NewsGothic 7 bold")
    if (twoTimesLS(row,col)):
        written="Double\nLetter\nScore"
        canvas.create_text((x0+x1)/2, (y0+y1)/2, text=written,
                           fill="black", font="NewsGothic 7 bold")    

def drawSideBoard():
    canvas.create_rectangle(canvas.data.boardWidth, 0,
                            canvas.data.canvasWidth,canvas.data.canvasHeight,
                            fill="royalblue")

def drawGrabBag():
    x1=canvas.data.grabCoordX1
    y1=canvas.data.grabCoordY1    
    x2=canvas.data.grabCoordX2
    y2=canvas.data.grabCoordY2
    canvas.create_rectangle(x1,y1,x2,y2,
                            fill="brown")
    canvas.create_text((x1+x2)/2,(y1+y2)/2,
                       text="Grab!",
                       fill="Gold",
                       font="Helvetica 40")

def drawScoreBoard():
    x1=canvas.data.scoreCoordX1
    y1=canvas.data.scoreCoordY1
    x2=canvas.data.scoreCoordX2
    y2=canvas.data.scoreCoordY2

    canvas.create_rectangle(x1,y1,x2,y2,
                            fill="brown")
    score1=canvas.data.score1
    score2=canvas.data.score2
    canvas.create_text(((x2-x1)/4)+x1,(y1+y2)/2-25,
                       text="Player1 Score:",
                       fill="Gold",
                       font="Helvetica 15")
    canvas.create_text(((x2-x1)/4)+x1,(y1+y2)/2+20,
                       text=score1,
                       fill="Gold",
                       font="Helvetica 15")
    
    canvas.create_text(((x2-x1)*3/4)+x1,(y1+y2)/2-25,
                       text="Player2 Score:",
                       fill="Gold",
                       font="Helvetica 15")
    canvas.create_text(((x2-x1)*3/4)+x1,(y1+y2)/2+20,
                       text=score2,
                       fill="Gold",
                       font="Helvetica 15")

def drawRackScrambler():
    x1=canvas.data.scrambleCoordX1
    y1=canvas.data.scrambleCoordY1
    x2=canvas.data.scrambleCoordX2
    y2=canvas.data.scrambleCoordY2

    canvas.create_rectangle(x1, y1, x2, y2, fill="brown")
    canvas.create_text(x1+((x2-x1)/2), y1+((y2-y1)/2),
                       text= "Scramble",
                       fill = "Gold",
                       font = "Helvetica 12" )


def scrambleRack():
#    print len(canvas.data.piecesOnRack)-1
#    for scramble in range (50):
    
    for scramble in xrange (10):
        x=random.randint(0,len(canvas.data.piecesOnRack)-1)     
        canvas.data.pieceInHand=True
        liftPieceFromPlacer(x, canvas.data.piecesOnRack[x])
        tileInfo=canvas.data.currentPiece
        moveBackToRack(tileInfo)
        canvas.data.pieceInHand=False

def drawSubmitButton():
    x1=canvas.data.submitCoordX1
    y1=canvas.data.submitCoordY1
    x2=canvas.data.submitCoordX2
    y2=canvas.data.submitCoordY2
    
    canvas.create_rectangle(x1, y1, x2, y2, fill="brown")
    canvas.create_text(x1+((x2-x1)/2), y1+((y2-y1)/2),
                       text= "Submit",
                       fill = "Gold",
                       font = "Helvetica 12" )

def drawNumPiecesLeft():
    x1=canvas.data.piecesLeftCoordX1
    y1=canvas.data.piecesLeftCoordY1
    x2=canvas.data.piecesLeftCoordX2
    y2=canvas.data.piecesLeftCoordY2

    piecesLeft=canvas.data.numPiecesInBag
    
    canvas.create_rectangle(x1, y1, x2, y2, fill="brown")
    canvas.create_text(x1+((x2-x1)/2), y1+((y2-y1)/2),
                       text= piecesLeft,
                       fill = "Gold",
                       font = "Helvetica 12" )
    

def getRandLetter():
    piecesInBag=len(canvas.data.scrabblePieces)
    counter=random.randint(0,piecesInBag-1)#number of pieces

    letter=canvas.data.scrabblePieces[counter]
    canvas.data.scrabblePieces.remove(letter)
    canvas.data.numPiecesInBag-=1
    return letter

def makePiece(): #takes a random piece and places it on rack

    #print numPiecesOnRack
    if len(canvas.data.piecesOnRack)<7:#number of Pieces allowed
        canvas.data.randomPiece=getRandLetter()
        piece = canvas.data.randomPiece
        
        canvas.data.randomPiecePointValue=assignPointValue(piece)
        pointValue=canvas.data.randomPiecePointValue
        #print "Piece:",piece,"PointValue:",pointValue

        col=canvas.data.coordsOnRack
        newPiece= Tile(piece, pointValue, -1, col)
        #row and col are currently "Dummy Values".aka Noting it's Off the Board
        #print newPiece.col

        storePiecesOnRack(newPiece)
        
        
def storePiecesOnRack(newPiece):
    c=0
    canvas.data.piecesOnRack.append(newPiece)
    #canvas.data.piecesOnRack containes list of tiles
    #print "*************", canvas.data.piecesOnRack[0]
    for row in range (len(canvas.data.piecesOnRack)):
        drawPieces(canvas.data.piecesOnRack[row],c)
        canvas.data.coordsOnRack+=1
        
        c+=1
 
def drawPieces(rackOfTiles,c):
    if rackOfTiles.letter!=None:
        tileHeight=canvas.data.pieceHeight
        tileWidth=canvas.data.pieceWidth
        numPiecesOnRack=canvas.data.numPiecesOnRack

        piece=rackOfTiles.letter
        pointValue=rackOfTiles.value
        
        drawTileIntoPlacerCell(0,c, piece, pointValue)
    else:
        row=rackOfTiles.row
        col=rackOfTiles.col
        drawTilePlacerCell(row,col)
        
def drawTileIntoPlacerCell(row,col, piece, pointValue):
    x0 = (canvas.data.margin1 + col *
          canvas.data.colWidth+canvas.data.tilePlacerCoordX0)
    y0 = (canvas.data.margin1 + row *
          canvas.data.rowHeight+canvas.data.tilePlacerCoordY0)
    x1 = x0 + canvas.data.colWidth    
    y1 = y0 + canvas.data.rowHeight

    #print "x0=", x0
    #print "y0=",y0
    #print "x1=",x1
    #print "y1=",y1
    
    #print "TopLeft:",x0, ",", y0, "          ","BotRight:",x1,",",y1
    canvas.create_rectangle(x0, y0, x1, y1,
                            fill = "LightGoldenrod1", activewidth=3)
    letter=piece
    value=pointValue
    canvas.create_text(((x1+x0)/2),
                       ((y1+y0)/2),
                       text=letter, fill="Black",
                       font = "times 20")
    canvas.create_text(((x1+x0)/2+16),
                       ((y1+y0)/2+14),
                       text=value,
                       fill="Black",
                       font = "times 10")
    canvas.data.placerOccupied =True

def assignPointValue(piece):
    pointValue = dict([("E",1),
                       ("A",1),
                       ("I",1),
                       ("O",1),
                       ("N",1),
                       ("R",1),
                       ("T",1),
                       ("L",1),
                       ("S",1),
                       ("U",1),
                       ("D",2),
                       ("G",2),
                       ("B",3),
                       ("C",3),
                       ("M",3),
                       ("P",3),
                       ("F",4),
                       ("H",4),
                       ("V",4),
                       ("W",4),
                       ("Y",4),
                       ("K",5),
                       ("J",8),
                       ("X",8),
                       ("Q",10),
                       ("Z",10),
                       (" ",0)])
    return pointValue[piece]

def pieceLocatedCenter():   
    counter=0
    for tiles in range(len(canvas.data.piecesPlacedInATurn)):
        if (canvas.data.piecesPlacedInATurn[tiles].row==7 and
            canvas.data.piecesPlacedInATurn[tiles].col==7):
            counter+=1
    if counter == 1:
        return True #need to make so if true, Locks it in
                    #place and its no longer your moce
    return False    

def wordPlacementIsValid():
    lastTilePlaced= (canvas.data.piecesPlacedInATurn
                     [len(canvas.data.piecesPlacedInATurn)-1])
    if canvas.data.gameStatus=="First Move":
        return pieceLocatedCenter() and fitsCrossWord(lastTilePlaced)
     #### least one letter on the center square (7,7)
    elif (canvas.data.gameStatus=="NormalMove1"
          or canvas.data.gameStatus=="NormalMove2"):
        return fitsCrossWord(lastTilePlaced)

def fitsCrossWord(lastTile):
    row = lastTile.row
    col = lastTile.col
    vertical = analyzeVertical(row, col)
    horizontal = analyzeHorizontal(row, col)

    
    #print "Vertical",vertical
    #print "Horizontal",horizontal
    return vertical and horizontal  

def analyzeVertical(r, c): #analyze vertically positioned word
    topMost=(-1,-1)
    string=""
    board=canvas.data.tilesOnBoard
    tileRow=r
    tileCol=c

    while (board[tileRow][tileCol]!=False
           and 0<=tileRow<=14
           and  0<=tileCol<=14):
        tileRow-=1
    topMost=(tileRow+1, tileCol) # finds coordinates of TopMost Piece
    return analyzeHorizOfVertical(topMost)

def analyzeHorizOfVertical(topMost):
    tileRow=topMost[0]
    tileCol=topMost[1]
    topMost=topMost
    board=canvas.data.tilesOnBoard
    string=""
    #Now we want to sweep down until we hit the bottom
    while (board[tileRow][tileCol]!=False
           and 0<=tileRow<=14
           and  0<=tileCol<=14):
        tile = board[tileRow][tileCol]  #col stays constant
        string+=tile.letter
        tileRow+=1
    if len(string)==1:
        return True
    else:
        return isAWord(string)  #if use isAWord function,
                #must set nuance that 1 letter word passes
        
    
def analyzeHorizontal(r,c): #analyze horizontally potitioned word
    leftMost=(-1,-1)
    string=""
    board=canvas.data.tilesOnBoard
    tileRow=r
    tileCol=c

    while (board[tileRow][tileCol]!=False
           and 0<=tileRow<=14
           and  0<=tileCol<=14):
        tileCol-=1
    leftMost=(tileRow, tileCol+1)
    return analyzeVertOfHorizontal(leftMost)

def analyzeVertOfHorizontal(leftMost):
    tileRow=leftMost[0]
    tileCol=leftMost[1]
    leftMost=leftMost
    string=""
    board=canvas.data.tilesOnBoard

    #Now we want to sweep to the right until we hit the edge of the word
    while (board[tileRow][tileCol]!=False
           and 0<=tileRow<=14
           and  0<=tileCol<=14):
        tile=board[tileRow][tileCol]
        string+=tile.letter
        tileCol+=1
    if len(string)==1:
            return True
    else:
        return isAWord(string) 
    
def init():
    #print "adfasfdfasfdfasfdfasfdfa"
    
    drawBoard()
    canvas.data.grabCoordX1=canvas.data.boardWidth+80   #GrabBag Dimensions
    canvas.data.grabCoordY1=30    
    canvas.data.grabCoordX2=canvas.data.canvasWidth-100
    canvas.data.grabCoordY2=canvas.data.canvasHeight-620
    
    canvas.data.scoreCoordX1=canvas.data.boardWidth+80 #scoreboard Dimensions
    canvas.data.scoreCoordY1=250
    canvas.data.scoreCoordX2=canvas.data.canvasWidth-100
    canvas.data.scoreCoordY2=canvas.data.canvasHeight-450

    canvas.data.tilePlacerCoordX0=(canvas.data.boardWidth+
                                   canvas.data.colWidth) #tilePlacer Dimensions

    canvas.data.tilePlacerCoordY0=canvas.data.canvasHeight-148
    canvas.data.tilePlacerCoordX1=(canvas.data.boardWidth+
                                  canvas.data.colWidth+
                                  (canvas.data.colWidth*7) )
    canvas.data.tilePlacerCoordY1=canvas.data.canvasHeight-100


    canvas.data.scrambleCoordX1=800 #Scramble Button Dimensions
    canvas.data.scrambleCoordY1=400
    canvas.data.scrambleCoordX2=canvas.data.scrambleCoordX1+150
    canvas.data.scrambleCoordY2=canvas.data.scrambleCoordY1+50

                                    #submit button Dimensions
    canvas.data.submitCoordX1=1000
    canvas.data.submitCoordY1=400
    canvas.data.submitCoordX2=canvas.data.submitCoordX1+150
    canvas.data.submitCoordY2=canvas.data.submitCoordY1+50

                                    #Pieces Left display dimension

    canvas.data.piecesLeftCoordX1=900 #Scramble Button Dimensions
    canvas.data.piecesLeftCoordY1=500
    canvas.data.piecesLeftCoordX2=canvas.data.piecesLeftCoordX1+150
    canvas.data.piecesLeftCoordY2=canvas.data.piecesLeftCoordY1+50

    canvas.data.twoDCoordinates=oneDToTwoD(canvas.data.coordinates)
    canvas.data.tilesOnBoard=oneDToTwoD(canvas.data.coordinatesTilesOnBoard)

    for x in range(7):
        makePiece()
    canvas.data.gameStatus="First Move"
    canvas.data.piecesOnRack = canvas.data.player1Pieces
    for x in range(7):
        makePiece()
        

    canvas.data.gameMode=0


    pass

########### copy-paste below here ###########

def run():
    # create the root and the canvas
    global canvas
    root = Tk()
    rows = 15
    cols = 15
    colWidth = 48
    rowHeight =48
    margin = 10
    pieceWidth=44
    pieceHeight=44
    boardWidth = 2*margin + cols*colWidth
    boardHeight = 2*margin + rows*rowHeight
    #print "boardWidth:",boardWidth
    #print "boardHeight:",boardHeight
    canvasWidth=boardWidth+550
    canvasHeight=boardHeight+80
    #print "canvasWidth:",canvasWidth
    #print "canvasHeight:",canvasHeight
    canvas = Canvas(root, width=canvasWidth, height=canvasHeight)
    canvas.pack()
    # Store canvas in root and in canvas itself for callbacks
    root.canvas = canvas.canvas = canvas
    # Set up canvas data and call init
    class Struct: pass
    canvas.data = Struct()
    canvas.data = Struct()
    canvas.data.boardWidth = boardWidth
    canvas.data.boardHeight = boardHeight
    canvas.data.canvasWidth=canvasWidth
    canvas.data.canvasHeight=canvasHeight
    canvas.data.colWidth = colWidth
    canvas.data.rowHeight = rowHeight
    canvas.data.margin = margin
    canvas.data.rows = rows
    canvas.data.cols = cols
    canvas.data.coordinates=[] #2 D list of All Colors on board
    canvas.data.twoDCoordinates=[] #2 D List of All colors on Board
    canvas.data.pieceWidth=pieceWidth
    canvas.data.pieceHeight=pieceHeight
    canvas.data.scrabblePieces=["A","A","A","A","A","A","A","A","A",
                                "B","B",
                                "C","C",
                                "D","D","D","D",
                                "E","E","E","E","E","E","E","E","E","E","E",
                                "E",
                                "F","F",
                                "G","G","G",
                                "H","H",
                                "I","I","I","I","I","I","I","I","I",
                                "J",
                                "K",
                                "L","L","L","L",
                                "M","M",
                                "N","N","N","N","N","N",
                                "O","O","O","O","O","O","O","O",
                                "P","P",
                                "Q",
                                "R","R","R","R","R","R",
                                "S","S","S","S",
                                "T","T","T","T","T","T",
                                "U","U","U","U",
                                "V","V",
                                "W","W",
                                "X",
                                "Y","Y",
                                "Z",
                                " "," "]
    canvas.data.randomPiece=""#randomPiece within the bounds of 100
                                #with equal chance per letter
    canvas.data.randomPiecePointValue=0
    canvas.data.numPiecesOnRack=0
    canvas.data.margin1=colWidth-pieceWidth
    canvas.data.placerOccupied=[]
    canvas.data.coordsOnRack=0
    canvas.data.mouseX=0
    canvas.data.mouseY=0
    canvas.data.tile=[]
    canvas.data.currentPiece=None
    canvas.data.pieceInHand=False
    canvas.data.occupiedBoardSpaces=[]
    canvas.data.coordinatesTilesOnBoard=[]
    canvas.data.tilesOnBoard=[]
    canvas.data.score1=0
    canvas.data.score2=0
    canvas.data.score=canvas.data.score1
    canvas.data.gameStatus=""
    canvas.data.piecesPlacedInATurn=[]
    canvas.data.scrabbleTitle=PhotoImage(file="scrabbleTitle.gif")
    canvas.data.scrabbleDecoration=PhotoImage(file="scrabbleDecoration.gif")
    canvas.data.player1Pieces=[]
    canvas.data.player2Pieces=[]
    canvas.data.piecesOnRack=canvas.data.player2Pieces

    canvas.data.numPiecesInBag=len(canvas.data.scrabblePieces)

    b1=Button(canvas,text=" Start Game" ,command=button1Pressed)
    canvas.data.button1=b1
    b2=Button(canvas,text="Instructions",command=button2Pressed)
    canvas.data.button2=b2
    b3=Button(canvas,text="    Keys    ",command=button3Pressed)
    canvas.data.button3=b3
    b4=Button(canvas,text="Back To Main",command=button4Pressed)
    canvas.data.button4=b4
    b5=Button(canvas,text="Back To Main",command=button5Pressed)
    canvas.data.button5=b5
    b6=Button(canvas,text="Back To Main",command=button6Pressed)
    canvas.data.button6=b6
    

    
    init()
    # set up events
    root.bind("<Button-1>", leftMousePressed)
    root.bind("<B1-Motion>", leftMouseMoved)
    root.bind("<B1-ButtonRelease>", leftMouseReleased)
    root.bind("<Key>", keyPressed)
    timerFired()
    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program
                    #waits until you close the window!)
    

run()
