#draws images and such
import pygame
import os

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
    friendly1HealthBarSprite = pygame.image.load(spritesheetMenuBars['friendlyHealth'][int(statsCharacter['friendly1'][0]['health']/2)][str(int(statsCharacter['friendly1'][0]['health']/2))])
    friendly1ManaBarSprite = pygame.image.load(spritesheetMenuBars['friendlyMana'][int(statsCharacter['friendly1'][1]['mana']/2)][str(int(statsCharacter['friendly1'][1]['mana']/2))])
    friendly1StaminaBarSprite = pygame.image.load(spritesheetMenuBars['friendlyStamina'][statsCharacter['friendly1'][2]['stamina']][str(statsCharacter['friendly1'][2]['stamina'])])
    friendly2HealthBarSprite = pygame.image.load(spritesheetMenuBars['friendlyHealth'][int(statsCharacter['friendly2'][0]['health']/2)][str(int(statsCharacter['friendly2'][0]['health']/2))])
    friendly2ManaBarSprite = pygame.image.load(spritesheetMenuBars['friendlyMana'][int(statsCharacter['friendly2'][1]['mana']/2)][str(int(statsCharacter['friendly2'][1]['mana']/2))])
    friendly2StaminaBarSprite = pygame.image.load(spritesheetMenuBars['friendlyStamina'][statsCharacter['friendly2'][2]['stamina']][str(statsCharacter['friendly2'][2]['stamina'])])
    friendly3HealthBarSprite = pygame.image.load(spritesheetMenuBars['friendlyHealth'][int(statsCharacter['friendly3'][0]['health']/2)][str(int(statsCharacter['friendly3'][0]['health']/2))])
    friendly3ManaBarSprite = pygame.image.load(spritesheetMenuBars['friendlyMana'][int(statsCharacter['friendly3'][1]['mana']/2)][str(int(statsCharacter['friendly3'][1]['mana']/2))])
    friendly3StaminaBarSprite = pygame.image.load(spritesheetMenuBars['friendlyStamina'][statsCharacter['friendly3'][2]['stamina']][str(statsCharacter['friendly3'][2]['stamina'])])
    enemy1HealthBarSprite = pygame.image.load(spritesheetMenuBars['enemyHealth'][int(statsCharacter['enemy1'][0]['health']/2)][str(int(statsCharacter['enemy1'][0]['health']/2))])
    enemy1ManaBarSprite = pygame.image.load(spritesheetMenuBars['enemyMana'][int(statsCharacter['enemy1'][1]['mana']/2)][str(int(statsCharacter['enemy1'][1]['mana']/2))])
    enemy1StaminaBarSprite = pygame.image.load(spritesheetMenuBars['enemyStamina'][statsCharacter['enemy1'][2]['stamina']][str(statsCharacter['enemy1'][2]['stamina'])])
    enemy2HealthBarSprite = pygame.image.load(spritesheetMenuBars['enemyHealth'][int(statsCharacter['enemy2'][0]['health']/2)][str(int(statsCharacter['enemy2'][0]['health']/2))])
    enemy2ManaBarSprite = pygame.image.load(spritesheetMenuBars['enemyMana'][int(statsCharacter['enemy2'][1]['mana']/2)][str(int(statsCharacter['enemy2'][1]['mana']/2))])
    enemy2StaminaBarSprite = pygame.image.load(spritesheetMenuBars['enemyStamina'][statsCharacter['enemy2'][2]['stamina']][str(statsCharacter['enemy2'][2]['stamina'])])
    enemy3HealthBarSprite = pygame.image.load(spritesheetMenuBars['enemyHealth'][int(statsCharacter['enemy3'][0]['health']/2)][str(int(statsCharacter['enemy3'][0]['health']/2))])
    enemy3ManaBarSprite = pygame.image.load(spritesheetMenuBars['enemyMana'][int(statsCharacter['enemy3'][1]['mana']/2)][str(int(statsCharacter['enemy3'][1]['mana']/2))])
    enemy3StaminaBarSprite = pygame.image.load(spritesheetMenuBars['enemyStamina'][statsCharacter['enemy3'][2]['stamina']][str(statsCharacter['enemy3'][2]['stamina'])])
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


statsCharacter = {
  "friendly1": [
    {"health": 100},
    {"mana": 50},
    {"stamina": 3},
    {"attack": 20},
    {"magic": 20},
    {"defense": 30},
    {"resistance": 20},
    {"buff1": 'none'},
    {"buff2": 'none'},
    {"debuff1": 'none'},
    {"debuff2": 'none'}
  ],
  "friendly2": [
    {"health": 100},
    {"mana": 50},
    {"stamina": 3},
    {"attack": 20},
    {"magic": 20},
    {"defense": 30},
    {"resistance": 20},
    {"buff1": 'none'},
    {"buff2": 'none'},
    {"debuff1": 'none'},
    {"debuff2": 'none'}
  ],
  "friendly3": [
    {"health": 50},
    {"mana": 20},
    {"stamina": 2},
    {"attack": 20},
    {"magic": 20},
    {"defense": 30},
    {"resistance": 20},
    {"buff1": 'none'},
    {"buff2": 'none'},
    {"debuff1": 'none'},
    {"debuff2": 'none'}
  ],

  "enemy1": [
    {"health": 100},
    {"mana": 50},
    {"stamina": 3},
    {"attack": 20},
    {"magic": 20},
    {"defense": 30},
    {"resistance": 20},
    {"buff1": 'none'},
    {"buff2": 'none'},
    {"debuff1": 'none'},
    {"debuff2": 'none'}
  ],
  "enemy2": [
    {"health": 100},
    {"mana": 50},
    {"stamina": 3},
    {"attack": 20},
    {"magic": 20},
    {"defense": 30},
    {"resistance": 20},
    {"buff1": 'none'},
    {"buff2": 'none'},
    {"debuff1": 'none'},
    {"debuff2": 'none'}
  ],
  "enemy3": [
    {"health": 2},
    {"mana": 78},
    {"stamina": 2},
    {"attack": 20},
    {"magic": 20},
    {"defense": 30},
    {"resistance": 20},
    {"buff1": 'none'},
    {"buff2": 'none'},
    {"debuff1": 'none'},
    {"debuff2": 'none'}
  ]

}
#placed low to prevent circular dependent imports
from view.spriteSheets import spritesheetMenuBars
