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
    menuFrameSprite = pygame.image.load(currentDirectory + '/images/menu/menuframe/MenuFrame1.png')
    screen.blit(menuFrameSprite, (0, 792)) #792 is below ground

def renderMenus(screen, currentDirectory):
    renderMenuFrame(screen, currentDirectory)


def renderGame(screen):
    currentDirectory = getDirectory()
    screen.fill((255, 255, 255)) #white
    renderSky(screen, currentDirectory)
    renderGround(screen, currentDirectory)
    renderMenus(screen, currentDirectory)
    pygame.display.flip()
    screen.fill((255, 255, 255)) #white
