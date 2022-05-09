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
    "buff1": 'none',
    "buff2": 'none',
    "debuff1": 'none',
    "debuff2": 'none',
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



def relocateMove(user, tileNumber):
    statsCharacter[user]['currentTile'] = tileNumber

def attackStab(user, target):
    if statsCharacter[target]['action'] == 'none':
        damage = statsCharacter[user]['attack']
    else:
        damage = statsCharacter[user]['attack'] - statsCharacter[target]['defense']
    if damage > 0:
        if statsCharacter[target]['debuff1'] == 'fragile' or statsCharacter[target]['debuff2'] == 'fragile':
            damage *= 1.5
        statsCharacter[target]['health'] -= damage
        if statsCharacter[target]['debuff1'] == 'none' or statsCharacter[target]['debuff1'] == "fragile":
            statsCharacter[target]['debuff1'] = 'fragile'
        else:
            statsCharacter[target]['debuff2'] = 'fragile'
    if statsCharacter[target]['health'] < 0:
        statsCharacter[target]['health'] = 0
