"""
    Leetcode #1423
"""


from typing import List
from functools import lru_cache

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k == len(cardPoints):
            return sum(cardPoints)

        @lru_cache(None)
        def helper(i, j, k):
            if k == 0:
                return 0

            res = max(cardPoints[i]+helper(i+1, j, k-1), cardPoints[j]+helper(i, j-1, k-1))
            return res


        return helper(0, len(cardPoints)-1, k)

    # sliding window approach
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints)

        window = len(cardPoints) - k

        score = 0

        sum_window = sum(cardPoints[:window])

        i = 0
        while i + window <= len(cardPoints):
            if i > 0:
                sum_window -= cardPoints[i-1]
                sum_window += cardPoints[i+window-1]

            score = max(score, total - sum_window)
            i += 1

        return score



if __name__ == "__main__":

    solution = Solution()

    assert solution.maxScore([1,2,3,4,5,6,1], 3) == 12
    assert solution.maxScore([2,2,2], 2) == 4

