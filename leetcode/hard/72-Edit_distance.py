"""
    Leetcode #72
"""


class Solution:
    memo = {}
    def minDistance(self, word1: str, word2: str, i: int = 0, j: int = 0) -> int:
        if i == len(word1) and j == len(word2):
            return 0
        
        if i == len(word1):
            return len(word2) - j

        if j == len(word2):
            return len(word1) - i

        if (i, j) not in self.memo:
            if word1[i] == word2[j]:
                ans = self.minDistance(word1, word2, i+1, j+1)

            else:
                insert = 1 + self.minDistance(word1, word2, i, j+1)
                delete = 1 + self.minDistance(word1, word2, i+1, j)
                replace = 1 + self.minDistance(word1, word2, i+1, j+1)

                ans = min(insert, delete, replace)

            self.memo[(i, j)] = ans

        return self.memo[(i, j)]

    # derived from above
    def minDistance_DP(self, word1, word2):

        m = len(word1)
        n = len(word2)

        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m+1):
            dp[i][0] = i

        for j in range(n+1):
            dp[0][j] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])


        return dp[-1][-1]


if __name__ == "__main__":

    solution = Solution()

    assert solution.minDistance("horse", "ros") == 3
    assert solution.minDistance_DP("intention", "execution") == 5
