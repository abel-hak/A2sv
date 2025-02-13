# Problem: Selection Sort - https://practice.geeksforgeeks.org/problems/selection-sort/1

class Solution:
    def sortTheStudents(self, matrix: List[List[int]], k: int) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        
        for j in range(m):
            for i in range(j+1,m):
                if matrix[i][k] > matrix[j][k]:
                    matrix[i],matrix[j] = matrix[j],matrix[i]
       
        return matrix



        