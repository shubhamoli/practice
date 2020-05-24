"""
    Leetcode # 347
"""

import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        res = []
        dic = Counter(nums)

        max_heap = [(-val, key) for key, val in dic.items()]
        heapq.heapify(max_heap)

        for i in range(k):
            res.append(heapq.heappop(max_heap)[1])

        return res


if __name__ == "__main__":

    solution = Solution()

    assert solution.topKFrequent([1,1,1,2,2,3], 2) == [1, 2]
    assert solution.topKFrequent([1], 1) == [1]
