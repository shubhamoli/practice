"""
    Leetcode #221
"""


from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        if not matrix[0]:
            return 0

        M = len(matrix)
        N = len(matrix[0])

        dp = [[-1] * (N+1) for i in range(M+1)]

        def helper(i, j):
            if i < 0 or i >= M or j < 0 or j >= N or matrix[i][j] == 0:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            if matrix[i][j] == 1:
                dp[i][j] = 1 + min(helper(i+1, j), helper(i, j+1), helper(i+1, j+1))
                return dp[i][j]


        maxi = 0
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 1:
                    maxi = max(maxi, helper(i, j))

        return maxi ** 2



if __name__ == "__main__":

    matrix = [
                [1,0,1,0,0],
                [1,0,1,1,1],
                [1,1,1,1,1],
                [1,0,0,1,0]
            ]
    assert Solution().maximalSquare(matrix) == 4

