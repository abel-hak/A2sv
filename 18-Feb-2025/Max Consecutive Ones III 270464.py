# Problem: Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/

from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        count = 0
        max1 = 0
        
        while r < len(nums):
            if nums[r] == 1:
                count += 1
            else:
                if k > 0:
                    k -= 1
                    count += 1
                else:
                    max1 = max(max1, count)
                    while nums[l] == 1:
                        l += 1
                        count -= 1
                    l += 1  
            
            r += 1
        
        return max(max1, count)