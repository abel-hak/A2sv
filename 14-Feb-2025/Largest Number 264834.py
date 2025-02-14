# Problem: Largest Number - https://leetcode.com/problems/largest-number/

from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if str(nums[i]) + str(nums[j]) < str(nums[j]) + str(nums[i]):
                    nums[i], nums[j] = nums[j], nums[i]
                    
        if nums[0] == 0:
            return "0"
                
        gg = ""
        for i in nums:
            gg += str(i)
        return gg