"""
    Leetcode #518
"""


from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def helper(target, curr, idx):
            if target == 0:
                return 1

            if memo.get((idx, target)) is not None:
                return memo[(idx, target)]

            count = 0
            for i in range(idx, len(coins)):
                if target - coins[i] < 0: continue
                curr.append(coins[i])
                count += helper(target - coins[i], curr, i)
                curr.pop()

            memo[(idx, target)] = count
            return count

        helper(amount, [], 0)
        return helper(amount, [], 0)

    def change_DP(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount+1) for _ in range(len(coins)+1)]
        dp[0][0] = 1

        for i in range(1, len(coins)+1):
            dp[i][0] = 1
            for j in range(1, amount+1):
                # coin greater than amount
                if coins[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]

        return dp[-1][amount]



if __name__ == "__main__":

    solution = Solution()

    assert solution.change(5, [1, 2, 5]) == 4
    assert solution.change(3, [2]) == 0

    assert solution.change_DP(5, [1, 2, 5]) == 4
    assert solution.change_DP(3, [2]) == 0
