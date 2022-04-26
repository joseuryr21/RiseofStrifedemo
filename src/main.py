#the game loop

import pygame
from view.renderGame import renderGame

screen = pygame.display.set_mode([1920, 1080])
isRunning = True
cntLoopnum = 1

def checkQuit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
            return isRunning
    isRunning = True
    return isRunning



while isRunning:
    pygame.time.delay(20)
    isRunning = checkQuit()
    renderGame(screen)
    cntLoopnum += 1
