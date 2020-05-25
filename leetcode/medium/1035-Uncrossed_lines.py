"""
    Leetcode #1035
"""

from typing import List


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        memo = [[-1] * len(B) for i in range(len(A))]

        def helper(i, j):
            if i >= len(A) or j >= len(B):
                return 0

            if memo[i][j] != -1:
                return memo[i][j]

            if A[i] == B[j]:
                memo[i][j] = 1 + helper(i+1, j+1)
                return memo[i][j]
            else:
                memo[i][j] = max(helper(i+1, j), helper(i, j+1))
                return memo[i][j]

        return helper(0, 0)

    def maxUncrossedLines_DP(self, A: List[int], B: List[int]) -> int:

        dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

        return dp[-1][-1]


if __name__ == "__main__":

    solution = Solution()

    assert solution.maxUncrossedLines([2,5,1,2,5], [10,5,2,1,5,2]) == 3
    assert solution.maxUncrossedLines_DP([1,3,7,1,7,5], [1,9,2,5,1]) == 2

