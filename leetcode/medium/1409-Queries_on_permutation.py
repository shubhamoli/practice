"""
    Leetcode #1409
"""


from typing import List
from collections import deque

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        res = []

        perm = deque(list(range(1, m+1)))

        for i in range(len(queries)):
            idx = perm.index(queries[i])
            res.append(idx)
            perm.remove(queries[i])
            perm.appendleft(queries[i])

        return res


if __name__ == "__main__":

    solution = Solution()

    assert solution.processQueries([3,1,2,1], 5) == [2,1,2,1]
    assert solution.processQueries([4,1,2,2], 4) == [3,1,2,0]

