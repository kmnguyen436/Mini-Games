from pygame.locals import *
import random
import pygame
import time
import math
height = width = 800
scale = 5
col = math.floor(width/scale)
row = math.floor(height/scale)
black = (0,0,0)
white = (255,255,255)
bordercolor = (79,8,8)
borderwidth = 1
PAUSE_COLOR = (0,255,255)

def drawBorderedRect(x,y,sc,c):
    pygame.draw.rect(sc,bordercolor,pygame.Rect(x,y,scale,scale))
    pygame.draw.rect(sc,c,pygame.Rect(x,y,scale-borderwidth,scale-borderwidth))

def create2DArray():
    fin = []
    for i in range(row):
        temp = []
        for j in range(col):
            temp.append(random.randint(0,1))
        fin.append(temp)
    return fin

def draw(g,s):
    for i in range(row):
        for j in range(col):
            xpos = i * scale
            ypos = j * scale
            if g[i][j] == 0:
                drawBorderedRect(xpos,ypos,s,black)
            else:
                drawBorderedRect(xpos,ypos,s,white)
    
def constructNextGen(g):
    temp = create2DArray()
    for i in range(row):
        for j in range(col):
            adj = countNeighbors(g,i,j)
            curr = g[i][j]
            
            if curr == 0 and adj == 3:
                temp[i][j] = 1
            elif curr == 1 and (adj < 2 or adj > 3):
                temp[i][j] = 0
            else:
                temp[i][j] = curr
    return temp
        
def countNeighbors(gr, x, y):
    sum = 0
    for i in range(-1,2):
        for j in range(-1,2):
            c = (x+i+col) % col
            r = (y+j+row) % row
            sum += gr[c][r]
    sum -= gr[x][y]
    return sum

def run():
    pygame.init()
    pygame.font.init()  
    scrn = pygame.display.set_mode((width,height), pygame.RESIZABLE)
    playing = True
    grid = create2DArray()
    running, pause = 1, 0
    state = running
    while playing:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                break
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    if state == pause:
                        return False
                    state = pause
                if event.key == K_r:
                    if state == pause:
                        state = running   
                    else:
                        grid = create2DArray()
        else:
            if state == running:
                draw(grid,scrn)
                time.sleep(.02)
                pygame.display.flip()
                grid = constructNextGen(grid)

if __name__ == "__main__":
    run()