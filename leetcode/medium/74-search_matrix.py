"""
    Leetcode #74
"""


from typing import List

class Solution:

    # Brute force -- O(n^2)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        if not target:
            return False

        if target < matrix[0][0]:
            return False

        if target > matrix[-1][-1]:
            return False

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True

        return False

    # O(log(mn)) == O(log(m)) + O(log(n))
    def searchMatrix_OPTI(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        if target == None or target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        M = len(matrix)
        N = len(matrix[0])

        l = 0
        r = M * N - 1
        while l != r:
            mid = (l + r) // 2
            if matrix[mid // N][mid % N] == target:
                return True

            if matrix[mid // N][mid % N] < target:
                l = mid + 1
            else:
                r = mid

        return False


if __name__ == "__main__":

    solution = Solution()

    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]

    assert solution.searchMatrix(matrix, 3) == True
    assert solution.searchMatrix(matrix, 13) == False

    assert solution.searchMatrix_OPTI(matrix, 3) == True
    assert solution.searchMatrix_OPTI(matrix, 13) == False
