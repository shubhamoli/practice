"""
    Leetcode #528
"""

from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self._weights = w

        for i in range(1, len(w)-1):
            self._weights[i] += self._weights[i-1]

        self._sum = self._weights[-1]

    def pickIndex(self) -> int:
        seed = random.randint(1, self._sum)
        l, r = 0, len(self._weights) - 1

        while l < r:
            mid = (l+r) // 2
            if seed < self._weights[mid]:
                r = mid
            else:
                l = mid + 1

        return l

