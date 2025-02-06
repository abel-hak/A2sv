# Problem: Toeplitz Matrix - https://leetcode.com/problems/toeplitz-matrix/

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
    

        for r in range(rows - 1):
            for c in range(cols - 1):
                if matrix[r][c] != matrix[r + 1][c + 1]:
                    return False
        return True