#stored gamedata

statsCharacter = {
  "friendly1": {
    "health": 100,
    "mana": 50,
    "stamina": 3,
    "attack": 20,
    "magic": 20,
    "defense": 30,
    "resistance": 20,
    "buff1": 'none',
    "buff2": 'none',
    "debuff1": 'none',
    "debuff2": 'none',
    "action": 'none',
    "spriteNum": 1,
    "currentTile": 1,
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
    "buff1": 'charged',
    "buff2": 'none',
    "debuff1": 'vulnerable',
    "debuff2": 'fragile',
    "action": 'none',
    "spriteNum": 1,
    "currentTile": 2,
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
    "buff1": 'none',
    "buff2": 'none',
    "debuff1": 'none',
    "debuff2": 'none',
    "action": 'none',
    "spriteNum": 1,
    "currentTile": 3,
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
    "buff1": 'none',
    "buff2": 'none',
    "debuff1": 'none',
    "debuff2": 'none',
    "action": 'none',
    "spriteNum": 1,
    "currentTile": 25,
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
    "buff1": 'none',
    "buff2": 'none',
    "debuff1": 'none',
    "debuff2": 'none',
    "action": 'none',
    "spriteNum": 1,
    "currentTile": 26,
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
    "buff1": 'none', #7
    "buff2": 'none', #8
    "debuff1": 'none', #9
    "debuff2": 'none', #10
    "action": 'none', #11
    "spriteNum": 1, #12
    "currentTile": 24, #13
    "previousTile": 0 #14
  }
  }

def healthStat(target):
    return statsCharacter[target]['health']

def attackStat(user):
    return statsCharacter[user]['attack']

def subtractDamage(target, damage):
    statsCharacter[target]['health'] -= damage

def defenseStat(target):
    return statsCharacter[target]['defense']

def characterAction(target):
    return statsCharacter[target]['action']

def debuffSlot1(target):
    return statsCharacter[target]['debuff1']

def debuffSlot2(target):
    return statsCharacter[target]['debuff2']

def giveFragile(target, debuffSlot):
    statsCharacter[target][debuffSlot] = 'fragile'

def setHealth(target, value):
    statsCharacter[target]['health'] = value

def relocateMove(user, tileNumber):
    statsCharacter[user]['currentTile'] = tileNumber

def attackStab(user, target):
    if characterAction(target) == 'none':
        damage = attackStat(user)
    else:
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
