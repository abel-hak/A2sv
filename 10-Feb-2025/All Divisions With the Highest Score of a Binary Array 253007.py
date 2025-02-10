# Problem: All Divisions With the Highest Score of a Binary Array - https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixsum = []
        sufixsum = []
        sum = 0
        prefixsum.append(0)
        sufixsum.append(0)
        for i in range(n):
            sum += nums[i]
            prefixsum.append(sum)
        sum = 0
        for j in range(n-1,-1,-1):
            sum += nums[j]
            sufixsum.append(sum)
       
        max1 = float('-inf')
        arr = []
        count = 0
        for i in range(n+1):
            ss = count - prefixsum[i] + sufixsum[n-i]
            if max1 < ss:
                max1 = ss
                arr = [i]
            elif max1 == ss:
                arr.append(i)
            count += 1
        return arr

