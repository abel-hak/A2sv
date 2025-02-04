# Problem: Check if All Characters Have Equal Number of Occurrences - https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        cou = Counter(s)
        co  = 0
        for c in cou:
            if co == 0:
                s = cou[c]
            if cou[c] != s and co != 0:
                return False
            co += 1
        return True