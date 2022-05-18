import unittest
from gamedata import *

class TestGameData(unittest.TestCase):

    def test_relocateMove(self):
        c = characterCurrentTile('friendly1')
        relocateMove('friendly1', c+1)
        self.assertEqual(characterCurrentTile('friendly1'), c+1)

    def test_Damage(self):
      initialHealth = healthStat('enemy2')
      subtractDamage('enemy2', 40)
      self.assertEqual(initialHealth, healthStat('enemy2') + 40)

    def test_DebuffFragile(self):
        initialDebuff1 = debuffSlot1('enemy3')
        giveFragile('enemy3', 'debuff1')
        self.assertEqual('fragile', debuffSlot1('enemy3'))

    def test_AttackStab(self):
        initialHealth = healthStat('friendly2')
        attackStab('enemy1', 'friendly2')
        self.assertEqual(initialHealth, healthStat('friendly2') + 20)
        attackStab('enemy1', 'friendly2')
        self.assertEqual(initialHealth, healthStat('friendly2') + 50)

    def test_isActionDecided(self):
        statsCharacter['friendly1']['action'] = 'attack'
        self.assertEqual(isActionDecided('friendly'), [True, False, False] )
        self.assertEqual(isActionDecided('enemy'), [False, False, False] )

    def test_roundEndRestoration(self):
        statsCharacter['friendly1']['action'] = 'attack'
        statsCharacter['friendly2']['movingTo'] = 2
        statsCharacter['friendly3']['mana'] = 81
        statsCharacter['enemy1']['movingTo'] = 'none'
        statsCharacter['enemy1']['stamina'] = 1
        statsCharacter['enemy2']['health'] = 0
        statsCharacter['enemy2']['mana'] = 81
        statsCharacter['enemy3']['buff1'][0] = 'charged'
        statsCharacter['enemy3']['buff1'][1] = 1
        statsCharacter['enemy3']['debuff1'][0] = 'fragile'
        statsCharacter['enemy3']['debuff1'][1] = 1
        statsCharacter['enemy3']['debuff2'][0] = 'vulnerable'
        statsCharacter['enemy3']['debuff2'][1] = 2
        roundEndRestoration()
        self.assertEqual(statsCharacter['friendly1']['action'], 'none')
        self.assertEqual(statsCharacter['friendly2']['movingTo'], 'none')
        self.assertEqual(statsCharacter['friendly3']['mana'], 100)
        self.assertEqual(statsCharacter['enemy1']['stamina'], 3)
        self.assertEqual(statsCharacter['enemy2']['mana'], 81)
        self.assertEqual(statsCharacter['enemy3']['buff1'][0], 'none')
        self.assertEqual(statsCharacter['enemy3']['buff1'][1], 0)
        self.assertEqual(statsCharacter['enemy3']['debuff1'][0], 'none')
        self.assertEqual(statsCharacter['enemy3']['debuff1'][1], 0)
        self.assertEqual(statsCharacter['enemy3']['debuff2'][0], 'vulnerable')
        self.assertEqual(statsCharacter['enemy3']['debuff2'][1], 1)

    def test_defendSelf(self):
        defendSelf('friendly1')
        attackStab('enemy3', 'friendly1')
        self.assertEqual(statsCharacter['friendly1']['health'], 100)
        self.assertEqual(statsCharacter['friendly1']['debuff1'][0], 'none')
        self.assertEqual(statsCharacter['friendly1']['debuff1'][1], 0)

    def test_relocateMove(self):
        statsCharacter['friendly3']['currentTile'] = 5
        initial = statsCharacter['friendly3']['currentTile']
        statsCharacter['friendly2']['currentTile'] = 1
        initial2 = statsCharacter['friendly2']['currentTile']
        relocateMove('friendly3', 4)
        self.assertEqual(initial, statsCharacter['friendly3']['currentTile'] - 1)
        relocateMove('friendly3', 10)
        self.assertEqual(statsCharacter['friendly3']['currentTile'], 4)
        returnResult = relocateMove('friendly3', 4)
        self.assertEqual(returnResult, False)
        returnResult = relocateMove('friendly3', 1)
        self.assertEqual(returnResult, False)

if __name__ == '__main__':
    unittest.main()
