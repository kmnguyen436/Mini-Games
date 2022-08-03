import pygame
import random
# Character class is used for displaying specific characters and moods
class Character(pygame.sprite.Sprite):
    # display bot during the game play
    def botNormal(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('images/Bot1.png'))
        self.sprites.append(pygame.image.load('images/Bot2.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]
    # display a happy bot when it wins
    def botWin(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('images/Bot1.png'))
        self.sprites.append(pygame.image.load('images/Bot2.png'))
        self.sprites.append(pygame.image.load('images/Bot_won.png'))
        self.sprites.append(pygame.image.load('images/Bot2.png'))
        self.sprites.append(pygame.image.load('images/Bot1.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]
    # display a sad bot when it loses
    def botLose(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('images/Bot_lost1.png'))
        self.sprites.append(pygame.image.load('images/Bot_lost2.png'))
        self.sprites.append(pygame.image.load('images/Bot_lost3.png'))
        self.sprites.append(pygame.image.load('images/Bot_lost2.png'))
        self.sprites.append(pygame.image.load('images/Bot_lost1.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
    # display the player during the game play
    def playerNormal(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('images/Player1.png'))
        self.sprites.append(pygame.image.load('images/Player2.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
    # display a happy player when they win
    def playerWin(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('images/Player1.png'))
        self.sprites.append(pygame.image.load('images/Player2.png'))
        self.sprites.append(pygame.image.load('images/Player_won.png'))
        self.sprites.append(pygame.image.load('images/Player2.png'))
        self.sprites.append(pygame.image.load('images/Player1.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
    # display a sad player when they lose
    def playerLose(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('images/Player_lost1.png'))
        self.sprites.append(pygame.image.load('images/Player_lost2.png'))
        self.sprites.append(pygame.image.load('images/Player_lost3.png'))
        self.sprites.append(pygame.image.load('images/Player_lost2.png'))
        self.sprites.append(pygame.image.load('images/Player_lost1.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
    def update(self):
        self.current_sprite += 1
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

def tictactoe():
    # initializing game...
    from pygame.locals import (
        K_ESCAPE,
        KEYDOWN,
        QUIT,
    )
    pygame.init()
    # initialize screen dimensions
    SCREEN_WIDTH = 700
    SCREEN_HEIGHT = 700

    white = (255, 255, 255)
    black = (0, 0, 0)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # createGrid method creates the game background
    def createGrid():
        # create screen
        pygame.display.set_caption("My Tic Tac Toe")
        screen.fill(white)
        pygame.display.flip()

        blockSize = 165  # Set the size of the grid block
        for x in range(3):
            for y in range(3):
                rect = pygame.Rect(100+blockSize*x, 160+blockSize*y, blockSize, blockSize)
                pygame.draw.rect(screen, black, rect, 1)
        rect = pygame.Rect(100, 160, blockSize*3, blockSize*3)
        pygame.draw.rect(screen, black, rect, 4)
        rect = pygame.Rect(225, 50, 250, 80)
        pygame.draw.rect(screen, black, rect, 4)
        pygame.display.flip()
    # takes the user's mouse input and checks where it lands on the grid
    # if the user presses one of the boxes, it will put their symbol there
    def playGame(posx, posy, turn):
        okay = False
        while not okay:
            # draw X symbols if user goes first
            if turn == 0:
                if 100 < posx < 265:
                    if 160 < posy < 325 and board[0][0] == 0:
                        addX(100, 160)
                        board[0][0] = 1
                        okay = True
                    elif 325 < posy < 490 and board[0][1] == 0:
                        addX(100, 325)
                        board[0][1] = 1
                        okay = True
                    elif 490 < posy < 655 and board[0][2] == 0:
                        addX(100, 490)
                        board[0][2] = 1
                        okay = True
                elif 265 < posx < 430:
                    if 160 < posy < 325 and board[1][0] == 0:
                        addX(265, 160)
                        board[1][0] = 1
                        okay = True
                    elif 325 < posy < 490 and board[1][1] == 0:
                        addX(265, 325)
                        board[1][1] = 1
                        okay = True
                    elif 490 < posy < 655 and board[1][2] == 0:
                        addX(265, 490)
                        board[1][2] = 1
                        okay = True
                elif 430 < posx < 595:
                    if 160 < posy < 325 and board[2][0] == 0:
                        addX(430, 160)
                        board[2][0] = 1
                        okay = True
                    elif 325 < posy < 490 and board[2][1] == 0:
                        addX(430, 325)
                        board[2][1] = 1
                        okay = True
                    elif 490 < posy < 655 and board[2][2] == 0:
                        addX(430, 490)
                        board[2][2] = 1
                        okay = True
            # draw O symbols if user goes second
            if turn == 1:
                if 100 < posx < 265:
                    if 160 < posy < 325 and board[0][0] == 0:
                        addO(100, 160)
                        board[0][0] = 1
                        okay = True
                    elif 325 < posy < 490 and board[0][1] == 0:
                        addO(100, 325)
                        board[0][1] = 1
                        okay = True
                    elif 490 < posy < 655 and board[0][2] == 0:
                        addO(100, 490)
                        board[0][2] = 1
                        okay = True
                elif 265 < posx < 430:
                    if 160 < posy < 325 and board[1][0] == 0:
                        addO(265, 160)
                        board[1][0] = 1
                        okay = True
                    elif 325 < posy < 490 and board[1][1] == 0:
                        addO(265, 325)
                        board[1][1] = 1
                        okay = True
                    elif 490 < posy < 655 and board[1][2] == 0:
                        addO(265, 490)
                        board[1][2] = 1
                        okay = True
                elif 430 < posx < 595:
                    if 160 < posy < 325 and board[2][0] == 0:
                        addO(430, 160)
                        board[2][0] = 1
                        okay = True
                    elif 325 < posy < 490 and board[2][1] == 0:
                        addO(430, 325)
                        board[2][1] = 1
                        okay = True
                    elif 490 < posy < 655 and board[2][2] == 0:
                        addO(430, 490)
                        board[2][2] = 1
                        okay = True
            return okay
    # checks the option the computer chooses
    # if the player goes first, the computer marks an O
    # if the player goes second, the computer marks an X
    def computerPlays(x, y, turn):
        okay = False
        while not okay:
            # if computer goes first
            if turn == 0:
                if board[x][y] != 0:
                    return okay
                elif x == 0:
                    if y == 0:
                        addX(100, 160)
                    elif y == 1:
                        addX(100, 325)
                    elif y == 2:
                        addX(100, 490)
                elif x == 1:
                    if y == 0:
                        addX(265, 160)
                    elif y == 1:
                        addX(265, 325)
                    elif y == 2:
                        addX(265, 490)
                elif x == 2:
                    if y == 0:
                        addX(430, 160)
                    elif y == 1:
                        addX(430, 325)
                    elif y == 2:
                        addX(430, 490)
            # if computer goes second
            if turn == 1:
                if board[x][y] != 0:
                    return okay
                elif x == 0:
                    if y == 0:
                        addO(100, 160)
                    elif y == 1:
                        addO(100, 325)
                    elif y == 2:
                        addO(100, 490)
                elif x == 1:
                    if y == 0:
                        addO(265, 160)
                    elif y == 1:
                        addO(265, 325)
                    elif y == 2:
                        addO(265, 490)
                elif x == 2:
                    if y == 0:
                        addO(430, 160)
                    elif y == 1:
                        addO(430, 325)
                    elif y == 2:
                        addO(430, 490)
            board[x][y] = 2
            okay = True
            return okay
    # checkWin method checks if a win condition is met and checks who won
    # returns a tuple whether there was a win and then by whom
    # if there is a 0 in the tuple, the first person won. If 1, second person won.
    def checkWin():
        win = (True, 0)
        if board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1:
             
            return win
        elif board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1:
             
            return win
        elif board[0][0] == 1 and board[0][1] == 1 and board[0][2] == 1:
             
            return win
        elif board[1][0] == 1 and board[1][1] == 1 and board[1][2] == 1:
             
            return win
        elif board[2][0] == 1 and board[2][1] == 1 and board[2][2] == 1:
             
            return win
        elif board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 1:
             
            return win
        elif board[0][1] == 1 and board[1][1] == 1 and board[2][1] == 1:
             
            return win
        elif board[0][2] == 1 and board[1][2] == 1 and board[2][2] == 1:
             
            return win
        else:
            win = (False, 0)
        win = (True, 1)
        if board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2:
              
            return win
        elif board[0][2] == 2 and board[1][1] == 2 and board[2][0] == 2:
              
            return win
        elif board[0][0] == 2 and board[0][1] == 2 and board[0][2] == 2:
              
            return win
        elif board[1][0] == 2 and board[1][1] == 2 and board[1][2] == 2:
              
            return win
        elif board[2][0] == 2 and board[2][1] == 2 and board[2][2] == 2:
              
            return win
        elif board[0][0] == 2 and board[1][0] == 2 and board[2][0] == 2:
              
            return win
        elif board[0][1] == 2 and board[1][1] == 2 and board[2][1] == 2:
              
            return win
        elif board[0][2] == 2 and board[1][2] == 2 and board[2][2] == 2:
              
            return win
        else:
            win = (False, 2)
        return win
    # method draws an X to the board
    def addX(x, y):
        mark_x = pygame.image.load('images/mark_x.png')
        mark_x = pygame.transform.scale(mark_x, (165, 165))
        screen.blit(mark_x, (x, y))
        pygame.display.flip()
    # method draws an O to the board
    def addO(x, y):
        mark_o = pygame.image.load('images/mark_o.png')
        mark_o = pygame.transform.scale(mark_o, (165, 165))
        screen.blit(mark_o, (x, y))
        pygame.display.flip()
    # popUpMessage method displays a message if user wins, loses,
    # or has a draw
    def popUpMessage(num):
        if num == 0:
            win_msg = pygame.image.load('images/won_msg.png')
            screen.blit(win_msg, (100, 200))
            pygame.display.flip()
        elif num == 1:
            lost_msg = pygame.image.load('images/lost_msg.png')
            screen.blit(lost_msg, (100, 200))
            pygame.display.flip()
        elif num == 2:
            draw_msg = pygame.image.load('images/draw_msg.png')
            screen.blit(draw_msg, (100, 200))
            pygame.display.flip()
    # an image of a yes and no button will appear
    def displayYesNoMsg():
        yes_msg = pygame.image.load('images/yes.png')
        screen.blit(yes_msg, (110, 450))
        pygame.display.flip()
        no_msg = pygame.image.load('images/no.png')
        screen.blit(no_msg, (400, 450))
        pygame.display.flip()
    # checks if the question is answered
    def answerYesNoMsg(posx, posy):
        if 129 < posx < 330 and 475 < posy < 575:
            return 1
        elif 410 < posx < 580 and 460 < posy < 575:
            return 0

    # create the grid and create all the sprites
    createGrid()
    bot_normal = pygame.sprite.Group()
    botN = Character()
    botN.botNormal(500,10)
    bot_normal.add(botN)

    botW = Character()
    bot_won = pygame.sprite.Group()
    botW.botWin(500,10)
    bot_won.add(botW)

    botL = Character()
    bot_lost = pygame.sprite.Group()
    botL.botLose(500,10)
    bot_lost.add(botL)

    player_normal = pygame.sprite.Group()
    playerN = Character()
    playerN.playerNormal(100,10)
    player_normal.add(playerN)

    player_won = pygame.sprite.Group()
    playerW = Character()
    playerW.playerWin(100,10)
    player_won.add(playerW)

    player_lost = pygame.sprite.Group()
    playerL = Character()
    playerL.playerLose(100,10)
    player_lost.add(playerL)

    # randomize if player goes first or not
    player = random.randint(0,1)
    # computer takes the other position
    computer = 1-player
    # if computer is 0, then they go first
    if computer == 0:
        botTurn = True
    else:
        botTurn = False
    # initialize the board and rounds
    board = [[0,0,0],[0,0,0],[0,0,0]]
    running = True
    currentRound = 0
    nextRound = 1
    moves = 0
    MAXMOVES = 9
    winner = (False, 0)
    answered = False
    # runs the game if running is true
    while running:
        #draw the player and computer bot on screen
        bot_normal.draw(screen)
        bot_normal.update()
        player_normal.draw(screen)
        player_normal.update()
        pygame.display.flip()
        pygame.time.wait(200)
        # check if there is a winner
        if winner[0]:
            break
        # computer goes first if it is 0
        if computer == 0 and botTurn and currentRound < nextRound:
            rect = pygame.Rect(230, 60, 240, 60)
            screen.fill(white, rect)
            image = pygame.image.load('images/bot_turn.png')
            image = pygame.transform.scale(image, (260, 100))
            screen.blit(image, (220, 40))
            pygame.display.flip()
            pygame.time.delay(800)
            currentRound += 1
            okay = False
            while not okay and not winner[0] and moves != MAXMOVES:
                x = random.randint(0, 2)
                y = random.randint(0, 2)
                okay = computerPlays(x, y, computer)
            winner = checkWin()
            moves += 1
            botTurn = False
        # get user mouse input
        for event in pygame.event.get():
            # player's turn
            if not botTurn:
                rect = pygame.Rect(230, 60, 240, 60)
                screen.fill(white, rect)
                image = pygame.image.load('images/player_turn.png')
                image = pygame.transform.scale(image, (260, 100))
                screen.blit(image, (220, 40))
                pygame.display.flip()
                # get user's mouse input
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_posx = pygame.mouse.get_pos()[0]
                    mouse_posy = pygame.mouse.get_pos()[1]
                    okay = playGame(mouse_posx, mouse_posy, player)
                    nextRound += 1
                    moves += 1
                    if okay:
                        botTurn = True
                    else:
                        botTurn = False
            if event.type == KEYDOWN:
                # stop loop if escape key is pressed
                if event.key == K_ESCAPE:
                    running = False
            # stop loop if they press the quit button
            elif event.type == QUIT:
                running = False
            winner = checkWin()
        # computer's turn when it is 1
        if computer == 1 and botTurn and currentRound + 2 == nextRound:
            rect = pygame.Rect(230, 60, 240, 60)
            screen.fill(white, rect)
            image = pygame.image.load('images/bot_turn.png')
            image = pygame.transform.scale(image, (260, 100))
            screen.blit(image, (220, 40))
            pygame.display.flip()
            pygame.time.delay(800)
            okay = False
            # randomize bot choices
            while not okay and not winner[0] and moves != MAXMOVES:
                bot_normal.update()
                player_normal.update()
                pygame.display.flip()
                x = random.randint(0, 2)
                y = random.randint(0, 2)
                okay = computerPlays(x, y, computer)
            botTurn = False
            winner = checkWin()
            pygame.display.flip()
            currentRound += 1
            moves += 1
        if not winner[0] and moves != MAXMOVES:
            continue
        # draw
        if not winner[0] and moves == MAXMOVES:
            popUpMessage(winner[1])
        # if there is a winner, check who won
        elif winner[0]:
            # player won
            if winner[1] == 0:
                popUpMessage(winner[1])
                player_won.draw(screen)
                player_won.update()
                bot_lost.draw(screen)
                bot_lost.update()
                pygame.display.flip()
                pygame.time.delay(200)
            # bot won
            elif winner[1] == 1:
                popUpMessage(winner[1])
                bot_won.draw(screen)
                bot_won.update()
                player_lost.draw(screen)
                player_lost.update()
                pygame.display.flip()
                pygame.time.delay(200)
        displayYesNoMsg()
        forceOut = False
        # wait until the user answers yes or no while sprites move
        while not answered:
            if winner[1] == 0:
                player_won.draw(screen)
                player_won.update()
                bot_lost.draw(screen)
                bot_lost.update()
            elif winner[1] == 1:
                bot_won.draw(screen)
                bot_won.update()
                player_lost.draw(screen)
                player_lost.update()
            pygame.display.flip()
            pygame.time.delay(200)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_posx = pygame.mouse.get_pos()[0]
                    mouse_posy = pygame.mouse.get_pos()[1]
                    ans = answerYesNoMsg(mouse_posx, mouse_posy)
                    # if user presses no, end game
                    if ans == 0:
                        running = False
                        answered = True
                        break
                    # if user presses yes, re-initialize values to original
                    # and start loop again
                    elif ans == 1:
                        createGrid()
                        player = random.randint(0, 1)
                        computer = 1 - player
                        board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                        running = True
                        currentRound = 0
                        nextRound = 1
                        moves = 0
                        MAXMOVES = 9
                        winner = (False, 0)
                        if computer == 0:
                            botTurn = True
                        else:
                            botTurn = False
                        answered = True
                        forceOut = True
                        pygame.display.flip()
                        break
                pygame.time.delay(200)
            if forceOut:
                answered = False
                break
        bot_normal.update()
        player_normal.update()
        pygame.display.flip()
        pygame.time.wait(200)
if __name__ == '__main__':
    pygame.init()
    tictactoe()
