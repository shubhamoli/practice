"""
    Leetcode #1395
"""

from typing import List
from collections import defaultdict


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        if not rating:
            return 0

        def helper(curr, idx):
            nonlocal count
            if len(curr) == 3:
                if curr[0] <= curr[1] <= curr[2]:
                    count += 1
                if curr[0] >= curr[1] >= curr[2]:
                    count += 1

            for i in range(idx, len(rating)):
                curr.append(rating[i])
                helper(curr, i+1)
                curr.pop()

        count = 0
        helper([], 0)
        return count

    def numTeams_DP(self, rating: List[int]) -> int:

        lesser = defaultdict(int)
        greater = defaultdict(int)

        for i in range(len(rating)-1):
            for j in range(i+1, len(rating)):
                if rating[i] < rating[j]:
                    greater[i] += 1
                else:
                    lesser[i] += 1

        res = 0
        for i in range(len(rating)-2):
            for j in range(i+1, len(rating)):
                if rating[i] < rating[j]:
                    res += greater[j]
                else:
                    res += lesser[j]

        return res


    def numTeams_OTHER(self, rating: List[int]) -> int:

        count = 0

        for i in range(len(rating)):
            ls, rg = 0, 0
            lg, rs = 0, 0
            for j in range(i):
                if rating[i] < rating[j]:
                    ls += 1
                elif rating[i] > rating[j]:
                    lg += 1

            for k in range(i+1, len(rating)):
                if rating[i] < rating[k]:
                    rs += 1
                elif rating[i] > rating[k]:
                    rg += 1

            count += (ls * rg) + (lg * rs)

        return count



if __name__ == "__main__":

    solution = Solution()

    assert solution.numTeams([2,5,3,4,1]) == 3
    assert solution.numTeams([2,1,3]) == 0

    assert solution.numTeams_DP([2,5,3,4,1]) == 3
    assert solution.numTeams_DP([2,1,3]) == 0

    assert solution.numTeams_OTHER([2,5,3,4,1]) == 3
    assert solution.numTeams_OTHER([2,1,3]) == 0

