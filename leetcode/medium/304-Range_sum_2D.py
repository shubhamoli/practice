"""
    Leetcode #304
"""

from typing import List

# Extension of LC#307
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return

        M = len(matrix)
        N = len(matrix[0])

        self._sum = [[0 for i in range(N+1)] for j in range(M+1)]

        for i in range(M):
            for j in range(N):
                self._sum[i+1][j+1] = self._sum[i+1][j] + self._sum[i][j+1] + matrix[i][j] - self._sum[i][j]

    # call to this will be frequent, so try to avoid calculation in this
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self._sum[row2+1][col2+1] - self._sum[row1][col2+1] - self._sum[row2+1][col1] + self._sum[row1][col1]


if __name__ == "__main__":


    matrix = [
          [3, 0, 1, 4, 2],
          [5, 6, 3, 2, 1],
          [1, 2, 0, 1, 5],
          [4, 1, 0, 1, 7],
          [1, 0, 3, 0, 5]
    ]

    obj = NumMatrix(matrix)

    assert obj.sumRegion(2, 1, 4, 3) == 8
    assert obj.sumRegion(1, 1, 2, 2) == 11
    assert obj.sumRegion(1, 2, 3, 4) == 12

