# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dicc = {}
        min1 = float('inf')
        re = []
        
       
        for i in range(len(list1)):
            dicc[list1[i]] = i
        
        
        for i in range(len(list2)):
            if list2[i] in dicc:
                sum_indices = dicc[list2[i]] + i
                if sum_indices < min1:
                    min1 = sum_indices
                    re = [list2[i]]  
                elif sum_indices == min1:
                    re.append(list2[i])  
        
        return re
