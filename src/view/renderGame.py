#draws images and such
import pygame
import os

tileSprites = ["/images/terrain/tileNormal.png", "/images/terrain/tileSelected.png", "/images/terrain/tileAttacked.png", "/images/terrain/tileHealed.png", "/images/terrain/tileLingered.png"]
tilePositions = [[80, 464], [80, 668], [264, 412], [264, 564], [264, 716], [448, 412], [448, 564], [448, 716], [632, 412], [632, 564], [632, 716], [816, 464], [816, 668], [1044, 464], [1044, 668], [1228, 412], [1228, 564], [1228, 716], [1412, 412], [1412, 564], [1412, 716], [1596, 412], [1596, 564], [1596, 716], [1780, 464], [1780, 668]]
tileHoverPositions = [[20, 392, 196, 588], [20, 592, 196, 788], [204, 392, 380, 508], [204, 516, 380, 660], [204, 668, 380, 788], [388, 392, 564, 508], [388, 516, 564, 660], [388, 668, 564, 788], [572, 392, 740, 508], [572, 516, 740, 660], [572, 668, 740, 788], [756, 392, 932, 588], [756, 592, 932, 788], [984, 392, 1160, 588], [984, 592, 1160, 788], [1168, 392, 1344, 508], [1168, 516, 1344, 660], [1168, 668, 1344, 788], [1352, 392, 1528, 508], [1352, 516, 1528, 660], [1352, 668, 1528, 788], [1536, 392, 1712, 508], [1536, 516, 1712, 660], [1536, 668, 1712, 788], [1720, 392, 1896, 588], [1720, 592, 1896, 788]]
effectPositions = [[[1268, 812], [1268, 848], [1308, 848]], [[1268, 900], [1268, 936], [1308, 936]], [[1268, 988], [1268, 1024], [1308, 1024]], [[1580, 812], [1580, 848], [1540, 848]], [[1580, 900], [1580, 936], [1540, 936]], [[1580, 988], [1580, 1024], [1540, 1024]]]
portraitPositions = [[980, 808], [980, 896], [980, 984], [1828, 808], [1828, 896], [1828, 984]]

from model.gamedata import statsCharacter

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
    if currentMenu() == 'main':
        attackSprite = pygame.image.load(currentDirectory + '/images/menu/grayMenu/mainbuttons/Attack1.png')
        screen.blit(attackSprite, (28, 824))
        defendSprite = pygame.image.load(currentDirectory + '/images/menu/grayMenu/mainbuttons/Defend1.png')
        screen.blit(defendSprite, (428, 824))
        specialSprite = pygame.image.load(currentDirectory + '/images/menu/grayMenu/mainbuttons/Special1.png')
        screen.blit(specialSprite, (28, 948))
        relocateSprite = pygame.image.load(currentDirectory + '/images/menu/grayMenu/mainbuttons/Relocate2.png')
        screen.blit(relocateSprite, (428, 948))
    backSprite = pygame.image.load(currentDirectory + '/images/menu/grayMenu/mainbuttons/Back1.png')
    screen.blit(backSprite, (828, 824))
    exitSprite = pygame.image.load(currentDirectory + '/images/menu/Exit1.png')
    screen.blit(exitSprite, (1840, 0))

def createBarSpritesheet(currentDirectory, index, characterType, statType):
    return (currentDirectory) + '/images/menu/blueMenu/' + characterType + statType + '/' + statType.lower() + str(index) + '.png'

def renderBars(screen, currentDirectory):
    friendly1HealthBarSprite = pygame.image.load(createBarSpritesheet(currentDirectory, int(statsCharacter['friendly1']['health']/2), 'friendly', 'Health'))
    friendly1ManaBarSprite = pygame.image.load(createBarSpritesheet(currentDirectory, int(statsCharacter['friendly1']['mana']/2), 'friendly', 'Mana'))
    friendly1StaminaBarSprite = pygame.image.load(createBarSpritesheet(currentDirectory, int(statsCharacter['friendly1']['stamina']), 'friendly', 'Stamina'))
    friendly2HealthBarSprite = pygame.image.load(createBarSpritesheet(currentDirectory, int(statsCharacter['friendly2']['health']/2), 'friendly', 'Health'))
    friendly2ManaBarSprite = pygame.image.load(createBarSpritesheet(currentDirectory, int(statsCharacter['friendly2']['mana']/2), 'friendly', 'Mana'))
    friendly2StaminaBarSprite = pygame.image.load(createBarSpritesheet(currentDirectory, int(statsCharacter['friendly2']['stamina']), 'friendly', 'Stamina'))
    friendly3HealthBarSprite = pygame.image.load(createBarSpritesheet(currentDirectory, int(statsCharacter['friendly3']['health']/2), 'friendly', 'Health'))
    friendly3ManaBarSprite = pygame.image.load(createBarSpritesheet(currentDirectory, int(statsCharacter['friendly3']['mana']/2), 'friendly', 'Mana'))
    friendly3StaminaBarSprite = pygame.image.load(createBarSpritesheet(currentDirectory, int(statsCharacter['friendly3']['stamina']), 'friendly', 'Stamina'))
    enemy1HealthBarSprite = pygame.image.load(createBarSpritesheet(currentDirectory, int(statsCharacter['enemy1']['health']/2), 'enemy', 'Health'))
    enemy1ManaBarSprite = pygame.image.load(createBarSpritesheet(currentDirectory, int(statsCharacter['enemy1']['mana']/2), 'enemy', 'Mana'))
    enemy1StaminaBarSprite = pygame.image.load(createBarSpritesheet(currentDirectory, int(statsCharacter['enemy1']['stamina']), 'enemy', 'Stamina'))
    enemy2HealthBarSprite = pygame.image.load(createBarSpritesheet(currentDirectory, int(statsCharacter['enemy2']['health']/2), 'enemy', 'Health'))
    enemy2ManaBarSprite = pygame.image.load(createBarSpritesheet(currentDirectory, int(statsCharacter['enemy2']['mana']/2), 'enemy', 'Mana'))
    enemy2StaminaBarSprite = pygame.image.load(createBarSpritesheet(currentDirectory, int(statsCharacter['enemy2']['stamina']), 'enemy', 'Stamina'))
    enemy3HealthBarSprite = pygame.image.load(createBarSpritesheet(currentDirectory, int(statsCharacter['enemy3']['health']/2), 'enemy', 'Health'))
    enemy3ManaBarSprite = pygame.image.load(createBarSpritesheet(currentDirectory, int(statsCharacter['enemy3']['mana']/2), 'enemy', 'Mana'))
    enemy3StaminaBarSprite = pygame.image.load(createBarSpritesheet(currentDirectory, int(statsCharacter['enemy3']['stamina']), 'enemy', 'Stamina'))
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

# if mouse inside boundaries, return img of a black tile
def checkHoverStatus(mousePosition, tileSprites, topLeftX, topLeftY, bottomRightX, bottomRightY):
    if (mousePosition[0] >= topLeftX and mousePosition[0] <= bottomRightX and mousePosition[1] >= topLeftY and mousePosition[1] <= bottomRightY):
        return tileSprites[1]
    return tileSprites[0]

def renderTiles(screen, currentDirectory):
    mousePosition = pygame.mouse.get_pos()
    for i in range(0, 26):
        tile = pygame.image.load(currentDirectory + checkHoverStatus(mousePosition, tileSprites, tileHoverPositions[i][0], tileHoverPositions[i][1], tileHoverPositions[i][2], tileHoverPositions[i][3]))
        screen.blit(tile, (tilePositions[i][0], tilePositions[i][1]))

def renderPortaits(screen, currentDirectory):
    mousePosition = pygame.mouse.get_pos()
    # if tile character is on is higlighted, portrait frame becomes black
    for i in range(1, 4):
        if (checkHoverStatus(mousePosition, tileSprites, tileHoverPositions[statsCharacter['friendly' + str(i)]['currentTile'] - 1][0], tileHoverPositions[statsCharacter['friendly' + str(i)]['currentTile'] - 1][1], tileHoverPositions[statsCharacter['friendly' + str(i)]['currentTile'] - 1][2], tileHoverPositions[statsCharacter['friendly' + str(i)]['currentTile'] - 1][3]) == tileSprites[1]):
            friendlyPortraitSprite = pygame.image.load(currentDirectory + '/images/menu/blueMenu/friendlyPortrait/portrait2.png')
            screen.blit(friendlyPortraitSprite, (portraitPositions[i - 1][0], portraitPositions[i - 1][1]))
        else:
            friendlyPortraitSprite = pygame.image.load(currentDirectory + '/images/menu/blueMenu/friendlyPortrait/portrait1.png')
            screen.blit(friendlyPortraitSprite, (portraitPositions[i - 1][0], portraitPositions[i - 1][1]))
    for i in range(1, 4):
        if (checkHoverStatus(mousePosition, tileSprites, tileHoverPositions[statsCharacter['enemy' + str(i)]['currentTile'] - 1][0], tileHoverPositions[statsCharacter['enemy' + str(i)]['currentTile'] - 1][1], tileHoverPositions[statsCharacter['enemy' + str(i)]['currentTile'] - 1][2], tileHoverPositions[statsCharacter['enemy' + str(i)]['currentTile'] - 1][3]) == tileSprites[1]):
            enemyPortraitSprite = pygame.image.load(currentDirectory + '/images/menu/blueMenu/enemyPortrait/portrait2.png')
            screen.blit(enemyPortraitSprite, (portraitPositions[i + 2][0], portraitPositions[i + 2][1]))
        else:
            enemyPortraitSprite = pygame.image.load(currentDirectory + '/images/menu/blueMenu/enemyPortrait/portrait1.png')
            screen.blit(enemyPortraitSprite, (portraitPositions[i + 2][0], portraitPositions[i + 2][1]))


def renderCharacters(screen, currentDirectory):
    #if characters are at the last animation frame, reset
    for i in range(1, 4):
        if statsCharacter['friendly' + str(i)]['action'] == 'none':
            friendly1CharacterSprite = pygame.image.load(currentDirectory + '/images/character/friendlyIdle/idle' + str(statsCharacter['friendly' + str(i)]['spriteNum']) + '.png')
            screen.blit(friendly1CharacterSprite, (tilePositions[statsCharacter['friendly' + str(i)]['currentTile'] - 1][0] - 36, tilePositions[statsCharacter['friendly' + str(i)]['currentTile'] - 1][1] - 104)) #-36, -104 alligns friendly character properly on tile
            if statsCharacter['friendly' + str(i)]['spriteNum'] == 5: #max idle sprite
                statsCharacter['friendly' + str(i)]['spriteNum'] = 1
            else:
                statsCharacter['friendly' + str(i)]['spriteNum'] += 1
    for i in range(1, 4):
        if statsCharacter['enemy' + str(i)]['action'] == 'none':
            friendly1CharacterSprite = pygame.image.load(currentDirectory + '/images/character/enemyIdle/idle' + str(statsCharacter['enemy' + str(i)]['spriteNum']) + '.png')
            screen.blit(friendly1CharacterSprite, (tilePositions[statsCharacter['enemy' + str(i)]['currentTile'] - 1][0] - 40, tilePositions[statsCharacter['enemy' + str(i)]['currentTile'] - 1][1] - 104)) #-40, -104 alligns enemy character properly on tile
            if statsCharacter['enemy' + str(i)]['spriteNum'] == 5: #max idle sprite
                statsCharacter['enemy' + str(i)]['spriteNum'] = 1
            else:
                statsCharacter['enemy' + str(i)]['spriteNum'] += 1

def renderEffects(screen, currentDirectory):
    for i in range(1, 4):
        if statsCharacter['friendly' + str(i)]['buff1'][0] != 'none':
            friendlyBuff1Sprite = pygame.image.load(currentDirectory + '/images/menu/blueMenu/buffs/' + statsCharacter['friendly' + str(i)]['buff1'][0] + '.png')
            screen.blit(friendlyBuff1Sprite, (effectPositions[i - 1][0][0], effectPositions[i - 1][0][1]))
        if statsCharacter['friendly' + str(i)]['debuff1'][0] != 'none':
            friendlyDebuff1Sprite = pygame.image.load(currentDirectory + '/images/menu/blueMenu/debuffs/' + statsCharacter['friendly' + str(i)]['debuff1'][0] + '.png')
            screen.blit(friendlyDebuff1Sprite, (effectPositions[i - 1][1][0], effectPositions[i - 1][1][1]))
        if statsCharacter['friendly' + str(i)]['debuff2'][0] != 'none':
            friendlyDebuff2Sprite = pygame.image.load(currentDirectory + '/images/menu/blueMenu/debuffs/' + statsCharacter['friendly' + str(i)]['debuff2'][0] + '.png')
            screen.blit(friendlyDebuff2Sprite, (effectPositions[i - 1][2][0], effectPositions[i - 1][2][1]))
    for i in range(1, 4):
        if statsCharacter['enemy' + str(i)]['buff1'][0] != 'none':
            enemyBuff1Sprite = pygame.image.load(currentDirectory + '/images/menu/blueMenu/buffs/' + statsCharacter['enemy' + str(i)]['buff1'][0] + '.png')
            screen.blit(enemyBuff1Sprite, (effectPositions[i + 2][0][0], effectPositions[i + 2][0][1]))
        if statsCharacter['enemy' + str(i)]['debuff1'][0] != 'none':
            enemyDebuff1Sprite = pygame.image.load(currentDirectory + '/images/menu/blueMenu/debuffs/' + statsCharacter['enemy' + str(i)]['debuff1'][0] + '.png')
            screen.blit(enemyDebuff1Sprite, (effectPositions[i + 2][1][0], effectPositions[i + 2][1][1]))
        if statsCharacter['enemy' + str(i)]['debuff2'][0] != 'none':
            enemyDebuff2Sprite = pygame.image.load(currentDirectory + '/images/menu/blueMenu/debuffs/' + statsCharacter['enemy' + str(i)]['debuff2'][0] + '.png')
            screen.blit(enemyDebuff2Sprite, (effectPositions[i + 2][2][0], effectPositions[i + 2][2][1]))

def renderMenus(screen, currentDirectory):
    renderMenuFrame(screen, currentDirectory)
    renderButtons(screen, currentDirectory)
    renderPortaits(screen, currentDirectory)
    renderBars(screen, currentDirectory)
    renderEffects(screen, currentDirectory)

def renderGame(screen):
    currentDirectory = getDirectory()
    renderSky(screen, currentDirectory)
    renderGround(screen, currentDirectory)
    renderTiles(screen, currentDirectory)
    renderMenus(screen, currentDirectory)
    renderCharacters(screen, currentDirectory)
    pygame.display.flip()
