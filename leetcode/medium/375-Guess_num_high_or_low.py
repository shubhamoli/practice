"""
    Leetcode #375
"""


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(n+1)]
        for j in range(2, n+1):
            for i in range(j-1, 0, -1):
                # find every k in range i...j
                # dp[i][j] =  min of (currnet k + max i...k-1 or k+1 .. j)
                dp[i][j] = min(k + max(dp[i][k-1], dp[k+1][j]) for k in range(i, j))

        return dp[1][n]


if __name__ == "__main__":

    solution = Solution()

    assert solution.getMoneyAmount(10) == 16
