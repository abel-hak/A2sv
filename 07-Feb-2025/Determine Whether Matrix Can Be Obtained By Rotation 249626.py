# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rev(mat):
            arr = []

            for j in range(len(mat)-1,-1,-1):
                arr.append(mat[j])
            return arr
        
        def transpose(matrix):
            res = []
            for i in  range(len(matrix[0])):
                arr = []
                for j in range(len(matrix)):
                    arr.append(matrix[j][i])
                res.append(arr)

            return res 

        for _ in range(4):  
            if mat == target:
                return True
            temp = rev(mat)
            mat = transpose(temp)
            
        
        return False
