# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        left = 0
        right = 1
        profit = 0
        while right < len(nums):
            if nums[left] > nums[right]:
                left = right
                right += 1
            else:
                profit = max(profit,nums[right] - nums[left])
                right += 1
        return profit

