# Problem: 3Sum Closest  - https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        mindiff1 = float('inf')
        minsumm2 = 0
        for i in range(len(nums)):
            l , r = 0 , len(nums) - 1
            mindiff = float('inf')
            minsumm = 0
            while l < r and l != i and r != i:
                sum = nums[i] + nums[l] + nums[r]
                diff = abs(target - sum)
                if sum == target:
                    return sum
                elif sum > target:
                    r-=1
                else:
                    l += 1
                if diff < mindiff:
                    mindiff = diff
                    minsumm = sum
            
            if mindiff < mindiff1:
                mindiff1 = mindiff
                minsumm2 = minsumm
                
        
        return minsumm2
