#the game loop

import pygame
from view.renderGame import renderGame
from model.gamedata import attackStab, relocateMove, roundEndRestoration

screen = pygame.display.set_mode([1920, 1080])
isRunning = True
cntLoopNum = 0
cntTurnNum = 0
clock = pygame.time.Clock()
renderGame(screen)

def checkWindowQuit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
            return isRunning
    isRunning = True
    return isRunning

def checkButtonQuit():
    mousePosition = pygame.mouse.get_pos()
    while mousePosition[0] > 1839 and mousePosition[1] < 81: #exit button location
        pygame.time.wait(10)
        pygame.event.get()
        mousePressed = pygame.mouse.get_pressed()
        mousePosition = pygame.mouse.get_pos()
        if mousePressed[0] == True:
            isRunning = False
            return isRunning
    isRunning = True
    return isRunning


while isRunning:
    clock.tick(30)
    renderGame(screen)
    isRunning = checkWindowQuit()
    isRunning = checkButtonQuit()
    optionSelecting = True
    while optionSelecting and isRunning:
        if cntTurnNum % 2 == 0: #player
            clock.tick(30)
            renderGame(screen)
            isRunning = checkWindowQuit()
            isRunning = checkButtonQuit()
            cntLoopNum += 1
            optionSelecting = False #test
        else: #ai
            clock.tick(30)
            renderGame(screen)
            isRunning = checkWindowQuit()
            isRunning = checkButtonQuit()
            cntLoopNum += 1
    roundEndRestoration()
