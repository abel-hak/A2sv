# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        dicc = defaultdict(int)
        for i in range(len(nums) ):
            for j in range(i+1,len(nums)):
                dicc[nums[i] * nums[j]] += 1
        
        sum = 0  
        for i in dicc:
            print(dicc[i])
            if dicc[i] > 1:
                sum += 8 * int((dicc[i] * (dicc[i] - 1)/2))
        return sum