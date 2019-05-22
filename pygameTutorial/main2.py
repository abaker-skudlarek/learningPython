# Alex Baker
# May 21 2019

# Following pygame tutorial on "thenewboston" by "sentdex"

import pygame
import time
import random

pygame.init()

#------------------------------------------------------------------------------#
#--------------------------- Variables ----------------------------------------#
#------------------------------------------------------------------------------#

# management variables
WINDOW_WIDTH  = 800
WINDOW_HEIGHT = 600
FPS = 144
font = pygame.font.SysFont(None, 25)
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


# colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# set window title
pygame.display.set_caption("Slither")

#------------------------------------------------------------------------------#
#--------------------------- Functions ----------------------------------------#
#------------------------------------------------------------------------------#

def messageToScreen(msg, color):
    screenText = font.render(msg, True, color)
    gameDisplay.blit(screenText, [WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2])

def gameLoop():
    # variables
    gameExit = False
    gameOver = False
    snakeSize = 20
    appleSize = 20
    movementSpeed = 2

    leadX = WINDOW_WIDTH / 2
    leadXChange = 0
    leadY = WINDOW_HEIGHT / 2
    leadYChange = 0

    appleX = random.randrange(0, WINDOW_WIDTH - appleSize)
    appleY = random.randrange(0, WINDOW_HEIGHT - appleSize)

    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)
            messageToScreen("Game over, press C to play again or Q to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    elif event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    leadXChange = -movementSpeed
                    leadYChange = 0
                elif event.key == pygame.K_RIGHT:
                    leadXChange = movementSpeed
                    leadYChange = 0
                elif event.key == pygame.K_UP:
                    leadYChange = -movementSpeed
                    leadXChange = 0
                elif event.key == pygame.K_DOWN:
                    leadYChange = movementSpeed
                    leadXChange = 0

        # check for going outside of window
        if(leadX >= WINDOW_WIDTH - snakeSize / 2 or leadX < 0
            or leadY >= WINDOW_HEIGHT - snakeSize / 2  or leadY < 0 ):
                gameOver = True

        leadX += leadXChange
        leadY += leadYChange

        gameDisplay.fill(white)

        # draw apple
        pygame.draw.rect(gameDisplay, red, [appleX, appleY, appleSize, appleSize])

        # draw snake
        pygame.draw.rect(gameDisplay, black, [leadX, leadY, snakeSize, snakeSize])

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit() # quit pygame
    quit()        # quit python

#------------------------------------------------------------------------------#
#--------------------------- Main Code ----------------------------------------#
#------------------------------------------------------------------------------#

# run main loop
gameLoop()









