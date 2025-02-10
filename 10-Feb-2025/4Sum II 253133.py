# Problem: 4Sum II - https://leetcode.com/problems/4sum-ii/

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        dicc1 = {}

        for i in nums1:
            for j in nums2:
                if i + j in dicc1:
                    dicc1[i+j] += 1
                else:
                    dicc1[i+j] = 1
        dicc2 = {}
        cou = 0

        for i in nums3:
            for j in nums4:
                if -(i + j) in dicc1:
                    cou += dicc1[-(i+j)]
            
                
        
        return cou
        
        

        