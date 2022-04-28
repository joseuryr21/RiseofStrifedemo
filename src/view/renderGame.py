#draws images and such
import pygame
import os
from model.gamedata import takeHit

currentDirectory = str(os.getcwd())
spritesheetMenuBars = {
    "friendlyHealth": [
    {"0": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health0.png'},
    {"1": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health1.png'},
    {"2": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health2.png'},
    {"3": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health3.png'},
    {"4": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health4.png'},
    {"5": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health5.png'},
    {"6": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health6.png'},
    {"7": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health7.png'},
    {"8": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health8.png'},
    {"9": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health9.png'},
    {"10": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health10.png'},
    {"11": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health11.png'},
    {"12": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health12.png'},
    {"13": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health13.png'},
    {"14": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health14.png'},
    {"15": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health15.png'},
    {"16": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health16.png'},
    {"17": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health17.png'},
    {"18": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health18.png'},
    {"19": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health19.png'},
    {"20": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health20.png'},
    {"21": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health21.png'},
    {"22": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health22.png'},
    {"23": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health23.png'},
    {"24": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health24.png'},
    {"25": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health25.png'},
    {"26": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health26.png'},
    {"27": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health27.png'},
    {"28": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health28.png'},
    {"29": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health29.png'},
    {"30": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health30.png'},
    {"31": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health31.png'},
    {"32": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health32.png'},
    {"33": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health33.png'},
    {"34": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health34.png'},
    {"35": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health35.png'},
    {"36": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health36.png'},
    {"37": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health37.png'},
    {"38": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health38.png'},
    {"39": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health39.png'},
    {"40": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health40.png'},
    {"41": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health41.png'},
    {"42": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health42.png'},
    {"43": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health43.png'},
    {"44": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health44.png'},
    {"45": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health45.png'},
    {"46": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health46.png'},
    {"47": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health47.png'},
    {"48": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health48.png'},
    {"49": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health49.png'},
    {"50": (currentDirectory) + '/images/menu/blueMenu/friendlyHealth/health50.png'}
    ],

    "friendlyMana": [
    {"0": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana0.png'},
    {"1": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana1.png'},
    {"2": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana2.png'},
    {"3": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana3.png'},
    {"4": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana4.png'},
    {"5": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana5.png'},
    {"6": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana6.png'},
    {"7": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana7.png'},
    {"8": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana8.png'},
    {"9": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana9.png'},
    {"10": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana10.png'},
    {"11": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana11.png'},
    {"12": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana12.png'},
    {"13": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana13.png'},
    {"14": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana14.png'},
    {"15": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana15.png'},
    {"16": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana16.png'},
    {"17": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana17.png'},
    {"18": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana18.png'},
    {"19": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana19.png'},
    {"20": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana20.png'},
    {"21": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana21.png'},
    {"22": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana22.png'},
    {"23": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana23.png'},
    {"24": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana24.png'},
    {"25": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana25.png'},
    {"26": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana26.png'},
    {"27": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana27.png'},
    {"28": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana28.png'},
    {"29": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana29.png'},
    {"30": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana30.png'},
    {"31": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana31.png'},
    {"32": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana32.png'},
    {"33": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana33.png'},
    {"34": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana34.png'},
    {"35": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana35.png'},
    {"36": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana36.png'},
    {"37": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana37.png'},
    {"38": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana38.png'},
    {"39": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana39.png'},
    {"40": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana40.png'},
    {"41": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana41.png'},
    {"42": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana42.png'},
    {"43": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana43.png'},
    {"44": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana44.png'},
    {"45": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana45.png'},
    {"46": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana46.png'},
    {"47": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana47.png'},
    {"48": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana48.png'},
    {"49": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana49.png'},
    {"50": (currentDirectory) + '/images/menu/blueMenu/friendlyMana/mana50.png'}
    ],

    "friendlyStamina": [
    {"0": (currentDirectory) + '/images/menu/blueMenu/friendlyStamina/stamina0.png'},
    {"1": (currentDirectory) + '/images/menu/blueMenu/friendlyStamina/stamina1.png'},
    {"2": (currentDirectory) + '/images/menu/blueMenu/friendlyStamina/stamina2.png'},
    {"3": (currentDirectory) + '/images/menu/blueMenu/friendlyStamina/stamina3.png'}
    ],

    "enemyHealth": [
    {"0": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health0.png'},
    {"1": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health1.png'},
    {"2": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health2.png'},
    {"3": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health3.png'},
    {"4": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health4.png'},
    {"5": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health5.png'},
    {"6": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health6.png'},
    {"7": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health7.png'},
    {"8": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health8.png'},
    {"9": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health9.png'},
    {"10": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health10.png'},
    {"11": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health11.png'},
    {"12": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health12.png'},
    {"13": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health13.png'},
    {"14": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health14.png'},
    {"15": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health15.png'},
    {"16": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health16.png'},
    {"17": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health17.png'},
    {"18": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health18.png'},
    {"19": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health19.png'},
    {"20": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health20.png'},
    {"21": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health21.png'},
    {"22": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health22.png'},
    {"23": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health23.png'},
    {"24": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health24.png'},
    {"25": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health25.png'},
    {"26": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health26.png'},
    {"27": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health27.png'},
    {"28": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health28.png'},
    {"29": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health29.png'},
    {"30": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health30.png'},
    {"31": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health31.png'},
    {"32": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health32.png'},
    {"33": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health33.png'},
    {"34": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health34.png'},
    {"35": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health35.png'},
    {"36": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health36.png'},
    {"37": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health37.png'},
    {"38": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health38.png'},
    {"39": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health39.png'},
    {"40": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health40.png'},
    {"41": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health41.png'},
    {"42": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health42.png'},
    {"43": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health43.png'},
    {"44": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health44.png'},
    {"45": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health45.png'},
    {"46": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health46.png'},
    {"47": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health47.png'},
    {"48": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health48.png'},
    {"49": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health49.png'},
    {"50": (currentDirectory) + '/images/menu/blueMenu/enemyHealth/health50.png'}
    ],

    "enemyMana": [
    {"0": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana0.png'},
    {"1": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana1.png'},
    {"2": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana2.png'},
    {"3": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana3.png'},
    {"4": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana4.png'},
    {"5": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana5.png'},
    {"6": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana6.png'},
    {"7": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana7.png'},
    {"8": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana8.png'},
    {"9": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana9.png'},
    {"10": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana10.png'},
    {"11": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana11.png'},
    {"12": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana12.png'},
    {"13": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana13.png'},
    {"14": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana14.png'},
    {"15": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana15.png'},
    {"16": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana16.png'},
    {"17": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana17.png'},
    {"18": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana18.png'},
    {"19": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana19.png'},
    {"20": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana20.png'},
    {"21": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana21.png'},
    {"22": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana22.png'},
    {"23": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana23.png'},
    {"24": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana24.png'},
    {"25": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana25.png'},
    {"26": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana26.png'},
    {"27": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana27.png'},
    {"28": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana28.png'},
    {"29": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana29.png'},
    {"30": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana30.png'},
    {"31": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana31.png'},
    {"32": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana32.png'},
    {"33": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana33.png'},
    {"34": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana34.png'},
    {"35": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana35.png'},
    {"36": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana36.png'},
    {"37": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana37.png'},
    {"38": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana38.png'},
    {"39": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana39.png'},
    {"40": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana40.png'},
    {"41": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana41.png'},
    {"42": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana42.png'},
    {"43": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana43.png'},
    {"44": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana44.png'},
    {"45": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana45.png'},
    {"46": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana46.png'},
    {"47": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana47.png'},
    {"48": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana48.png'},
    {"49": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana49.png'},
    {"50": (currentDirectory) + '/images/menu/blueMenu/enemyMana/mana50.png'}
    ],

    "enemyStamina": [
    {"0": (currentDirectory) + '/images/menu/blueMenu/enemyStamina/stamina0.png'},
    {"1": (currentDirectory) + '/images/menu/blueMenu/enemyStamina/stamina1.png'},
    {"2": (currentDirectory) + '/images/menu/blueMenu/enemyStamina/stamina2.png'},
    {"3": (currentDirectory) + '/images/menu/blueMenu/enemyStamina/stamina3.png'}
    ]
}

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

def renderBars(screen, currentDirectory):
    friendly1HealthBarSprite = pygame.image.load(spritesheetMenuBars['friendlyHealth'][50]['50'])
    friendly1ManaBarSprite = pygame.image.load(spritesheetMenuBars['friendlyMana'][50]['50'])
    friendly1StaminaBarSprite = pygame.image.load(spritesheetMenuBars['friendlyStamina'][3]['3'])
    screen.blit(friendly1HealthBarSprite, (1060, 812))
    screen.blit(friendly1ManaBarSprite, (1060, 836))
    screen.blit(friendly1StaminaBarSprite, (1060, 860))

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
    pygame.display.flip()
