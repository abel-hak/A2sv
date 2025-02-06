# Problem: Valid Sudoku - https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m, n = 9, 9  # Fixed size for Sudoku
        
     
        for j in range(n):  
            seen = set()
            for i in range(m):  
                if board[i][j] != "." and board[i][j] in seen:
                    return False
                seen.add(board[i][j])

       
        for row in board: 
            seen = set()
            for val in row:  
                if val != "." and val in seen:
                    return False
                seen.add(val)
        
     
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                seen = set()
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        if board[r][c] != "." and board[r][c] in seen:
                            return False
                        seen.add(board[r][c])

        return True