# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x = -1
        y = -1
        i = 0
        while i + 1 < len(matrix):
            if matrix[i][0] < target < matrix[i+1][0]:
                x = i 
                break
            elif matrix[i][0] == target  or target == matrix[i+1][0]:
                return True
            i+=1
        
        j = 0
        while j < len(matrix[0]):
            if matrix[x][j] == target:
                return True
            j += 1
        return False
        