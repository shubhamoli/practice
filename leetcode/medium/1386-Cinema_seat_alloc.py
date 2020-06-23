"""
    Leetcode #1386
"""


from typing import List
from collections import defaultdict

class Solution:
    def maxNumberOfFamilies_BF(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats = defaultdict(set)

        for i, j in reservedSeats:
            if j in [2,3,4,5]:
                seats[i].add(0)
            if j in [4,5,6,7]:
                seats[i].add(1)
            if j in [6,7,8,9]:
                seats[i].add(2)

        # max 2*n 4-consecutive seats can be there
        res = 2*n
        for i in seats:
            # if more than 3 occupied in a row
            # res -= 2
            # else -1
            if len(seats[i]) == 3:
                res -= 2
            else:
                res -= 1

        return res


if __name__ == "__main__":

    solution = Solution()

    assert solution.maxNumberOfFamilies_BF(2, [[2,1],[1,8],[2,6]]) == 2
    assert solution.maxNumberOfFamilies_BF(3, [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]) == 4

