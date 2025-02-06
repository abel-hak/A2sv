# Problem: Spiral Matrix - https://leetcode.com/problems/spiral-matrix/

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        i, j = 0, 0
        m, n = len(matrix), len(matrix[0])
        visited = set()

        while len(res) < m * n:
            while j < n and (i, j) not in visited:  
                res.append(matrix[i][j])
                visited.add((i, j))
                j += 1
            j -= 1
            i += 1

            while i < m and (i, j) not in visited:  
                res.append(matrix[i][j])
                visited.add((i, j))
                i += 1
            i -= 1
            j -= 1

            while j >= 0 and (i, j) not in visited: 
                res.append(matrix[i][j])
                visited.add((i, j))
                j -= 1
            j += 1
            i -= 1

            while i >= 0 and (i, j) not in visited:  
                res.append(matrix[i][j])
                visited.add((i, j))
                i -= 1
            i += 1
            j += 1

        return res
