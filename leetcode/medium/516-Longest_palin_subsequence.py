"""
    Leetcode #516
"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = [[0] * len(s) for _ in range(len(s))]
        def helper(l, r):
            if l == r:
                return 1
            if l > r:
                return 0

            if memo[l][r]:
                return memo[l][r]

            if s[l] == s[r]:
                memo[l][r] = 2 + helper(l+1, r-1)
            else:
                memo[l][r] = max(helper(l+1, r), helper(l, r-1))

            return memo[l][r]

        return helper(0, len(s)-1)


    def longestPalindromeSubseq_DP(self, s: str) -> int:
        # reverse the string
        # and problem will be similar to finding common subseq
        # and in case of palindrome, it'll be common subseq in both
        t = s[::-1]
        dp = [[0 for i in range(len(t) + 1)] for j in range(len(s) + 1)]

        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]


if __name__ == "__main__":

    solution = Solution()

    assert solution.longestPalindromeSubseq("bbbab") == 4 # "bbbb"
    assert solution.longestPalindromeSubseq("cbbd") == 2 # "bb"

    assert solution.longestPalindromeSubseq_DP("bbbab") == 4 # "bbbb"
    assert solution.longestPalindromeSubseq_DP("cbbd") == 2 # "bb"

