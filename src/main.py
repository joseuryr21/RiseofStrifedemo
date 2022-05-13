#the game loop

import pygame
from view.renderGame import renderGame
from model.gamedata import attackStab, relocateMove, roundEndRestoration, isActionDecided, testActionsDecided

#----------------------------------------------------------------------#
#                            Initial setup                             #
#----------------------------------------------------------------------#

screen = pygame.display.set_mode([1920, 1080])
isRunning = True
cntLoopNum = 0
cntTurnNum = 0
clock = pygame.time.Clock()
renderGame(screen)
characterDecisions = ['','','','','','']

#----------------------------------------------------------------------#
#                              Functions                               #
#----------------------------------------------------------------------#

def checkButtonQuit():
    pygame.event.get()
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

def universalSetup():
    clock.tick(30)
    renderGame(screen)
    isRunning = checkButtonQuit()
    return isRunning

#----------------------------------------------------------------------#
#                             Game loop                                #
#----------------------------------------------------------------------#

while isRunning:
    optionSelecting = True
    while optionSelecting and isRunning:
        if cntTurnNum % 2 == 0: #player
            isRunning = universalSetup()
            testActionsDecided('friendly')
            characterDecisions[0], characterDecisions[1], characterDecisions[2] = isActionDecided('friendly')
            cntLoopNum += 1
            if characterDecisions[0] == True and characterDecisions[1] == True and characterDecisions[2] == True:
                cntTurnNum += 1
        else: #ai
            isRunning = universalSetup()
            characterDecisions[3], characterDecisions[4], characterDecisions[5] = isActionDecided('enemy')
            cntLoopNum += 1
            cntTurnNum += 1
            optionSelecting = False #test
    roundEndRestoration()
