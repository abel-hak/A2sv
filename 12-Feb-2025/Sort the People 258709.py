# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        max_height = max(heights)
        count = [None] * (max_height + 1)

        for i in range(len(heights)):
            count[heights[i]] = names[i]  

        return [count[h] for h in range(max_height, -1, -1) if count[h] is not None]