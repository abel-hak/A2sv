# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = []
        sum = 0
        for i in nums:
            sum += i
            prefix.append(sum)
        for i in range(len(nums)):
            l_sum = prefix[i-1] if i != 0 else 0
            r_sum = prefix[n-1] - prefix[i]
            if l_sum == r_sum:
                return i
        return -1