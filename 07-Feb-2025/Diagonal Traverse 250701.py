# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

from typing import List

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        n, m = len(matrix), len(matrix[0])
        i, j = 0, 0

        while len(res) < n * m:
            
            while i >= 0 and j < m:
                res.append(matrix[i][j])
                i -= 1
                j += 1
            i += 1  
            if j >= m:  
                i += 1
                j -= 1

            
            while j >= 0 and i < n:
                res.append(matrix[i][j])
                i += 1
                j -= 1
            j += 1  
            if i >= n:  
                i -= 1
                j += 1
        
        return res
