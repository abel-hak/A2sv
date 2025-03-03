# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        count = 0
        for i in s:
            if i == 'L':
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                count += 1
        
        return count