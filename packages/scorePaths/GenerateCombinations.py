# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 20:16:26 2020

@author: George
"""

import itertools
from typing import List, Any


# this class generates acceptable goal combinations based on the number of positive scores
# negative scores and the allowable difference in goals
class GenerateCombinations:
    allowed_combos = []

    # return the number of valid combos
    def valid_combo_num(self):
        dimensions = self.allowed_combos.shape

        if len(dimensions) == 1:
            if dimensions[0] == 0:
                return 0
            else:
                return 1
        else:
            return dimensions[0]

    # this function generates an iterable of all possible combinations of 1 and -1
    def _all_combos(self, p_scores, n_scores):
        for positions in itertools.combinations(range(p_scores + n_scores), p_scores):
            goals = [-1] * (p_scores + n_scores)  # init so all goals are -1

            for iP in positions:
                goals[iP] = 1

            yield goals
