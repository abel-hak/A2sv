# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        r = len(nums)-1
        print(nums)
        while r-2 >= 0:
            if nums[r] < nums[r-1] + nums[r-2]:
                return nums[r] + nums[r-1] + nums[r-2]
            r-=1
        return 0