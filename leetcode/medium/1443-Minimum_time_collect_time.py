"""
    Leetcode #1443
"""


from typing import List
from collections import defaultdict


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree = defaultdict(list)

        # to avoid loop as graph is not unidirected
        visited = set()

        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        dist = 0
        def helper(node):
            nonlocal dist
            if node in visited: return False

            visited.add(node)
            found = hasApple[node]

            for child in tree[node]:
                if helper(child):
                    dist += 2
                    found = True

            return found or hasApple[node]

        helper(0)
        return dist


if __name__ == "__main__":

    solution = Solution()

    assert solution.minTime(7,
                            [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],
                            [False,False,True,False,True,True,False]) == 8
