#the game loop

import pygame
from view.renderGame import renderGame
from model.gamedata import attackStab, relocateMove

screen = pygame.display.set_mode([1920, 1080])
isRunning = True
cntLoopNum = 0
clock = pygame.time.Clock()

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
    isRunning = checkWindowQuit()
    isRunning = checkButtonQuit()
    renderGame(screen)
    attackStab('friendly1','enemy1')#test
    attackStab('enemy2','friendly3')#test
    relocateMove('friendly1', 8)
    cntLoopNum += 1
