"""
    Leetcode #310
"""

from typing import List
from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        d = defaultdict(set)

        for u, v in edges:
            d[u].add(v)
            d[v].add(u)

        s = set(range(n))

        # remove leaves till we get to at most 2 nodes
        while len(s) > 2:
            leaves = set(i for i in s if len(d[i]) == 1)
            s -= leaves
            for i in leaves:
                for j in d[i]:
                    d[j].remove(i)

        # return remaining at most 2 nodes
        return list(s)


if __name__ == "__main__":

    assert Solution().findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]) == [1]

