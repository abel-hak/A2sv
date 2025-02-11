# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

from collections import Counter
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicc = defaultdict(list)
        for i in strs:
            arr = "".join(sorted(i))
            dicc[arr].append(i)
        ans = []
        for i in dicc:
            ans.append(dicc[i])
       
        return ans
