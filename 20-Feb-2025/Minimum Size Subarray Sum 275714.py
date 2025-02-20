# Problem: Minimum Size Subarray Sum - https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        min1 = float('inf')
        n = len(nums)
        sum = 0
        for right in range(n):
            sum += nums[right]
            while sum >= target:
                min1 = min(min1,right-left+1)
                sum -= nums[left]
                left += 1
        return min1 if min1 != float('inf') else 0
