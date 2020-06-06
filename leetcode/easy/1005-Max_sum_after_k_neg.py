"""
    Leetcode #1005
"""


from typing import List
import heapq

class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        heapq.heapify(A)
        i = 0
        while i < K:
            _min = heapq.heappop(A)
            heapq.heappush(A, _min * -1)
            i += 1

        return sum(A)


if __name__ == "__main__":

    solution = Solution()

    assert solution.largestSumAfterKNegations([4,2,3], 1) == 5
    assert solution.largestSumAfterKNegations([3,-1,0,2], 3) == 6
