import unittest
from gamedata import relocateMove, currentTile, healthStat, subtractDamage, debuffSlot1, debuffSlot2, giveFragile

class TestGameData(unittest.TestCase):

    def test_relocateMove(self):
        c = currentTile('friendly1')
        relocateMove('friendly1', c+1)
        self.assertEqual(currentTile('friendly1'), c+1)

    def test_Damage(self):
      initialHealth = healthStat('enemy2')
      subtractDamage('enemy2', 40)
      self.assertEqual(initialHealth, healthStat('enemy2') + 40)

    def test_DebuffFragile(self):
        initialDebuff1 = debuffSlot1('enemy3')
        initialDebuff2 = debuffSlot2('friendly3')
        giveFragile('enemy3', 'debuff1')
        giveFragile('friendly3', 'debuff2')
        self.assertEqual('fragile', debuffSlot1('enemy3'))
        self.assertEqual('fragile', debuffSlot2('friendly3'))

if __name__ == '__main__':
    unittest.main()
