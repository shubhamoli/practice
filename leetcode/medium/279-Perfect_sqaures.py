"""
    Leetcode #279
"""

class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i**2 for i in range(1,int(n**0.5)+1)]
        dp = [n + 1 for i in range(n + 1)]
        dp[0] = 0
        for i in squares:
            for j in range(1 , n + 1):
                if j >= i:
                    dp[j] = min(dp[j] , 1 + dp[j - i])
        return dp[-1]

if __name__ == "__main__":

    assert Solution().numSquares(12) == 3   # 4+4+4
    assert Solution().numSquares(13) == 2   # 4+9
