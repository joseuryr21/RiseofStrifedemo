#draws images and such
import pygame
import os
from model.gamedata import takeHit

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


def renderPortaits(screen, currentDirectory):
    friendly1PortraitSprite = pygame.image.load(currentDirectory + '/images/menu/blueMenu/friendlyPortrait/portrait1.png')
    screen.blit(friendly1PortraitSprite, (980, 808))

def renderMenus(screen, currentDirectory):
    renderMenuFrame(screen, currentDirectory)
    renderButtons(screen, currentDirectory)
    renderPortaits(screen, currentDirectory)

def renderGame(screen):
    currentDirectory = getDirectory()
    screen.fill((255, 255, 255)) #white
    renderSky(screen, currentDirectory)
    renderGround(screen, currentDirectory)
    renderMenus(screen, currentDirectory)
    pygame.display.flip()
