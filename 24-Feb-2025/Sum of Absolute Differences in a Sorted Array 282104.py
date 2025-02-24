# Problem: Sum of Absolute Differences in a Sorted Array - https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]
        
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]

        result = []
        for i in range(n):
            if i == 0:
                left_sum = 0
            else:
                left_sum = i * nums[i] - prefix_sum[i - 1]
            
            if i == n - 1:
                right_sum = 0
            else:
                right_sum = (prefix_sum[n - 1] - prefix_sum[i]) - (n - i - 1) * nums[i]
            
            result.append(left_sum + right_sum)
        
        return result

