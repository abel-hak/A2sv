# Problem: Longest-consecutive-sequence/ - https://leetcode.com/problems/longest-consecutive-sequence/

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0  

        dicc = set(nums)
        count = 0

        for i in dicc:
            if i - 1 not in dicc:
                curr = i
                streak = 1

                while curr + 1 in dicc:
                    curr += 1
                    streak += 1

                count = max(count, streak)

        return count
