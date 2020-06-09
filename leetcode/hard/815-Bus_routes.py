"""
    Leetcode #815
"""


from typing import List
from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0

        queue = deque()
        graph = defaultdict(set)
        routes = list(map(set, routes))
        seen, targets = set(), set()

        for i in range(len(routes)):
            if S in routes[i]:
                seen.add(i)
                queue.append((i, 1))

            if T in routes[i]:
                targets.add(i)

            for j in range(i+1, len(routes)):
                if routes[i] & routes[j]:
                    graph[i].add(j)
                    graph[j].add(i)

        while queue:
            curr, count = queue.popleft()
            if curr in targets:
                return count

            for n in graph[curr]:
                if n not in seen:
                    queue.append((n, count+1))
                    seen.add(n)


        return -1


if __name__ == "__main__":

    solution = Solution()

    assert solution.numBusesToDestination([[1, 2, 7], [3, 6, 7]], 1, 6) == 2
