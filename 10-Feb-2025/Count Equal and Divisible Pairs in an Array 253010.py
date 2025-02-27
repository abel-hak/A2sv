# Problem: Count Equal and Divisible Pairs in an Array - https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cou = 0
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    cou += 1
        return cou

        