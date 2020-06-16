"""
    Leetcode #994
"""


from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1

        M = len(grid)
        N = len(grid[0])

        fresh = 0
        q = deque()

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        count = 0
        while q:
            count += 1
            size = len(q)

            for _ in range(size):
                i, j = q.popleft()

                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    x, y = i + dx, j + dy

                    if x < 0 or x >= M or y < 0 or y >= N or grid[x][y] in [0, 2]:
                        continue

                    grid[x][y] = 2
                    fresh -= 1

                    q.append((x, y))


        # decreasing count by 1 because we are increasing (inside loop) it before doing anything
        return count - 1 if fresh == 0 else -1



if __name__ == "__main__":

    solution = Solution()

    grid = [[2,1,1],
            [1,1,0],
            [0,1,1]]

    assert solution.orangesRotting(grid) == 4

    grid = [[2,1,1],
            [0,1,1],
            [1,0,1]]

    assert solution.orangesRotting(grid) == -1
