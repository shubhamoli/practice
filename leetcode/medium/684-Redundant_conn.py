"""
    Leetcode #684
"""


from typing import List
from collections import defaultdict

class Solution:
    # Time: O(N^2)
    # Space: O(N)
    def findRedundantDirectedConnection_DFS(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)

        def hasPath(u, v):
            if u not in visited:
                visited.add(u)

                if u == v:
                    return True

                return any(hasPath(nei, v) for nei in graph[u])


        # detect cycle while creating graph
        for u, v in edges:
            visited = set()

            if u in graph and v in graph and hasPath(u, v):
                return [u, v]

            graph[u].add(v)
            graph[v].add(u)


    def findRedundantDirectedConnection_UNION_FIND(self, edges: List[List[int]]) -> List[int]:
        p = list(range(len(edges) + 1))
        def find(x):
            while p[x] != x:
                p[x] = p[p[x]]
                x = p[x]
            return p[x]
        for a, b in edges:
            pa, pb = find(a), find(b)
            if pa == pb: return [a, b]
            p[pa] = p[pb]




if __name__ == "__main__":

    solution = Solution()

    assert solution.findRedundantDirectedConnection_DFS([[1,2], [1,3], [2,3]]) == [2, 3]
    assert solution.findRedundantDirectedConnection_DFS([[1,2], [2,3], [3,4], [4,1], [1,5]]) == [4, 1]

    assert solution.findRedundantDirectedConnection_UNION_FIND([[1,2], [1,3], [2,3]]) == [2, 3]
    assert solution.findRedundantDirectedConnection_UNION_FIND([[1,2], [2,3], [3,4], [4,1], [1,5]]) == [4, 1]

