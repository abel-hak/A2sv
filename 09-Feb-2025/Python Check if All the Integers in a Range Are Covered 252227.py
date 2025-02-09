# Problem: Python Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        cou = 0
        tem = right - left + 1
        while left <= right:
            for i in ranges:
                co = 0
                print(i[0], i[1])
                if i[0] <= left <= i[1] and co==0:
                    co+=1
                    cou+=1
                    break
            left += 1
        
        return cou == tem
        
