# Problem: Count Number of Nice Subarrays - https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        dicc = defaultdict(int)
        dicc[0] = 1
        sum = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                sum += 1
            if sum - k in dicc:
                count += dicc[sum-k]
            dicc[sum] += 1
        
        return count