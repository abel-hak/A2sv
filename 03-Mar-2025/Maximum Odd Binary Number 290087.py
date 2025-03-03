# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ss= ""
        count = 0
        for i in s:
            if i == '1':
                count += 1
        count -= 1
        temp = count
        while temp > 0:
            ss += '1'
            temp -= 1
        n = len(s) - count-1
        for i in range(n):
            ss += '0'
        ss += '1'
        return ss

            
        