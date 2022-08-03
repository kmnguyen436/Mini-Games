import pygame
import random
def run():
    from pygame.locals import (
        K_ESCAPE,
        KEYDOWN,
        QUIT,
    )

    # initialize some variables
    pygame.init()
    SCREEN_WIDTH = 700
    SCREEN_HEIGHT = 700

    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (139,0,0)
    neonred = (255, 0, 0)
    green = (46,139,87)
    neongreen = (124,252,0)
    blue = (0, 0, 255)
    neonblue = (0,238,238)
    purple = (122, 55, 139)
    neonpurple = (255,0,255)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    start = False
    cluePauseTime = 333
    nextClueWaitTime = 1000
    pattern = [0,0,0,0,0,0,0,0]
    progress = 0
    guessCounter = 0
    mistakeCounter = 0
    clueHoldTime = 1000

    # this draws the start button and the game buttons
    def createBoard():
        pygame.display.set_caption("Simon - Memory Game")
        screen.fill(white)
        playButtonSize = 50

        rect = pygame.Rect(90, 100, playButtonSize+20, playButtonSize)
        pygame.draw.rect(screen, black, rect, 2, 15)
        buttonSize = 250
        rect1 = pygame.Rect(90, 165, buttonSize, buttonSize)
        rect2 = pygame.Rect(90, 420, buttonSize, buttonSize)
        rect3 = pygame.Rect(345, 165, buttonSize, buttonSize)
        rect4 = pygame.Rect(345, 420, buttonSize, buttonSize)
        screen.fill(red, rect1)
        pygame.draw.rect(screen, white, rect1, 5, 30)
        pygame.draw.rect(screen, black, rect1, 2, 30)
        screen.fill(blue, rect2)
        pygame.draw.rect(screen, white, rect2, 5, 30)
        pygame.draw.rect(screen, black, rect2, 2, 30)
        screen.fill(green, rect3)
        pygame.draw.rect(screen, white, rect3, 5, 30)
        pygame.draw.rect(screen, black, rect3, 2, 30)
        screen.fill(purple, rect4)
        pygame.draw.rect(screen, white, rect4, 5, 30)
        pygame.draw.rect(screen, black, rect4, 2, 30)
        pygame.display.flip()
    # this randomizes patterns in which buttons light up
    def createPattern(pattern):
        i = 0
        while i < len(pattern):
            num = random.randint(1,4)
            pattern[i] = num
            i += 1
    # buttons will light up and make sounds when pressed
    def lightButton(num):
        buttonSize = 250
        # for red button
        if num == 1:
            rect1 = pygame.Rect(90, 165, buttonSize, buttonSize)
            screen.fill(neonred, rect1)
            pygame.draw.rect(screen, white, rect1, 5, 30)
            pygame.draw.rect(screen, black, rect1, 2, 30)
            pygame.mixer.music.load('beeps/beep.wav')
            pygame.mixer.music.play()
        # for blue button
        elif num == 2:
            rect2 = pygame.Rect(90, 420, buttonSize, buttonSize)
            screen.fill(neonblue, rect2)
            pygame.draw.rect(screen, white, rect2, 5, 30)
            pygame.draw.rect(screen, black, rect2, 2, 30)
            pygame.mixer.music.load('beeps/beep2.wav')
            pygame.mixer.music.play()
        # for green button
        elif num == 3:
            rect3 = pygame.Rect(345, 165, buttonSize, buttonSize)
            screen.fill(neongreen, rect3)
            pygame.draw.rect(screen, white, rect3, 5, 30)
            pygame.draw.rect(screen, black, rect3, 2, 30)
            pygame.mixer.music.load('beeps/beep3.wav')
            pygame.mixer.music.play()
        # for purple button
        elif num == 4:
            rect4 = pygame.Rect(345, 420, buttonSize, buttonSize)
            screen.fill(neonpurple, rect4)
            pygame.draw.rect(screen, white, rect4, 5, 30)
            pygame.draw.rect(screen, black, rect4, 2, 30)
            pygame.mixer.music.load('beeps/beep4.wav')
            pygame.mixer.music.play()
        pygame.display.flip()
    # revert buttons back to its original color
    def clearButton():
        buttonSize = 250
        rect1 = pygame.Rect(90, 165, buttonSize, buttonSize)
        screen.fill(red, rect1)
        pygame.draw.rect(screen, white, rect1, 5, 30)
        pygame.draw.rect(screen, black, rect1, 2, 30)
        rect2 = pygame.Rect(90, 420, buttonSize, buttonSize)
        screen.fill(blue, rect2)
        pygame.draw.rect(screen, white, rect2, 5, 30)
        pygame.draw.rect(screen, black, rect2, 2, 30)
        rect3 = pygame.Rect(345, 165, buttonSize, buttonSize)
        screen.fill(green, rect3)
        pygame.draw.rect(screen, white, rect3, 5, 30)
        pygame.draw.rect(screen, black, rect3, 2, 30)
        rect4 = pygame.Rect(345, 420, buttonSize, buttonSize)
        screen.fill(purple, rect4)
        pygame.draw.rect(screen, white, rect4, 5, 30)
        pygame.draw.rect(screen, black, rect4, 2, 30)
        pygame.display.flip()
    # clue action for one button
    def playSingleClue(btn):
        lightButton(btn)
        pygame.time.wait(700)
        clearButton()
        pygame.time.wait(300)
    # put all clue actions together to create a sequence
    def playClueSequence():
        delay = nextClueWaitTime
        for i in range(progress+1):
            playSingleClue(pattern[i])
            delay += clueHoldTime
            delay += cluePauseTime
    # update round on screen
    def roundCount(progress):
        font = pygame.font.Font('freesansbold.ttf', 25)
        progress_text = font.render(str(progress), True, black)
        progressRect = progress_text.get_rect()
        progressRect.center = (440, 125)
        screen.blit(progress_text, progressRect)
        screen.fill(white, progressRect)
        progress_text = font.render(str(progress+1), True, black)
        screen.blit(progress_text, progressRect)
        return progress
    # update mistake on screen
    def mistakeCount(mistake):
        font = pygame.font.Font('freesansbold.ttf', 25)
        mistake_text = font.render(str(mistake), True, black)
        mistakeRect = mistake_text.get_rect()
        mistakeRect.center = (580, 125)
        screen.blit(mistake_text, mistakeRect)
        screen.fill(white, mistakeRect)
        mistake_text = font.render(str(mistake), True, black)
        screen.blit(mistake_text, mistakeRect)
        return mistake
    # action when game is lost
    def loseGame():
        text3 = font.render('Press the buttons in the correct order.', True, black)
        textRect3 = text3.get_rect()
        textRect3.center = (350, 40)
        text4 = font.render('You only get 3 tries. Good luck!', True, black)
        textRect4 = text4.get_rect()
        textRect4.center = (350, 75)
        screen.fill(white, textRect3)
        screen.fill(white, textRect4)
        text3 = font.render('Awww...You lost.', True, black)
        textRect3 = text3.get_rect()
        textRect3.center = (350, 40)
        screen.blit(text3, textRect3)
        text4 = font.render('Press start to play again.', True, black)
        textRect4 = text4.get_rect()
        textRect4.center = (350, 75)
        screen.blit(text4, textRect4)
        stopGame()
    # action when game is won
    def winGame():
        text3 = font.render('Press the buttons in the correct order.', True, black)
        textRect3 = text3.get_rect()
        textRect3.center = (350, 40)
        text4 = font.render('You only get 3 tries. Good luck!', True, black)
        textRect4 = text4.get_rect()
        textRect4.center = (350, 75)
        screen.fill(white, textRect3)
        screen.fill(white, textRect4)
        text3 = font.render('Yay! You won!', True, black)
        textRect3 = text3.get_rect()
        textRect3.center = (350, 40)
        screen.blit(text3, textRect3)
        text4 = font.render('Press start to play again.', True, black)
        textRect4 = text4.get_rect()
        textRect4.center = (350, 75)
        screen.blit(text4, textRect4)
        stopGame()
    # re-initialize everything to previous value when game restarts
    def reset():
        nonlocal mistakeCounter, guessCounter, pattern, progress, clueHoldTime, cluePauseTime, nextClueWaitTime
        cluePauseTime = 333
        nextClueWaitTime = 1000
        pattern = [0, 0, 0, 0, 0, 0, 0, 0]
        progress = 0
        guessCounter = 0
        mistakeCounter = 0
        clueHoldTime = 1000
    # look over player's guesses
    def guess(btn):
        nonlocal mistakeCounter, guessCounter, progress, clueHoldTime
        if mistakeCounter != 3:
            if btn == pattern[guessCounter]:
                if guessCounter == progress:
                    if progress == len(pattern) - 1:
                        roundCount(progress)
                        winGame()
                    else:
                        progress += 1
                        roundCount(progress)
                        guessCounter = 0
                        pygame.time.wait(600)
                        playClueSequence()
                        clueHoldTime -= 60
                else:
                    guessCounter += 1
            else:
                mistakeCounter += 1
                mistakeCount(mistakeCounter)
                if mistakeCounter == 3:
                    loseGame()
                else:
                    guessCounter = 0
                    pygame.time.wait(600)
                    playClueSequence()
        else:
            loseGame()

    createBoard()
    # Welcome message
    font = pygame.font.Font('freesansbold.ttf', 40)
    text1 = font.render('Welcome to the game!', True, black)
    # text = font.render('Repeat the pattern shown by pressing the buttons in the correct order. You only get 3 tries. Good luck!', True, black)
    textRect1 = text1.get_rect()
    textRect1.center = (SCREEN_WIDTH / 2, 50)
    screen.blit(text1, textRect1)
    font = pygame.font.Font('freesansbold.ttf', 25)
    text2 = font.render('Click start to play.', True, black)
    textRect2 = text2.get_rect()
    textRect2.center = (280, 125)
    screen.blit(text2, textRect2)

    start_text = font.render('Start', True, black)
    startRect = start_text.get_rect()
    startRect.center = (125, 125)
    screen.blit(start_text, startRect)
    pygame.display.flip()
    # action when start button is pressed
    def startPressed():
        screen.fill(white, textRect1)
        screen.fill(white, textRect2)
        screen.fill(white, startRect)
        stop_text = font.render('Stop', True, black)
        stopRect = start_text.get_rect()
        stopRect.center = (125, 125)
        screen.blit(stop_text, stopRect)

        text3 = font.render('Press the buttons in the correct order.', True, black)
        textRect3 = text3.get_rect()
        textRect3.center = (350, 40)
        screen.blit(text3, textRect3)
        text4 = font.render('You only get 3 tries. Good luck!', True, black)
        textRect4 = text4.get_rect()
        textRect4.center = (350, 75)
        screen.fill(white,textRect4)
        screen.blit(text4, textRect4)

        progress_text = font.render("Round: ", True, black)
        progressRect = progress_text.get_rect()
        progressRect.center = (390, 125)
        screen.blit(progress_text, progressRect)
        progress_text = font.render("Mistake: ", True, black)
        progressRect = progress_text.get_rect()
        progressRect.center = (520, 125)
        screen.blit(progress_text, progressRect)
        pygame.display.flip()
        pygame.time.wait(1500)
        startGame()
        return True
    def startGame():
        global clueHoldTime, mistakeCounter
        clueHoldTime = 1000
        createPattern(pattern)
        mistakeCounter = 0
        roundCount(progress)
        mistakeCount(mistakeCounter)
        playClueSequence()
    def stopGame():
        screen.fill(white, startRect)
        start_text1 = font.render('Start', True, black)
        startRect1 = start_text.get_rect()
        startRect1.center = (125, 125)
        screen.blit(start_text1, startRect1)
        pygame.display.flip()
        reset()
        return False
    progress = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_posx = pygame.mouse.get_pos()[0]
                mouse_posy = pygame.mouse.get_pos()[1]
                if 95 < mouse_posx < 155 and 107 < mouse_posy < 142 and not start:
                    start = startPressed()

                elif 95 < mouse_posx < 155 and 107 < mouse_posy < 142 and start:
                    start = stopGame()

                if 93 < mouse_posx < 340 and 169 < mouse_posy < 413:
                    lightButton(1)
                    pygame.time.wait(200)
                    clearButton()
                    pygame.time.wait(200)
                    if start:
                        guess(1)
                elif 93 < mouse_posx < 340 and 424 < mouse_posy < 665:
                    lightButton(2)
                    pygame.time.wait(200)
                    clearButton()
                    pygame.time.wait(200)
                    if start:
                        guess(2)
                elif 347 < mouse_posx < 593 and 169 < mouse_posy < 413:
                    lightButton(3)
                    pygame.time.wait(100)
                    clearButton()
                    pygame.time.wait(100)
                    if start:
                        guess(3)
                elif 347 < mouse_posx < 593 and 424 < mouse_posy < 665:
                    lightButton(4)
                    pygame.time.wait(100)
                    clearButton()
                    pygame.time.wait(100)
                    if start:
                        guess(4)

            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    running = False
            # Did the user click the window close button? If so, stop the loop.
            elif event.type == QUIT:
                running = False

if __name__ == "__main__":
    run()