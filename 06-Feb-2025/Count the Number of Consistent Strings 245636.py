# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        co_al = Counter(allowed)
        cou = 0
        for i in words:
            for j in i:
                if j not in co_al:
                    break
            else:
                cou += 1
        return cou