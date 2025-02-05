# Problem: Check if One String Swap Can Make Strings Equal - https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        
        if len(s1) != len(s2):
            return False
        
        diff = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff.append(i)
                
        if len(diff) == 2:
            i, j = diff
            return s1[i] == s2[j] and s1[j] == s2[i]
        
        return len(diff) == 0
