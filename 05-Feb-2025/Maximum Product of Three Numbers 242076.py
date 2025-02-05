# Problem: Maximum Product of Three Numbers - https://leetcode.com/problems/maximum-product-of-three-numbers/description/

from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1

        if len(nums) == 3:
            return nums[l] * nums[l+1] * nums[l+2]

       
        max1 = nums[l] * nums[l+1] * nums[r]  # Two smallest negatives and the largest positive
        max2 = nums[r] * nums[r-1] * nums[r-2]  # Three largest values

        return max(max1, max2)
