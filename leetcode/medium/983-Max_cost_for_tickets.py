"""
    Leetcode #983
"""

from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}
        def helper(i):
            if i == len(days):
                return 0

            if memo.get(i) is not None:
                return memo[i]

            memo[i] = float("inf")

            # buy a day-pass, or week-pass, or month-pass
            singleDay = costs[0] + helper(nextDayIndex(i, 1))
            week = costs[1] + helper(nextDayIndex(i, 7))
            month = costs[2] + helper(nextDayIndex(i, 30))

            # save minimum one
            memo[i] = min(singleDay, week, month)

            return memo[i]

        def nextDayIndex(i, j):
            end = days[i] + j - 1
            new = i
            while new < len(days) and days[new] <= end:
                new += 1

            return new

        # DFS + memo
        return helper(0)


if __name__ == "__main__":

    solution = Solution()

    assert solution.mincostTickets([1,4,6,7,8,20], [2,7,15]) == 11
    assert solution.mincostTickets([1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15]) == 17

