"""
    Leetcode #309
"""


from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        free = 0
        have = cool = float('-inf')

        for p in prices:
            free, have, cool = max(free, cool), max(have, free - p), have + p

        return max(free, cool)


if __name__ == "__main__":

    assert Solution().maxProfit([1,2,3,0,2]) == 3
