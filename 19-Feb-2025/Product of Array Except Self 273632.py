# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        mul = 1
        for i in range(n):
            prefix[i] = mul
            mul *= nums[i]
        
        right = 1
        print(prefix)
    
        for i in range(len(nums) - 1,-1,-1):
            prefix[i] = prefix[i] * right
            right *= nums[i]
        
        return prefix
