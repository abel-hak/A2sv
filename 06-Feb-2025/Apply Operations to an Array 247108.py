# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i+1] = 0
        cou = 0
        arr=[]
        for i in range(len(nums)):
            if nums[i] == 0:
                cou += 1
            else:
                arr.append(nums[i])

        for i in range(cou):
            arr.append(0)
        return arr
