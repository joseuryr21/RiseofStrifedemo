#the game loop

import pygame
from view.renderGame import renderGame

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



while isRunning:
    pygame.time.delay(50)
    isRunning = checkWindowQuit()
    if cntLoopNum % 2 == 0:
        renderGame(screen)
    cntLoopNum += 1
