"""
    Leetcode #274
"""

from typing import List


class Solution:
    # similar to bucket sort
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citeCount = [0] * (n+1)
        for c in citations:
            if c >= n:
                citeCount[n] += 1
            else:
                citeCount[c] += 1

        i = n-1
        while i >= 0:
            citeCount[i] += citeCount[i+1]
            if citeCount[i+1] >= i+1:
                return i+1
            i -= 1
        return 0


if __name__ == "__main__":

    assert Solution().hIndex([3,0,6,1,5]) == 3
