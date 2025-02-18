# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1) - 1
        cou1 = Counter(s1)

        while r < len(s2):
            temp = Counter(s2[l:r+1])
            if temp == cou1:
                return True
            else:
                l += 1
                r += 1
        return False
        