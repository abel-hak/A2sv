# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        cou = Counter(nums)
        lef = 0
        coun = 0
        for i in cou:
            if cou[i] % 2 != 0:
                lef += 1
                if cou[i] >= 2:
                    coun  += cou[i] // 2
                
            else:
                coun += cou[i] // 2
        return [coun,lef]
