"""
    Leetcode #1317
"""

from typing import List

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        if not mat or not mat[0]:
            return []

        M = len(mat)
        N = len(mat[0])
        answer = [[0] * N for _ in range(M)]

        def calcSum(i, j):
            _sum = 0
            for k in range(max(0, i-K), min(i+K+1, M)):
                for l in range(max(0, j-K), min(j+K+1, N)):
                    _sum += mat[k][l]

            return _sum

        for i in range(M):
            for j in range(N):
                answer[i][j] = calcSum(i, j)

        return answer


    def matrixBlockSum_OPTI(self, mat: List[List[int]], K: int) -> List[List[int]]:
        if not mat or not mat[0]:
            return []

        M = len(mat)
        N = len(mat[0])

        rangeSum = [[0] * (N+1) for _ in range(M+1)]

        for i in range(M):
            for j in range(N):
                rangeSum[i+1][j+1] = mat[i][j] + rangeSum[i+1][j] + rangeSum[i][j+1] - rangeSum[i][j]

        answer = [[0] * N for _ in range(M)]

        for i in range(M):
            for j in range(N):
                r1, c1, r2, c2 = max(0, i-K), max(0, j-K), min(i+K+1, M), min(j+K+1, N)
                answer[i][j] = rangeSum[r2][c2] - rangeSum[r1][c2] - rangeSum[r2][c1] + rangeSum[r1][c1]

        return answer



if __name__ == "__main__":

    solution = Solution()

    matrix = [[1,2,3],
              [4,5,6],
              [7,8,9]]

    assert solution.matrixBlockSum(matrix, 1) == [[12,21,16],[27,45,33],[24,39,28]]
    assert solution.matrixBlockSum(matrix, 2) == [[45,45,45],[45,45,45],[45,45,45]]

    assert solution.matrixBlockSum_OPTI(matrix, 1) == [[12,21,16],[27,45,33],[24,39,28]]
    assert solution.matrixBlockSum_OPTI(matrix, 2) == [[45,45,45],[45,45,45],[45,45,45]]

