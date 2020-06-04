"""
    Leetcode #914
"""


from typing import List
from collections import Counter
import math

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if not deck or len(deck) < 2:
            return False

        count = list(Counter(deck).values())

        tmp = count[0]
        for i in count[1:]:
            tmp = math.gcd(tmp, i)

        return tmp >= 2


if __name__ == "__main__":

    solution = Solution()

    assert solution.hasGroupsSizeX([1,2,3,4,4,3,2,1]) == True
    assert solution.hasGroupsSizeX([1,1,1,2,2,2,3,3]) == False
    assert solution.hasGroupsSizeX([1,1,2,2,2,2]) == True

