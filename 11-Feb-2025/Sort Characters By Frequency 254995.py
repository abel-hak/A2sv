# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        cou = Counter(s)
        sorted_chars = sorted(s, key=lambda x: (-cou[x], x))
        return "".join(sorted_chars)
