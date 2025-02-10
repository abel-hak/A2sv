# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sum = 0
        ans=[]
        for i in nums:
            if i % 2 == 0:
                sum += i
            
            
        for i in queries:
            if nums[i[1]] % 2 == 0:
                sum = sum - nums[i[1]]
            nums[i[1]] = nums[i[1]] + i[0]
            if nums[i[1]] % 2 == 0:
                sum = sum + nums[i[1]]
            ans.append(sum)

        return ans