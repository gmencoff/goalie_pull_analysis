# -*- coding: utf-8 -*-
"""
Created on Sunday Nov 22 20:16:26 2020

@author: George
"""

from packages.scorePaths.GenerateCombinations import GenerateCombinations
import numpy as np


# This class calculates the possible combinations for time steps regardless of goal ordering. For example, if 5 goals
# are to be scored and there are 6 total time steps, then the possible combinations are:
# oggggg, gogggg, ggoggg, gggogg, ggggog, gggggo
class TimeCombos(GenerateCombinations):

    def __init__(self, n_goals, time_steps):
        """
        :type n_goals: int
        :type time_steps: int
        """
        # n goals is the number of goals scored in the time steps
        # time steps are the total number of time steps
        # total non-goals is time steps - n goals
        non_goals = time_steps - n_goals

        all_combos = self._all_combos(n_goals, non_goals)

        self.allowed_combos = np.array([])

        for combo in all_combos:
            if np.size(self.allowed_combos) == 0:
                self.allowed_combos = np.array(combo)
            else:
                self.allowed_combos = np.vstack((self.allowed_combos, combo))
