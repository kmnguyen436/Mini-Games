import pygame
from pygame.locals import *
import random
import math
#initialize many global variables to be reused
colorList = [(0,0,255), (0,255,0), (255,0,0), (0,0,139), (89,12,12), (0,128,128), (0,0,0), (30,30,30)]
mineratio = 0.15
firstClick = True
bombCounter = 0
height = width = 800
boardsize = 15
scale = height//boardsize
black = (0,0,0)
gray = (155, 163, 157)
darkgray = (82,82,82)
row = math.floor(height/scale)
col = math.floor(width/scale)
tileArea = row*col
PAUSE_COLOR = (0,255,255)
clearstack = []
ttlMines = int(tileArea*mineratio)
ClearCon = tileArea - ttlMines
screen = pygame.display.set_mode((width,height),pygame.RESIZABLE)

class Piece:
    def __init__(self,bombStatus):
        self.bombStatus = bombStatus
        self.revealed = False
        self.hasFlag = False
    #simple getters and setters
    def getFlag(self):
        return self.hasFlag
    def getRevealed(self):
        return self.revealed
    def getBombStatus(self):
        return self.bombStatus
    def setBombStatus(self,st):
        self.bombStatus = st
    def setFlag(self,status):
        self.hasFlag = status
    def setNeighbors(self,amt):
        self.NumNeighbors = amt
    def getNeighbors(self):
        return self.NumNeighbors
    def setRevealed(self):
        self.revealed = True

    #Unique display in the show() function based on the status of the piece.
    def showPiece(self,x,y,scrn):
        global colorList
        if self.bombStatus:
            pass
        else:
            if self.getNeighbors() == 0:
                pygame.draw.rect(scrn,darkgray,pygame.Rect(x,y,scale-2,scale-2))
            else:
                FONT = pygame.font.SysFont("Aerial", scale)
                Sprite = FONT.render(str(self.NumNeighbors),False,colorList[self.NumNeighbors-1])
                pygame.draw.rect(scrn,darkgray,pygame.Rect(x,y,scale-2,scale-2))
                scrn.blit(Sprite,(x+(scale/3),y + (scale/4)))
    

def drawRect(x,y,c):
    #simply draws a bordered rectangle at a target location
    pygame.draw.rect(screen,black,pygame.Rect(x,y,scale,scale))
    pygame.draw.rect(screen,c,pygame.Rect(x,y,scale-2,scale-2))

def assignNeighbors(board):
    #once bombs are placed, iterate through once more to determine neighbor status of all blocks
    for r in range(row):
        for c in range(col):
            getAmtNeighbors(board,board[r][c],(r,c))

def createBoard():
    #initialize a 2d array with piece objects 
    board = []
    for r in range(row):
        r = []
        for c in range(col):
            piece = Piece(False)
            r.append(piece)
        board.append(r)

    #go through and find n amount of unique bomb spots and changge those pieces
    for k in range(ttlMines):
        x = random.randint(0,row-1)
        y = random.randint(0,col-1)
        while board[x][y].getBombStatus():
            x = random.randint(0,row-1)
            y = random.randint(0,col-1)
        board[x][y].setBombStatus(True)
    
    assignNeighbors(board)
    return board

def show(b):
    #shows the board based on the status of the individual pieces.
    for i in range(row):
        for j in range(col):
            xpos = i * scale
            ypos = j * scale
            if b[i][j].getRevealed():
                b[i][j].showPiece(xpos,ypos,screen)
            elif b[i][j].getFlag():
                drawRect(xpos,ypos,(0,255,0))
            else:
                drawRect(xpos,ypos,gray)

def onClick(pos,brd,rc):
    #get the board piece and firstClick status
    global firstClick
    i = pos[0] // scale
    j = pos[1] // scale
    piece = brd[i][j]

    #cannot click a piece already revealed, and cannot click a flagged block
    if piece.getRevealed() or (not rc and piece.getFlag()):
        return True

    #if they right click, toggle the flag on the piece
    if rc:
        if piece.getFlag():
            piece.setFlag(False)
        else:
            piece.setFlag(True)
        return True
    
    #if they clicked a bomb AND its not the first click, you lost. If it is the first click, erase the bomb so you cant lose on first click.
    if piece.getBombStatus():
        if firstClick:
            piece.setBombStatus(False)
            firstClick = False
            assignNeighbors(brd)
            return True
        else:
            return False

    #if nothing else, they made a normal click, reveal or cascade
    else:
        firstClick = False
        #if the block is empty with no neighbors, cascade and reveal all nearby blocks and those blocks with no neighbors
        if piece.getNeighbors() == 0:
            EmptyHandler(piece,brd,i,j)
        else:
            piece.setRevealed()
        return True

def RevealNeighbors(board, xc, yc):
    #iterate through neighbors on the board and clear them
    for i in range(-1,2):
        for j in range(-1,2):
            x = xc + i
            y = yc + j
            if x < 0 or x >= row or y < 0 or y >= col:
                continue
            board[x][y].setRevealed()

def EmptyHandler(piece, board, xc, yc):
    #reveal initial piece, and call reveal neighbors which reveals everyone around it.
    piece.setRevealed()
    RevealNeighbors(board,xc,yc)

    #append this to the clearstack list to prepare for cascade.
    clearstack.append(piece)

    #IF any neighbors around the empty piece are ALSO empty AND they are not in the clear stack, recursively call the function and clear them too
    for i in range(-1,2):
        for j in range(-1,2):
            x = xc + i
            y = yc + j
            if x < 0 or x >= row or y < 0 or y >= col:
                continue
            if board[x][y].getNeighbors() == 0 and (board[x][y] not in clearstack):
                EmptyHandler(board[x][y],board,x,y)
            else:
                pass


def getAmtNeighbors(board, piece, index):
    #check all neighbors and get a sum of them.
    sum = 0
    for i in range(-1,2):
        for j in range(-1,2):
            x = index[0] + i
            y = index[1] + j
            if x < 0 or x >= row or y < 0 or y >= col:
                continue
            if board[x][y].getBombStatus():
                sum += 1
            else:
                pass
    piece.setNeighbors(sum)

def checkWinCon(board):
    #if all pieces without a bomb have been cleared, you win
    for i in range(row):
        for j in range(col):
            if board[i][j].getRevealed():
                continue
            else:
                if board[i][j].getBombStatus():
                    continue
                else:
                    return False
    return True

def showFullBoard(board):
    #upon losing or winning, reveal the whole board including bombs
    for i in range(row):
        for j in range(col):
            xpos = i * scale
            ypos = j * scale
            if board[i][j].getRevealed():
                board[i][j].showPiece(xpos,ypos,screen)
            elif board[i][j].getFlag():
                if board[i][j].getBombStatus():
                    drawRect(xpos,ypos,(0,255,0))
                else:
                    pygame.draw.line(screen,(255,0,0),(xpos,ypos),(xpos+scale,ypos+scale),5)
                    pygame.draw.line(screen,(255,0,0),(xpos+scale,ypos),(xpos,ypos+scale),5)
            elif board[i][j].getBombStatus():
                drawRect(xpos,ypos,gray)
                pygame.draw.circle(screen,black,(xpos+(scale//2),ypos+(scale//2)),scale/4)
                pygame.draw.line(screen,black,(xpos+(scale//2),ypos+(scale//8)),(xpos+(scale//2),ypos+(7*scale)//8),5)
                pygame.draw.line(screen,black,(xpos+(scale//8),ypos+(scale//2)),(xpos+(7*scale)//8,ypos+scale//2),5)
            else:
                drawRect(xpos,ypos,gray)

def run():
    #initiliaze game variables and pygame, show first board
    pygame.init()
    playing = True
    board = createBoard()
    show(board)
    pygame.display.flip()
    #main game loop
    while True:
        #listener for player input
        for event in pygame.event.get():
            if event.type == QUIT:
                return False
            #if the player hits escape, it leaves
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                        return False
                if event.key == K_r:
                    global firstClick
                    board = createBoard()
                    playing = True
                    firstClick = True
                    show(board)
                    pygame.display.flip()
            #on click, determine if they lost/won, update and show board
            if playing:
                if event.type == MOUSEBUTTONDOWN:
                    typeClick = pygame.mouse.get_pressed()[2]
                    checkMove = onClick(pygame.mouse.get_pos(),board, typeClick)
                    if checkWinCon(board):
                        playing = False
                        showFullBoard(board)
                    if checkMove:
                        show(board)
                        pygame.display.flip()
                    else:
                        playing = False
        if not playing:
            showFullBoard(board)
            pygame.display.flip()

if __name__ == "__main__":
    run()