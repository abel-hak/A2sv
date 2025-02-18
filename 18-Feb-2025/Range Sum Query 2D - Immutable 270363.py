# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

from typing import List

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.List = matrix
        n = len(self.List)
        m = len(self.List[0])
        self.pre_t = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                self.pre_t[i][j] = (
                    self.List[i - 1][j - 1] +
                    self.pre_t[i - 1][j] +
                    self.pre_t[i][j - 1] -
                    self.pre_t[i - 1][j - 1]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.pre_t[row2 + 1][col2 + 1]
            - self.pre_t[row1][col2 + 1]
            - self.pre_t[row2 + 1][col1]
            + self.pre_t[row1][col1]
        )
