import unittest
from gamedata import healthStat, manaStat, staminaStat, attackStat, magicStat, defenseStat, resistanceStat, buffSlot1, buffSlot2, debuffSlot1, debuffSlot2, characterAction, characterSpriteNum, characterCurrentTile, characterPreviousTile, subtractDamage, setHealth, giveFragile, relocateMove, attackStab, isActionDecided, statsCharacter

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

if __name__ == '__main__':
    unittest.main()
