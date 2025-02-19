# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        sum = 0
        dicc = defaultdict(int)
        dicc[0] = 1
        for i in nums:
            sum += i
            rem = sum % k
            rem = (rem + k) % k
            if rem in dicc:
                count += dicc[rem] 
            dicc[rem] += 1
            
            
        print(dicc)
        return count