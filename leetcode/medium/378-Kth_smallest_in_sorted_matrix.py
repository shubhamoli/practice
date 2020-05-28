"""
    Leetcode #378
"""


from typing import List
import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or not matrix[0]:
            return -1

        heap, res, n = [(matrix[0][0], 0, 0)], 0, len(matrix)
        for k in range(1, k + 1):
            res, row, col = heapq.heappop(heap)
            # first search in cols
            if not row and col < n - 1:
                heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))
            # then row-wise
            if row < n - 1:
                heapq.heappush(heap, (matrix[row + 1][col], row + 1, col))

        return res


if __name__ == "__main__":

    matrix = [
       [ 1,  5,  9],
       [10, 11, 13],
       [12, 13, 15]
    ]

    assert Solution().kthSmallest(matrix, 8) == 13
