# Problem: Running Sum of 1d Array - https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr = []
        sum = 0
        for i in nums:
            sum += i
            arr.append(sum)
        return arr
