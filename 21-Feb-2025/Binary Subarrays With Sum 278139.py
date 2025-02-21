# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        count = 0
        sum = 0
        dicc = defaultdict(int)
        dicc[0] = 1
        k = goal

        for i in nums:
            sum += i
            if sum - k in dicc:
                count += dicc[sum-k] 
            dicc[sum] += 1
            
        
        return count