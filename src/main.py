#the game loop

import pygame
from view.renderGame import renderGame
from model.gamedata import attackStab

screen = pygame.display.set_mode([1920, 1080])
isRunning = True
cntLoopNum = 0

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
    pygame.time.delay(50)
    isRunning = checkWindowQuit()
    isRunning = checkButtonQuit()
    if cntLoopNum % 2 == 0:
        renderGame(screen)
    attackStab('friendly1','enemy1')#test
    attackStab('enemy2','friendly3')#test
    cntLoopNum += 1
