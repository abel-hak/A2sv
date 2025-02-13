# Problem: Sort The Students By Their Kth Score - https://leetcode.com/problems/sort-the-students-by-their-kth-score/

class Solution:
    def sortTheStudents(self, matrix: List[List[int]], k: int) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        
        for j in range(m):
            for i in range(j+1,m):
                if matrix[i][k] > matrix[j][k]:
                    matrix[i],matrix[j] = matrix[j],matrix[i]
       
        return matrix



        