# Problem: Maximum Score After Splitting a String  - https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
        prefix = []
        total = 0
        for i in s:
            total += int(i)
            prefix.append(total)
            
        max1 = float('-inf')
        for i in range(len(s) - 1):  # Ensure valid split
            sum1 = prefix[-1] - prefix[i] + (i + 1 - prefix[i])
            max1 = max(max1, sum1)
        return max1
