# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 13:29:16 2020

@author: George
"""

import unittest
from packages.scorePaths.GoalCombos import GoalCombos


class TestGoaliePull(unittest.TestCase):
    def test_goal_combos(self):
        all_bad = GoalCombos(5, 5, -1)
        self.assertEqual(all_bad.valid_combo_num(), 0)

        one_good = GoalCombos(1, 1, 0)
        self.assertEqual(one_good.valid_combo_num(), 1)

        all_good = GoalCombos(1, 5, 1)
        self.assertEqual(all_good.valid_combo_num(), 6)


if __name__ == '__main__':
    unittest.main()
