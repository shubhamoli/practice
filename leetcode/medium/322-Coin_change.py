"""
    Leetcode #322
"""


from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = float('inf')
        dp = [0] + [MAX for i in range(amount)]

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i-c] + 1)

        if dp[-1] == MAX:
            return -1

        return dp[-1]


if __name__ == "__main__":

    assert Solution().coinChange([1, 2, 5], 11) == 3
    assert Solution().coinChange([2], 3) == -1
