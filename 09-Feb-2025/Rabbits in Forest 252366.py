# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

from collections import Counter
from typing import List

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        cou = Counter(answers)
        sum = 0

        for i in cou:
            if i == 0:
                sum += cou[i]
            elif cou[i] <= i + 1:
                sum += i + 1
            else:
                ss = (cou[i] + i) // (i + 1)
                sum += ss * (i + 1)

        return sum
