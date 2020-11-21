# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 20:16:26 2020

@author: George
"""

import itertools
import numpy as np


# this class generates acceptable goal combinations based on the number of positive scores
# negative scores and the allowable difference in goals
class GoalCombos:

    def __init__(self, p_scores, n_scores, diff_allowed):
        """
        :type n_scores: int
        :type p_scores: int
        :type diff_allowed: int
        """
        # p scores are the number of positive scores in the sequence
        # n scores are the number of negative scores in the sequence
        # diff allowed is the allowable goal difference at any point in the combo
        all_combos = self._all_combos(p_scores, n_scores)

        self.allowed_combos = np.array([])

        for combo in all_combos:
            cumulative_score = self._get_cumulative_score(combo)
            if max(cumulative_score) <= diff_allowed:
                if np.size(self.allowed_combos) == 0:
                    self.allowed_combos = np.array(combo)
                else:
                    self.allowed_combos = np.vstack((self.allowed_combos, combo))

    # this function generates an iterable of all possible combinations of 1 and -1
    def _all_combos(self, p_scores, n_scores):
        for positions in itertools.combinations(range(p_scores + n_scores), p_scores):
            goals = [-1] * (p_scores + n_scores)  # init so all goals are -1

            for iP in positions:
                goals[iP] = 1

            yield goals

    def _get_cumulative_score(self, goal_array):
        score_range = range(len(goal_array))
        cumulative_score = [0 for i in score_range]
        for goal_idx in score_range:
            if goal_idx == 0:
                cumulative_score[goal_idx] = goal_array[goal_idx]
            else:
                cumulative_score[goal_idx] = goal_array[goal_idx] + cumulative_score[goal_idx - 1]

        return cumulative_score
