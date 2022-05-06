#draws images and such
import pygame
import os
from model.gamedata import statsCharacter

tileSprites = ["/images/terrain/tileNormal.png", "/images/terrain/tileSelected.png", "/images/terrain/tileAttacked.png", "/images/terrain/tileHealed.png", "/images/terrain/tileLingered.png"]
tilePositions = [[80, 464], [80, 668], [264, 412], [264, 564], [264, 716], [448, 412], [448, 564], [448, 716], [632, 412], [632, 564], [632, 716], [816, 464], [816, 668], [1044, 464], [1044, 668], [1228, 412], [1228, 564], [1228, 716], [1412, 412], [1412, 564], [1412, 716], [1596, 412], [1596, 564], [1596, 716], [1780, 464], [1780, 668]]

def getDirectory():
    currentDirectory = str(os.getcwd())
    currentDirectory = currentDirectory.replace("\\",'/')
    return currentDirectory

def renderSky(screen, currentDirectory):
    skySprite = pygame.image.load(currentDirectory + '/images/terrain/Sky1.png')
    screen.blit(skySprite, (0, 0))

def renderGround(screen, currentDirectory):
    groundSprite = pygame.image.load(currentDirectory + '/images/terrain/Ground1.png')
    screen.blit(groundSprite, (0, 384)) #384 is below sky

def renderMenuFrame(screen, currentDirectory):
    menuFrameSprite = pygame.image.load(currentDirectory + '/images/menu/menuFrame/MenuFrame1.png')
    screen.blit(menuFrameSprite, (0, 792)) #792 is below ground

def renderButtons(screen, currentDirectory):
    attackSprite = pygame.image.load(currentDirectory + '/images/menu/grayMenu/mainbuttons/Attack1.png')
    defendSprite = pygame.image.load(currentDirectory + '/images/menu/grayMenu/mainbuttons/Defend1.png')
    specialSprite = pygame.image.load(currentDirectory + '/images/menu/grayMenu/mainbuttons/Special1.png')
    relocateSprite = pygame.image.load(currentDirectory + '/images/menu/grayMenu/mainbuttons/Relocate2.png')
    backSprite = pygame.image.load(currentDirectory + '/images/menu/grayMenu/mainbuttons/Back1.png')
    exitSprite = pygame.image.load(currentDirectory + '/images/menu/Exit1.png')
    screen.blit(attackSprite, (28, 824))
    screen.blit(defendSprite, (428, 824))
    screen.blit(specialSprite, (28, 948))
    screen.blit(relocateSprite, (428, 948))
    screen.blit(backSprite, (828, 824))
    screen.blit(exitSprite, (1840, 0))

def createBarSpritesheet(currentDirectory, index, characterType, statType):
    return (currentDirectory) + '/images/menu/blueMenu/' + characterType + statType + '/' + statType.lower() + str(index) + '.png'

def renderBars(screen, currentDirectory):
    friendly1HealthBarSprite = pygame.image.load(createBarSpritesheet(currentDirectory, int(statsCharacter['friendly1'][0]['health']/2), 'friendly', 'Health'))
    friendly1ManaBarSprite = pygame.image.load(createBarSpritesheet(currentDirectory, int(statsCharacter['friendly1'][1]['mana']/2), 'friendly', 'Mana'))
    friendly1StaminaBarSprite = pygame.image.load(createBarSpritesheet(currentDirectory, int(statsCharacter['friendly1'][2]['stamina']), 'friendly', 'Stamina'))
    friendly2HealthBarSprite = pygame.image.load(createBarSpritesheet(currentDirectory, int(statsCharacter['friendly2'][0]['health']/2), 'friendly', 'Health'))
    friendly2ManaBarSprite = pygame.image.load(createBarSpritesheet(currentDirectory, int(statsCharacter['friendly2'][1]['mana']/2), 'friendly', 'Mana'))
    friendly2StaminaBarSprite = pygame.image.load(createBarSpritesheet(currentDirectory, int(statsCharacter['friendly2'][2]['stamina']), 'friendly', 'Stamina'))
    friendly3HealthBarSprite = pygame.image.load(createBarSpritesheet(currentDirectory, int(statsCharacter['friendly3'][0]['health']/2), 'friendly', 'Health'))
    friendly3ManaBarSprite = pygame.image.load(createBarSpritesheet(currentDirectory, int(statsCharacter['friendly3'][1]['mana']/2), 'friendly', 'Mana'))
    friendly3StaminaBarSprite = pygame.image.load(createBarSpritesheet(currentDirectory, int(statsCharacter['friendly3'][2]['stamina']), 'friendly', 'Stamina'))
    enemy1HealthBarSprite = pygame.image.load(createBarSpritesheet(currentDirectory, int(statsCharacter['enemy1'][0]['health']/2), 'enemy', 'Health'))
    enemy1ManaBarSprite = pygame.image.load(createBarSpritesheet(currentDirectory, int(statsCharacter['enemy1'][1]['mana']/2), 'enemy', 'Mana'))
    enemy1StaminaBarSprite = pygame.image.load(createBarSpritesheet(currentDirectory, int(statsCharacter['enemy1'][2]['stamina']), 'enemy', 'Stamina'))
    enemy2HealthBarSprite = pygame.image.load(createBarSpritesheet(currentDirectory, int(statsCharacter['enemy2'][0]['health']/2), 'enemy', 'Health'))
    enemy2ManaBarSprite = pygame.image.load(createBarSpritesheet(currentDirectory, int(statsCharacter['enemy2'][1]['mana']/2), 'enemy', 'Mana'))
    enemy2StaminaBarSprite = pygame.image.load(createBarSpritesheet(currentDirectory, int(statsCharacter['enemy2'][2]['stamina']), 'enemy', 'Stamina'))
    enemy3HealthBarSprite = pygame.image.load(createBarSpritesheet(currentDirectory, int(statsCharacter['enemy3'][0]['health']/2), 'enemy', 'Health'))
    enemy3ManaBarSprite = pygame.image.load(createBarSpritesheet(currentDirectory, int(statsCharacter['enemy3'][1]['mana']/2), 'enemy', 'Mana'))
    enemy3StaminaBarSprite = pygame.image.load(createBarSpritesheet(currentDirectory, int(statsCharacter['enemy3'][2]['stamina']), 'enemy', 'Stamina'))
    screen.blit(friendly1HealthBarSprite, (1060, 812))
    screen.blit(friendly1ManaBarSprite, (1060, 836))
    screen.blit(friendly1StaminaBarSprite, (1060, 860))
    screen.blit(friendly2HealthBarSprite, (1060, 900))
    screen.blit(friendly2ManaBarSprite, (1060, 924))
    screen.blit(friendly2StaminaBarSprite, (1060, 948))
    screen.blit(friendly3HealthBarSprite, (1060, 988))
    screen.blit(friendly3ManaBarSprite, (1060, 1012))
    screen.blit(friendly3StaminaBarSprite, (1060, 1036))
    screen.blit(enemy1HealthBarSprite, (1620, 812))
    screen.blit(enemy1ManaBarSprite, (1620, 836))
    screen.blit(enemy1StaminaBarSprite, (1620, 860))
    screen.blit(enemy2HealthBarSprite, (1620, 900))
    screen.blit(enemy2ManaBarSprite, (1620, 924))
    screen.blit(enemy2StaminaBarSprite, (1620, 948))
    screen.blit(enemy3HealthBarSprite, (1620, 988))
    screen.blit(enemy3ManaBarSprite, (1620, 1012))
    screen.blit(enemy3StaminaBarSprite, (1620, 1036))

def checkTileStatus(mousePosition, tileSprites, topLeftX, topLeftY, bottomRightX, bottomRightY):
    if (mousePosition[0] >= topLeftX and mousePosition[0] <= bottomRightX and mousePosition[1] >= topLeftY and mousePosition[1] <= bottomRightY):
        return tileSprites[1]
    return tileSprites[0]

def renderTiles(screen, currentDirectory):
    mousePosition = pygame.mouse.get_pos()
    #friendlyside
    tile1 = pygame.image.load(currentDirectory + checkTileStatus(mousePosition, tileSprites, 20, 392, 196, 588))
    tile2 = pygame.image.load(currentDirectory + checkTileStatus(mousePosition, tileSprites, 20, 592, 196, 788))
    tile3 = pygame.image.load(currentDirectory + checkTileStatus(mousePosition, tileSprites, 204, 392, 380, 508))
    tile4 = pygame.image.load(currentDirectory + checkTileStatus(mousePosition, tileSprites, 204, 516, 380, 660))
    tile5 = pygame.image.load(currentDirectory + checkTileStatus(mousePosition, tileSprites, 204, 668, 380, 788))
    tile6 = pygame.image.load(currentDirectory + checkTileStatus(mousePosition, tileSprites, 388, 392, 564, 508))
    tile7 = pygame.image.load(currentDirectory + checkTileStatus(mousePosition, tileSprites, 388, 516, 564, 660))
    tile8 = pygame.image.load(currentDirectory + checkTileStatus(mousePosition, tileSprites, 388, 668, 564, 788))
    tile9 = pygame.image.load(currentDirectory + checkTileStatus(mousePosition, tileSprites, 572, 392, 740, 508))
    tile10 = pygame.image.load(currentDirectory + checkTileStatus(mousePosition, tileSprites, 572, 516, 740, 660))
    tile11 = pygame.image.load(currentDirectory + checkTileStatus(mousePosition, tileSprites, 572, 668, 740, 788))
    tile12 = pygame.image.load(currentDirectory + checkTileStatus(mousePosition, tileSprites, 756, 392, 932, 588))
    tile13 = pygame.image.load(currentDirectory + checkTileStatus(mousePosition, tileSprites, 756, 592, 932, 788))
    #enemyside
    tile14 = pygame.image.load(currentDirectory + checkTileStatus(mousePosition, tileSprites, 984, 392, 1160, 588))
    tile15 = pygame.image.load(currentDirectory + checkTileStatus(mousePosition, tileSprites, 984, 592, 1160, 788))
    tile16 = pygame.image.load(currentDirectory + checkTileStatus(mousePosition, tileSprites, 1168, 392, 1344, 508))
    tile17 = pygame.image.load(currentDirectory + checkTileStatus(mousePosition, tileSprites, 1168, 516, 1344, 660))
    tile18 = pygame.image.load(currentDirectory + checkTileStatus(mousePosition, tileSprites, 1168, 668, 1344, 788))
    tile19 = pygame.image.load(currentDirectory + checkTileStatus(mousePosition, tileSprites, 1352, 392, 1528, 508))
    tile20 = pygame.image.load(currentDirectory + checkTileStatus(mousePosition, tileSprites, 1352, 516, 1528, 660))
    tile21 = pygame.image.load(currentDirectory + checkTileStatus(mousePosition, tileSprites, 1352, 668, 1528, 788))
    tile22 = pygame.image.load(currentDirectory + checkTileStatus(mousePosition, tileSprites, 1536, 392, 1712, 508))
    tile23 = pygame.image.load(currentDirectory + checkTileStatus(mousePosition, tileSprites, 1536, 516, 1712, 660))
    tile24 = pygame.image.load(currentDirectory + checkTileStatus(mousePosition, tileSprites, 1536, 668, 1712, 788))
    tile25 = pygame.image.load(currentDirectory + checkTileStatus(mousePosition, tileSprites, 1720, 392, 1896, 588))
    tile26 = pygame.image.load(currentDirectory + checkTileStatus(mousePosition, tileSprites, 1720, 592, 1896, 788))
    #friendlyside
    screen.blit(tile1, (80, 464))
    screen.blit(tile2, (80, 668))
    screen.blit(tile3, (264, 412))
    screen.blit(tile4, (264, 564))
    screen.blit(tile5, (264, 716))
    screen.blit(tile6, (448, 412))
    screen.blit(tile7, (448, 564))
    screen.blit(tile8, (448, 716))
    screen.blit(tile9, (632, 412))
    screen.blit(tile10, (632, 564))
    screen.blit(tile11, (632, 716))
    screen.blit(tile12, (816, 464))
    screen.blit(tile13, (816, 668))
    #enemyside
    screen.blit(tile14, (1044, 464))
    screen.blit(tile15, (1044, 668))
    screen.blit(tile16, (1228, 412))
    screen.blit(tile17, (1228, 564))
    screen.blit(tile18, (1228, 716))
    screen.blit(tile19, (1412, 412))
    screen.blit(tile20, (1412, 564))
    screen.blit(tile21, (1412, 716))
    screen.blit(tile22, (1596, 412))
    screen.blit(tile23, (1596, 564))
    screen.blit(tile24, (1596, 716))
    screen.blit(tile25, (1780, 464))
    screen.blit(tile26, (1780, 668))

def renderPortaits(screen, currentDirectory):
    friendly1PortraitSprite = pygame.image.load(currentDirectory + '/images/menu/blueMenu/friendlyPortrait/portrait1.png')
    friendly2PortraitSprite = pygame.image.load(currentDirectory + '/images/menu/blueMenu/friendlyPortrait/portrait1.png')
    friendly3PortraitSprite = pygame.image.load(currentDirectory + '/images/menu/blueMenu/friendlyPortrait/portrait1.png')
    enemy1PortraitSprite = pygame.image.load(currentDirectory + '/images/menu/blueMenu/enemyPortrait/portrait1.png')
    enemy2PortraitSprite = pygame.image.load(currentDirectory + '/images/menu/blueMenu/enemyPortrait/portrait1.png')
    enemy3PortraitSprite = pygame.image.load(currentDirectory + '/images/menu/blueMenu/enemyPortrait/portrait1.png')
    screen.blit(friendly1PortraitSprite, (980, 808))
    screen.blit(friendly2PortraitSprite, (980, 896))
    screen.blit(friendly3PortraitSprite, (980, 984))
    screen.blit(enemy1PortraitSprite, (1828, 808))
    screen.blit(enemy2PortraitSprite, (1828, 896))
    screen.blit(enemy3PortraitSprite, (1828, 984))

def renderCharacters(screen, currentDirectory):
    for i in range(1, 4):
        if statsCharacter['friendly' + str(i)][11]['action'] == 'none':
            friendly1CharacterSprite = pygame.image.load(currentDirectory + '/images/character/friendlyIdle/idle' + str(statsCharacter['friendly' + str(i)][12]['spriteNum']) + '.png')
            screen.blit(friendly1CharacterSprite, (statsCharacter['friendly' + str(i)][13]['currentX'], statsCharacter['friendly' + str(i)][14]['currentY']))
            if statsCharacter['friendly' + str(i)][12]['spriteNum'] == 5:
                statsCharacter['friendly' + str(i)][12]['spriteNum'] = 1
            else:
                statsCharacter['friendly' + str(i)][12]['spriteNum'] += 1
    for i in range(1, 4):
        if statsCharacter['enemy' + str(i)][11]['action'] == 'none':
            friendly1CharacterSprite = pygame.image.load(currentDirectory + '/images/character/enemyIdle/idle' + str(statsCharacter['enemy' + str(i)][12]['spriteNum']) + '.png')
            screen.blit(friendly1CharacterSprite, (statsCharacter['enemy' + str(i)][13]['currentX'], statsCharacter['enemy' + str(i)][14]['currentY']))
            if statsCharacter['enemy' + str(i)][12]['spriteNum'] == 5:
                statsCharacter['enemy' + str(i)][12]['spriteNum'] = 1
            else:
                statsCharacter['enemy' + str(i)][12]['spriteNum'] += 1

def renderMenus(screen, currentDirectory):
    renderMenuFrame(screen, currentDirectory)
    renderButtons(screen, currentDirectory)
    renderPortaits(screen, currentDirectory)
    renderBars(screen, currentDirectory)


def renderGame(screen):
    currentDirectory = getDirectory()
    screen.fill((255, 255, 255)) #white
    renderSky(screen, currentDirectory)
    renderGround(screen, currentDirectory)
    renderMenus(screen, currentDirectory)
    renderTiles(screen, currentDirectory)
    renderCharacters(screen, currentDirectory)
    pygame.display.flip()
