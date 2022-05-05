#stored gamedata

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
    {"debuff2": 'none'},
    {"action": 'none'},
    {"spriteNum": 1},
    {"currentX": 44}, #-36 (tile1)
    {"currentY": 360}, #-104 (tile1)
    {"previousX": 0},
    {"previousY": 0}
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
    {"debuff2": 'none'},
    {"action": 'none'},
    {"spriteNum": 1},
    {"currentX": 300},
    {"currentY": 300},
    {"previousX": 0},
    {"previousY": 0}
  ],
  "friendly3": [
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
    {"debuff2": 'none'},
    {"action": 'none'},
    {"spriteNum": 1},
    {"currentX": 500},
    {"currentY": 500},
    {"previousX": 0},
    {"previousY": 0}
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
    {"debuff2": 'none'},
    {"action": 'none'},
    {"spriteNum": 1},
    {"currentX": 1420},
    {"currentY": 500},
    {"previousX": 0},
    {"previousY": 0}
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
    {"debuff2": 'none'},
    {"action": 'none'},
    {"spriteNum": 1},
    {"currentX": 1620},
    {"currentY": 300},
    {"previousX": 0},
    {"previousY": 0}
  ],
  "enemy3": [
    {"health": 100}, #0
    {"mana": 50}, #1
    {"stamina": 3}, #2
    {"attack": 20}, #3
    {"magic": 20}, #4
    {"defense": 30}, #5
    {"resistance": 20}, #6
    {"buff1": 'none'}, #7
    {"buff2": 'none'}, #8
    {"debuff1": 'none'}, #9
    {"debuff2": 'none'}, #10
    {"action": 'none'}, #11
    {"spriteNum": 1}, #12
    {"currentX": 1820}, #13
    {"currentY": 100}, #14
    {"previousX": 0}, #15
    {"previousY": 0} #16
  ]

}

def attackStab(user, target):
    if statsCharacter[target][11]['action'] == 'none':
        damage = statsCharacter[user][3]['attack']
    else:
        damage = statsCharacter[user][3]['attack'] - statsCharacter[target][5]['defense']
    if damage > 0:
        if statsCharacter[target][9]['debuff1'] == 'fragile' or statsCharacter[target][10]['debuff2'] == 'fragile':
            damage *= 1.5
        statsCharacter[target][0]['health'] -= damage
        if statsCharacter[target][9]['debuff1'] == 'none' or statsCharacter[target][9]['debuff1'] == "fragile":
            statsCharacter[target][9]['debuff1'] = 'fragile'
        else:
            statsCharacter[target][10]['debuff2'] = 'fragile'
    if statsCharacter[target][0]['health'] < 0:
        statsCharacter[target][0]['health'] = 0
