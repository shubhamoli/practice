"""
    Leetcode #973
"""


import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        heap = []

        for x, y in points:
            dist = -(x*x + y*y)

            if len(heap) == K:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))


        return [[x, y] for (dist, x, y) in heap]


if __name__ == "__main__":

    solution = Solution()

    assert solution.kClosest([[1,3],[-2,2]], 1) == [[-2,2]]
