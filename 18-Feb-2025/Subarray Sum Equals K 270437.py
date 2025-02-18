# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sum = 0
        dicc = defaultdict(int)
        dicc[0] = 1

        for i in nums:
            sum += i
            if sum - k in dicc:
                count += dicc[sum-k] 
            dicc[sum] += 1
            
        
        return count
        