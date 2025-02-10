# Problem: Maximum Gap - https://leetcode.com/problems/maximum-gap/

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        max1 = 0
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                temp = nums[i+1] - nums[i]
                max1 = max(max1,temp)
        return max1