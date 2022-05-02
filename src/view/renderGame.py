#draws images and such
import pygame
import os
from model.gamedata import statsCharacter

tileSprites = ["/images/terrain/tileNormal.png", "/images/terrain/tileSelected.png", "/images/terrain/tileAttacked.png", "/images/terrain/tileHealed.png", "/images/terrain/tileLingered.png"]

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

def renderTiles(screen, currentDirectory):
    mousePosition = pygame.mouse.get_pos()

    #friendlyside
    tile1 = pygame.image.load(currentDirectory + tileSprites[0])
    tile2 = pygame.image.load(currentDirectory + tileSprites[0])
    tile3 = pygame.image.load(currentDirectory + tileSprites[0])
    tile4 = pygame.image.load(currentDirectory + tileSprites[0])
    tile5 = pygame.image.load(currentDirectory + tileSprites[0])
    tile6 = pygame.image.load(currentDirectory + tileSprites[0])
    tile7 = pygame.image.load(currentDirectory + tileSprites[0])
    tile8 = pygame.image.load(currentDirectory + tileSprites[0])
    tile9 = pygame.image.load(currentDirectory + tileSprites[0])
    tile10 = pygame.image.load(currentDirectory + tileSprites[0])
    tile11 = pygame.image.load(currentDirectory + tileSprites[0])
    tile12 = pygame.image.load(currentDirectory + tileSprites[0])
    tile13 = pygame.image.load(currentDirectory + tileSprites[0])
    #enemyside
    tile14 = pygame.image.load(currentDirectory + tileSprites[0])
    tile15 = pygame.image.load(currentDirectory + tileSprites[0])
    tile16 = pygame.image.load(currentDirectory + tileSprites[0])
    tile17 = pygame.image.load(currentDirectory + tileSprites[0])
    tile18 = pygame.image.load(currentDirectory + tileSprites[0])
    tile19 = pygame.image.load(currentDirectory + tileSprites[0])
    tile20 = pygame.image.load(currentDirectory + tileSprites[0])
    tile21 = pygame.image.load(currentDirectory + tileSprites[0])
    tile22 = pygame.image.load(currentDirectory + tileSprites[0])
    tile23 = pygame.image.load(currentDirectory + tileSprites[0])
    tile24 = pygame.image.load(currentDirectory + tileSprites[0])
    tile25 = pygame.image.load(currentDirectory + tileSprites[0])
    tile26 = pygame.image.load(currentDirectory + tileSprites[0])
    #friendlyside
    screen.blit(tile1, (80, 464)) #TL: 20, 392 --BR: 196, 588| -60, -72 -- +116, +124
    screen.blit(tile2, (80, 668)) #TL: 20, 592 --BR: 196, 788
    screen.blit(tile3, (264, 412)) #TL: 204, 392 -- BR: 380, 508| -60, -20 -- +116, +96
    screen.blit(tile4, (264, 564)) #TL: 204, 516 -- BR: 380, 660| -60, -448 -- +116, +96
    screen.blit(tile5, (264, 716)) #TL: 204, 668 -- BR: 380, 788| -60, -48 -- +116, +72
    screen.blit(tile6, (448, 412)) ##TL: 388, 392 -- BR: 564, 508
    screen.blit(tile7, (448, 564)) ##TL: 388, 516 -- BR: 564, 660
    screen.blit(tile8, (448, 716)) ##TL: 388, 668 -- BR: 564, 788
    screen.blit(tile9, (632, 412)) ###TL: 572, 392 -- BR: 740, 508
    screen.blit(tile10, (632, 564)) ###TL: 572, 516 -- BR: 740, 660
    screen.blit(tile11, (632, 716)) ###TL: 572, 668 -- BR: 740, 788
    screen.blit(tile12, (816, 464)) #TL: 756, 392 --BR: 932, 188
    screen.blit(tile13, (816, 668)) #TL: 756, 592 --BR: 932, 788
    #enemyside
    screen.blit(tile14, (1044, 464)) #TL: 984, 392 --BR: 1160, 588
    screen.blit(tile15, (1044, 668)) #TL: 984, 592 --BR: 1160, 788
    screen.blit(tile16, (1228, 412)) #TL: 1168, 392 -- BR: 1344, 508
    screen.blit(tile17, (1228, 564)) #TL: 1168, 516 -- BR: 1344, 660
    screen.blit(tile18, (1228, 716)) #TL: 1168, 668 -- BR: 1344, 788
    screen.blit(tile19, (1412, 412)) ##TL: 1352, 392 -- BR: 1528, 508
    screen.blit(tile20, (1412, 564)) ##TL: 1352, 516 -- BR: 1528, 660
    screen.blit(tile21, (1412, 716)) ##TL: 1352, 668 -- BR: 1528, 788
    screen.blit(tile22, (1596, 412)) ###TL: 1536, 392 -- BR: 1712, 508
    screen.blit(tile23, (1596, 564)) ###TL: 1536, 516 -- BR: 1712, 660
    screen.blit(tile24, (1596, 716)) ###TL: 1536, 668 -- BR: 1712, 788
    screen.blit(tile25, (1780, 464)) #TL: 1720, 392 --BR: 1896, 588
    screen.blit(tile26, (1780, 668)) #TL: 1720, 392 --BR: 1896, 588

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
    pygame.display.flip()
