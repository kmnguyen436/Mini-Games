# Course: CS2520
# Assignment: Capstone Project

# Connect 4

from ast import Or
import pygame
from pygame.locals import *
import numpy as np

class Connect4():
    #constant values
    ROWS = 6
    COLS = 7
    RADIUS = 30

    #color constants
    WHITE   = (255,255,255)
    BLACK   = (0,0,0)
    RED     = (255,0,0)
    BLUE    = (0,0,255)
    YELLOW  = (255,255,0)
    TXTYELLOW = (240,240,0)

    #rectangles
    rects = {}

    def __init__(self):
        #fps
        self.clock = pygame.time.Clock()
        self.fps = 60

        #array of ints to keep track of what colors are on the board
        self.array = np.zeros((self.ROWS,self.COLS),int)

        #window displaying the board           
        self.screen = pygame.display.set_mode((800,600))    #window size
        self.screen.fill(self.WHITE)                        #background
        pygame.display.set_caption('Connect 4')             #window title/name

        #information around the screen
        pygame.font.init()
        font = pygame.font.SysFont('Arial', 40)
        text = font.render('Current Turn: ',False,self.BLACK,None)
        self.screen.blit(text,(10,5))

        text = font.render('Press:',False,self.BLACK,None)
        self.screen.blit(text,(20,535))

        #label the columns
        for i in range(1,8):
            text = font.render(str(i),False,self.BLACK,None)
            self.screen.blit(text,(180+70*(i-1),535))

        #connect4 board
        board_size = (500,430)                              #blue rectangle
        self.rects["board"] = pygame.Rect((150,100),board_size)
        pygame.draw.rect(self.screen,self.BLUE,self.rects["board"])
        pygame.draw.rect(self.screen,self.BLACK,self.rects["board"],2)    #border

        for c in range(self.COLS):                          #empty circles
            for r in range(self.ROWS):
                self.draw_circle(self.array,r,c)

        self.init_cols()

        #starts with red player
        self.player = 1
        self.display_turn()

        self.winner = None
        self.playing = True
        self.done = False

    def reset(self):
        'resets array and board for new game'
        self.array = np.zeros((self.ROWS,self.COLS),int)    #fill array with 0s again

        #redraw the board
        pygame.draw.rect(self.screen,self.BLUE,self.rects["board"])         #blue rectangle
        pygame.draw.rect(self.screen,self.BLACK,self.rects["board"],2)      #border

        for c in range(self.COLS):                          #empty circles
            for r in range(self.ROWS):
                self.draw_circle(self.array,r,c)

        self.player = 1         #start with red again
        self.display_turn()     #display turn

        self.winner = None      #new game, no winner yet
        self.playing = True     #playing again

    def init_cols(self):
        self.rects['col1'] = pygame.Rect(155,0,70,600)
        self.rects['col2'] = pygame.Rect(155+70,0,70,600)
        self.rects['col3'] = pygame.Rect(155+140,0,70,600)
        self.rects['col4'] = pygame.Rect(155+210,0,70,600)
        self.rects['col5'] = pygame.Rect(155+280,0,70,600)
        self.rects['col6'] = pygame.Rect(155+350,0,70,600)
        self.rects['col7'] = pygame.Rect(155+420,0,70,600)

    def draw_circle_border(self,center):
        'draws 1 pixel black border on circle'
        pygame.draw.circle(self.screen,self.BLACK,center,self.RADIUS,1)

    def circle_coords(self,r,c):
        'converts row and column values to x,y coordinates'
        x0 = 190
        y0 = 140
        x = x0 + 70*c
        y = y0 + 70*r
        return (x,y)        

    def draw_circle(self,array,r,c):
        'changes the color of a circle based on the row and color it is in'
        match array[r][c]:          #color determined by value in array
            case 0:
                color = self.WHITE
            case 1:
                color = self.RED
            case 2:
                color = self.YELLOW
        coords = self.circle_coords(r,c)    #convert array position into display coords

        #draws the circle
        pygame.draw.circle(self.screen,color,coords,self.RADIUS)
        self.draw_circle_border(coords)     #border

    def check_next_row(self,column):
        'searches for next empty slot in column from the bottom up'
        for i in range(self.ROWS-1,-1,-1):  #iterates thru [5,0] backwards
            if self.array[i][column] == 0:  #empty slot in column found
                return i                    #return row # of empty slot
        return None

    def erase_turn(self):
        'erases current turn display'
        pygame.draw.rect(self.screen,self.WHITE,(210,5,100,40))

    def display_turn(self):
        'display which player"s turn it currently is'
        self.erase_turn()                                   #erase
        font = pygame.font.SysFont('Arial', 40)
        if self.player == 1:                                #overwrite
            text = font.render('Red',False,self.RED,None)
        else:
            text = font.render('Yellow',False,self.TXTYELLOW,None)
        self.screen.blit(text,(210,5))

    def switch_player(self):
        'switches between player 1 and 2'
        if self.player == 1:
            self.player = 2
        else:
            self.player = 1
        self.display_turn()     #update display

    def check_horizontal_win(self):
        'checks for 4 pieces in a row horizontally'
        for i in range(self.ROWS):      #check every row
            for j in range(0,4):        #first piece of 4 found in col [0,3]
                #check for 4 in a row
                if self.array[i][j] != 0:   #zero is not a player
                    if self.array[i][j] == self.array[i][j+1] == self.array[i][j+2] == self.array[i][j+3]:
                        self.winner = self.array[i][j]      #updates winner

    def check_vertical_win(self):
        'checks for 4 pieces in a row vertically'
        for i in range(self.COLS):      #check every column
            for j in range(0,3):        #first piece of 4 can be found in row [0,2]
                #check for 4 in a row
                if self.array[j][i] != 0:
                    if self.array[j][i] == self.array[j+1][i] == self.array[j+2][i] == self.array[j+3][i]:
                        self.winner = self.array[j][i]      #updates winner

    def check_diagonal_win(self):
        'checks for 4 pieces in a row diagonally'

        #\ diagonals
        for i in range(0,3):            #check first three rows for first of 4
            for j in range(0,4):        #check first four columns for first of 4
                #check for 4 in a row
                if self.array[i][j] != 0:
                    if self.array[i][j] == self.array[i+1][j+1] == self.array[i+2][j+2] == self.array[i+3][j+3]:
                        self.winner = self.array[i][j]      #updates winner

        if self.winner == None:
            #/ diagonals
            for i in range(0,3):            #check first three rows for first of 4
                for j in range(3,7):        #check last four columns for first of 4
                    #check for 4 in a row
                    if self.array[i][j] != 0:
                        if self.array[i][j] == self.array[i+1][j-1] == self.array[i+2][j-2] == self.array[i+3][j-3]:
                            self.winner = self.array[i][j]      #updates winner
        

    def check_win(self):
        'does all the checks'
        self.check_horizontal_win()
        self.check_vertical_win()
        self.check_diagonal_win()

    def announce_win(self,player):
        'draws pop up box to announce winner and ask for a new game'
        box = pygame.Rect(170,150,460,300)
        pygame.draw.rect(self.screen,self.WHITE,box)        #box
        pygame.draw.rect(self.screen,self.BLACK,box,1)      #box border

        font = pygame.font.SysFont('Arial', 80)
        if player == 1:
            text = font.render('Red Wins!',False,self.RED,None)
            text_rect = pygame.Rect(250,150,100,100)
        else:
            text = font.render('Yellow Wins!',False,self.TXTYELLOW,None)
            text_rect = pygame.Rect(215,150,100,100)
        self.screen.blit(text,text_rect)                    #display winner

        font = pygame.font.SysFont('Arial', 60)             #display 'play again?'
        text = font.render('Play again?',False,self.BLACK,None)
        text_rect = pygame.Rect(270,250,100,100)
        self.screen.blit(text,text_rect)

        self.rects["yes_btn"] = pygame.Rect(200,350,150,70) 
        pygame.draw.rect(self.screen,self.BLACK,self.rects['yes_btn'])  #button
        text_rect = pygame.Rect(230,350,150,70)                         #button text
        text = font.render('Yes',False,self.WHITE,None)
        self.screen.blit(text,text_rect)

        self.rects["no_btn"] = pygame.Rect(450,350,150,70)  
        pygame.draw.rect(self.screen,self.BLACK,self.rects['no_btn'])   #button
        text_rect = pygame.Rect(495,350,150,70)                         #button text
        text = font.render('No',False,self.WHITE,None)
        self.screen.blit(text,text_rect)

    def end_game(self):
        self.playing = False            #end game
        self.erase_turn()               #nobody's turn
        self.announce_win(self.winner)  #summons the pop up box

    def drop_piece(self,column):
        empty_row = self.check_next_row(column)
        if empty_row != None:
            self.array[empty_row][column] = self.player     #update array
            self.draw_circle(self.array,empty_row,column)   #update display
            self.check_win()            #check for 4 in a row
            if self.winner == 1 or self.winner == 2:
                self.end_game()
            else:
                self.switch_player()    #successful drop; next turn

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #stops everything if window is closed
                self.done = True
                pygame.quit()   #end pygame instance
                quit()          #end program

            #key is pressed during game
            elif event.type == pygame.KEYDOWN and self.playing:    #user pressed a thing
                if event.key == pygame.K_1:     #column inputs
                    self.drop_piece(0)
                if event.key == pygame.K_2:
                    self.drop_piece(1)
                if event.key == pygame.K_3:
                    self.drop_piece(2)
                if event.key == pygame.K_4:
                    self.drop_piece(3)
                if event.key == pygame.K_5:
                    self.drop_piece(4)
                if event.key == pygame.K_6:
                    self.drop_piece(5)
                if event.key == pygame.K_7:
                    self.drop_piece(6)
                if event.key == pygame.K_ESCAPE:    #escape to stop playing
                    self.playing = False
            
            elif event.type == pygame.KEYDOWN and not self.playing:
                if event.key == pygame.K_ESCAPE:    #double escape to stop loop
                    self.done = True                #closes window

            #mouse click outside of game
            elif event.type == pygame.MOUSEBUTTONUP and not self.playing:
                pos = pygame.mouse.get_pos()
                if self.rects['yes_btn'].collidepoint(pos):
                    self.reset()
                elif self.rects['no_btn'].collidepoint(pos):
                    self.done = True

            #mouse click during game
            elif event.type == pygame.MOUSEBUTTONUP and self.playing:
                pos = pygame.mouse.get_pos()
                if self.rects['col1'].collidepoint(pos):
                    self.drop_piece(0)
                if self.rects['col2'].collidepoint(pos):
                    self.drop_piece(1)
                if self.rects['col3'].collidepoint(pos):
                    self.drop_piece(2)
                if self.rects['col4'].collidepoint(pos):
                    self.drop_piece(3)
                if self.rects['col5'].collidepoint(pos):
                    self.drop_piece(4)
                if self.rects['col6'].collidepoint(pos):
                    self.drop_piece(5)
                if self.rects['col7'].collidepoint(pos):
                    self.drop_piece(6)

    def run(self):
        while not self.done:
            dt = self.clock.tick(self.fps)      #fps
            self.event_loop()
            pygame.display.update()

    def play(self):
        self.__init__()
        self.run()
def run():
    pygame.init()
    game = Connect4()
    game.play()
if __name__ == '__main__':
    run()