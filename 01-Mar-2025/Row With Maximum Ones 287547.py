# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max1 = float('-inf')
        ind = -1
        for i in range(len(mat)):
            sum = 0
            for j in range(len(mat[0])):
                sum += mat[i][j]
            if sum > max1:
                max1 = sum
                ind = i
        return [ind,max1]
