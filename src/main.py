#the game loop

import pygame
from view.renderGame import renderGame, tileSprites, tileHoverPositions, checkTileStatus
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
characterDecisions = [False, False, False, False, False, False]
isButtonsPressed = [False, False, False, False, False, False]

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

def mouseActivity():
    mousePosition = pygame.mouse.get_pos()
    isMousePressed = pygame.mouse.get_pressed()
    return mousePosition, isMousePressed;

#----------------------------------------------------------------------#
#                             Game loop                                #
#----------------------------------------------------------------------#

while isRunning:
    optionSelecting = True
    while optionSelecting and isRunning:
        if cntTurnNum % 2 == 0: #player
            isRunning = universalSetup()
            if characterDecisions[0] == False:
                mousePosition, isMousePressed = mouseActivity() #choosing a place to do actions
                for i in range(0, 26): #
                    isHovered = checkTileStatus(mousePosition, tileSprites, tileHoverPositions[i][0], tileHoverPositions[i][1], tileHoverPositions[i][2], tileHoverPositions[i][3]) #
                    if isHovered == '/images/terrain/tileSelected.png' and isMousePressed[0]: #
                        characterDecisions[0] = relocateMove('friendly1', i + 1) #
                        i = 26
            elif characterDecisions[1] == False:
                    mousePosition, isMousePressed = mouseActivity() #choosing a place to do actions
                    for i in range(0, 26): #
                        isHovered = checkTileStatus(mousePosition, tileSprites, tileHoverPositions[i][0], tileHoverPositions[i][1], tileHoverPositions[i][2], tileHoverPositions[i][3]) #
                        if isHovered == '/images/terrain/tileSelected.png' and isMousePressed[0]: #
                            characterDecisions[1] = relocateMove('friendly2', i + 1) #
                            i = 26
            else:
                mousePosition, isMousePressed = mouseActivity() #choosing a place to do actions
                for i in range(0, 26): #
                    isHovered = checkTileStatus(mousePosition, tileSprites, tileHoverPositions[i][0], tileHoverPositions[i][1], tileHoverPositions[i][2], tileHoverPositions[i][3]) #
                    if isHovered == '/images/terrain/tileSelected.png' and isMousePressed[0]: #
                        characterDecisions[2] = relocateMove('friendly3', i + 1) #
                        i = 26
            #make a boolean for if move(for now), which is True when the button is clicked(press anim?). Then If if it's true and player clicks on a tile attempt to move to that tile
            #testActionsDecided('friendly')
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
    for i in range(0, 6):
        characterDecisions[i] = False
    roundEndRestoration()
