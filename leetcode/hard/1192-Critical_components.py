"""
    Leetcode #1192
"""


from typing import List
import collections

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = collections.defaultdict(list)

        for conn in connections:
            graph[conn[0]].append(conn[1])
            graph[conn[1]].append(conn[0])

        N = len(connections)
        connections = set(map(tuple, (map(sorted, connections))))
        rank =  [-2] * N  # -2 unvisited, >0 visiting, N visited

        def dfs(node, depth):
            if rank[node] >= 0:
                return rank[node]

            rank[node] = depth
            min_depth = N

            for neighbor in graph[node]:
                if rank[neighbor] == depth - 1:
                    continue

                back_depth = dfs(neighbor, depth+1)

                # cycle detected
                # remove this from connections
                if back_depth <= depth:
                    connections.discard(tuple(sorted((node, neighbor))))

                min_depth = min(min_depth, back_depth)

            rank[node] = N
            return min_depth


        dfs(0, 0)
        return list(connections)

