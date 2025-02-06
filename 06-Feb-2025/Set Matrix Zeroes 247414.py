# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        arr = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):

                if matrix[i][j] == 0:
                    arr.append([i,j])
        for i in arr:
            for j in range(len(matrix)):
                matrix[j][i[1]] = 0
            for j in range(len(matrix[0])):
                matrix[i[0]][j] = 0

            
        