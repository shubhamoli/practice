"""
    Leetcode #240
"""


class Solution:
    def searchMatrix(self, matrix, target) -> bool:
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        if not matrix[0]:
            return False

        M = len(matrix)
        N = len(matrix[0])

        row = M - 1
        col = 0
        while row >= 0 and col < N:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                row = row - 1
            else:
                col = col + 1

        return False



if __name__ == "__main__":

    matrix = [
          [1,   4,  7, 11, 15],
          [2,   5,  8, 12, 19],
          [3,   6,  9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]
        ]

    assert Solution().searchMatrix(matrix, 5) == True
    assert Solution().searchMatrix(matrix, 20) == False

