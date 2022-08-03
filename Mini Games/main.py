import pygame
from pygame.locals import *
import MineSweeper
import GameOfLife
import TicTacToe
import Simon
import Connect4
height = 800
width = 800
def displayText(text,font,color,screen,x,y):
    textinit = font.render(text, 1, color)
    textimg = textinit.get_rect()
    textimg.topleft = (x,y)
    screen.blit(textinit,textimg)

def display(screen, cursorpos):
    screen.fill((1,50,32))
    TITLE_FONT = pygame.font.SysFont("Aerial", 150)
    GAMES_FONT = pygame.font.SysFont("Segoe UI", 100)
    CURSOR_IMAGE = pygame.image.load("images/Cursor.png")
    displayText("Minigames", TITLE_FONT, (204,164,61),screen,60,0)
    displayText("Minesweeper", GAMES_FONT, (204,164,61),screen,135,100)
    displayText("Game Of Life", GAMES_FONT, (204,164,61),screen,135,200)
    displayText("Tic Tac Toe", GAMES_FONT, (204,164,61),screen,135,300)
    displayText("Simon", GAMES_FONT, (204,164,61),screen,135,400)
    displayText("Connect Four", GAMES_FONT, (204,164,61),screen,135,500)
    displayText("Quit", GAMES_FONT, (204,164,61),screen,135,600)
    screen.blit(CURSOR_IMAGE,(80,(cursorpos*100)+50))
    


def main():
    pygame.init()
    screen = pygame.display.set_mode((width,height),pygame.RESIZABLE)
    Clock = pygame.time.Clock()
    cursorpos = 1
    while True:
        display(screen, cursorpos)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                break
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    if cursorpos == 1:
                        pass
                    else:
                        cursorpos -= 1
                if event.key == K_DOWN:
                    if cursorpos == 6:
                        pass
                    else:
                        cursorpos += 1
                if event.key == K_RETURN:
                    if cursorpos == 1:
                        MineSweeper.run()
                    elif cursorpos == 2:
                        GameOfLife.run()
                    elif cursorpos == 3:
                        TicTacToe.tictactoe()
                        pygame.display.set_mode((height,width), pygame.RESIZABLE)
                    elif cursorpos == 4:
                        Simon.run()
                        pygame.display.set_mode((height,width), pygame.RESIZABLE)
                    elif cursorpos == 5:
                        Connect4.run()
                        pygame.display.set_mode((height,width), pygame.RESIZABLE)
                    else:
                        pygame.quit()
                        quit()
        pygame.display.flip()
        Clock.tick(60)

if __name__ == "__main__":
    main()