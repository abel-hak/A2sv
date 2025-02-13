# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        re = k % len(nums)
        l , r = 0 , len(nums) - 1
        while l <= r:
            nums[l],nums[r] = nums[r],nums[l]
            l += 1
            r -= 1
        l , r = 0 , re - 1
        while l <= r:
            nums[l],nums[r] = nums[r],nums[l]
            l += 1
            r -= 1
        l , r = re , len(nums)-1
        while l <= r:
            nums[l],nums[r] = nums[r],nums[l]
            l += 1
            r -= 1
        print(nums)

        
         
        