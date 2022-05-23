#stored gamedata
from view.renderGame import tilePositions

statsCharacter = {
  "friendly1": {
    "health": 100,
    "mana": 50,
    "stamina": 3,
    "attack": 20,
    "magic": 20,
    "defense": 30,
    "resistance": 20,
    "buff1": ['none', 0],
    "buff2": ['none', 0],
    "debuff1": ['none', 0],
    "debuff2": ['none', 0],
    "action": 'none',
    "movingTo": 'none',
    "spriteNum": 1,
    "currentTile": 10,
    "previousTile": 0
  },
  "friendly2": {
    "health": 100,
    "mana": 50,
    "stamina": 3,
    "attack": 20,
    "magic": 20,
    "defense": 30,
    "resistance": 20,
    "buff1": ['none', 0],
    "buff2": ['none', 0],
    "debuff1": ['none', 0],
    "debuff2": ['none', 0],
    "action": 'none',
    "movingTo": 'none',
    "spriteNum": 1,
    "currentTile": 3,
    "previousTile": 0
  },
  "friendly3": {
    "health": 100,
    "mana": 50,
    "stamina": 3,
    "attack": 20,
    "magic": 20,
    "defense": 30,
    "resistance": 20,
    "buff1": ['none', 0],
    "buff2": ['none', 0],
    "debuff1": ['none', 0],
    "debuff2": ['none', 0],
    "action": 'none',
    "movingTo": 'none',
    "spriteNum": 1,
    "currentTile": 5,
    "previousTile": 0
    },

  "enemy1": {
    "health": 100,
    "mana": 50,
    "stamina": 3,
    "attack": 20,
    "magic": 20,
    "defense": 30,
    "resistance": 20,
    "buff1": ['none', 0],
    "buff2": ['none', 0],
    "debuff1": ['none', 0],
    "debuff2": ['none', 0],
    "action": 'none',
    "movingTo": 'none',
    "spriteNum": 1,
    "currentTile": 17,
    "previousTile": 0
  },
  "enemy2": {
    "health": 100,
    "mana": 50,
    "stamina": 3,
    "attack": 20,
    "magic": 20,
    "defense": 30,
    "resistance": 20,
    "buff1": ['none', 0],
    "buff2": ['none', 0],
    "debuff1": ['none', 0],
    "debuff2": ['none', 0],
    "action": 'none',
    "movingTo": 'none',
    "spriteNum": 1,
    "currentTile": 22,
    "previousTile": 0
  },
  "enemy3": {
    "health": 100, #0
    "mana": 50, #1
    "stamina": 3, #2
    "attack": 20, #3
    "magic": 20, #4
    "defense": 30, #5
    "resistance": 20, #6
    "buff1": ['none', 0], #7
    "buff2": ['none', 0], #8
    "debuff1": ['none', 0], #9
    "debuff2": ['none', 0], #10
    "action": 'none', #11
    "movingTo": 'none', #12
    "spriteNum": 1, #13
    "currentTile": 24, #14
    "previousTile": 0 #15
  }
  }

defaultStats = {
    "health": 100,
    "mana": 50,
    "stamina": 3,
    "attack": 20,
    "magic": 20,
    "defense": 30,
    "resistance": 20,
    "buff1": ['none', 0],
    "buff2": ['none', 0],
    "debuff1": ['none', 0],
    "debuff2": ['none', 0],
    "action": 'none',
    "movingTo": 'none',
    "spriteNum": 1,
  }

menuLocation = 'main'
#main, attack, defend, special, or relocate



#----------------------------------------------------------------------#
#                         Dependent functions                          #
#----------------------------------------------------------------------#

def healthStat(character):
    return statsCharacter[character]['health']

def manaStat(character):
    return statsCharacter[character]['mana']

def staminaStat(character):
    return statsCharacter[character]['stamina']

def attackStat(character):
    return statsCharacter[character]['attack']

def magicStat(character):
    return statsCharacter[character]['magic']

def defenseStat(character):
    return statsCharacter[character]['defense']

def resistanceStat(character):
    return statsCharacter[character]['resistance']

def buffSlot1(character):
    return statsCharacter[character]['buff1'][0]

def buffSlot2(character):
    return statsCharacter[character]['buff2'][0]

def debuffSlot1(character):
    return statsCharacter[character]['debuff1'][0]

def debuffSlot2(character):
    return statsCharacter[character]['debuff2'][0]

def characterAction(character):
    return statsCharacter[character]['action']

def characterSpriteNum(character):
    return statsCharacter[character]['spriteNum']

def characterCurrentTile(character):
    return statsCharacter[character]['currentTile']

def characterPreviousTile(character):
    return statsCharacter[character]['previousTile']

def subtractDamage(character, damage):
    statsCharacter[character]['health'] -= damage

def setHealth(character, value):
    statsCharacter[character]['health'] = value

def giveFragile(character, debuffSlot):
    statsCharacter[character][debuffSlot][0] = 'fragile'
    statsCharacter[character][debuffSlot][1] = 1

#----------------------------------------------------------------------#
#                              Actions                                 #
#----------------------------------------------------------------------#

def attackStab(user, target):
    if characterAction(target) == 'none':
        damage = attackStat(user)
    elif characterAction(target) == 'defendSelf':
        damage = attackStat(user) - defenseStat(target)
    if damage > 0:
        if debuffSlot1(target) == 'fragile' or debuffSlot2(target) == 'fragile':
            damage *= 1.5
        subtractDamage(target, damage)
        if debuffSlot1(target) == 'none' or debuffSlot1(target) == "fragile":
            giveFragile(target, 'debuff1')
        else:
            giveFragile(target, 'debuff2')
    if healthStat(target) < 0:
        setHealth(target, 0)

def defendSelf(character):
    statsCharacter[character]['action'] = 'defendSelf'

def relocateMove(character, tileNumber):
    topLeftXMoveRange = tilePositions[statsCharacter[character]['currentTile'] - 1][0] - 185 #185 is just enough to move horizontally through columns
    topLeftYMoveRange = tilePositions[statsCharacter[character]['currentTile'] - 1][1] - 205 #205 is just enough to move vertically in a two tile column
    bottomRightXMoveRange = tilePositions[statsCharacter[character]['currentTile'] - 1][0] + 185
    bottomRightYMoveRange = tilePositions[statsCharacter[character]['currentTile'] - 1][1] + 205
    if statsCharacter[character]['stamina'] != 0:
        if tilePositions[tileNumber - 1][0] > topLeftXMoveRange and tilePositions[tileNumber - 1][0] < bottomRightXMoveRange and tilePositions[tileNumber - 1][1] > topLeftYMoveRange and tilePositions[tileNumber - 1][1] < bottomRightYMoveRange and tileNumber != statsCharacter[character]['currentTile']:
            for i in range(1, 4):
                if str(i) == character[-1]: #if evaluating same character
                    break
                if (tilePositions[statsCharacter[character[0:-1] + str(i)]['currentTile'] - 1][0] == tilePositions[tileNumber - 1][0] and tilePositions[statsCharacter[character[0:-1] + str(i)]['currentTile'] - 1][1] == tilePositions[tileNumber - 1][1]):
                    statsCharacter[character]['movingTo'] = 'none'
                    return
            statsCharacter[character]['currentTile'] = tileNumber
            statsCharacter[character]['movingTo'] = tileNumber
            statsCharacter[character]['stamina'] -= 1
            return
    statsCharacter[character]['movingTo'] = 'none'
    return

#----------------------------------------------------------------------#
#                              General                                 #
#----------------------------------------------------------------------#

def roundEndRestoration():
    effects = ['buff1', 'buff2', 'debuff1', 'debuff2']
    chars = ['friendly', 'enemy']
    for c in chars:
        for i in range(1, 4):
            if healthStat(c + str(i)) != 0:
                statsCharacter[c + str(i)]['mana'] += 20
                if statsCharacter[c + str(i)]['mana'] > 100:
                    statsCharacter[c + str(i)]['mana'] = 100
                if statsCharacter[c + str(i)]['movingTo'] == 'none':
                    statsCharacter[c + str(i)]['stamina'] = 3
                statsCharacter[c + str(i)]['action'] = 'none'
                statsCharacter[c + str(i)]['movingTo'] = 'none'
                for e in effects:
                    if statsCharacter[c + str(i)][e][1] != 0:
                        statsCharacter[c + str(i)][e][1] -= 1
                        if statsCharacter[c + str(i)][e][1] == 0:
                            statsCharacter[c + str(i)][e][0] = 'none'

def isActionDecided(side):
    actions = ['none', 'none', 'none']
    for i in range(1, 4):
        if statsCharacter[side + str(i)]['action'] != 'none' or statsCharacter[side + str(i)]['movingTo'] != 'none':
            actions[i - 1] = True
        else:
            actions[i - 1] = False
    return actions

def currentMenu():
    return menuLocation
